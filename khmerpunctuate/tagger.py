import os
import numpy as np
import appdirs
import shutil
from khmerpunctuate.utils import download_file
from sentencepiece import SentencePieceProcessor
from onnxruntime import InferenceSession, SessionOptions, GraphOptimizationLevel

TOKEN_IDX_MAP = {
  0: "",
  1: " ",
  2: "!",
  3: "។",
  4: "?",
  5: "៖",
  6: "។\n",
  7: "B-NUMBER",
  8: "I-NUMBER",
  9: "B-QUOTE",
  10: "I-QUOTE",
}

SPM_MODEL_PATH = os.path.join(os.path.dirname(__file__), "sentencepiece.bpe.model")
MODEL_PUBLIC_URL = "https://huggingface.co/seanghay/khmer-punctuation-restore/resolve/main/deep-punctuation-v2.onnx"
MODEL_DIR = os.path.join(appdirs.user_cache_dir(), "khmerpunctuate")

MODEL_PATH = os.path.join(MODEL_DIR, "deep-punctuation-v2.onnx")
MODEL_PATH_TMP = os.path.join(MODEL_DIR, "deep-punctuation-v2.onnx.tmp")

if not os.path.exists(MODEL_PATH):
  os.makedirs(MODEL_DIR, exist_ok=True)
  download_file(MODEL_PUBLIC_URL, MODEL_PATH_TMP)
  shutil.move(MODEL_PATH_TMP, MODEL_PATH)

sess_options = SessionOptions()
sess_options.graph_optimization_level = GraphOptimizationLevel.ORT_DISABLE_ALL
session = InferenceSession(MODEL_PATH, sess_options=sess_options)
spm = SentencePieceProcessor(model_file=SPM_MODEL_PATH)

def punctuate(words, max_length=256):
  word_pos = 0
  decode_idx = 0
  while word_pos < len(words):
    x = [0]
    y_mask = [0]
    while len(x) < max_length and word_pos < len(words):
      tokens = [token_id + 1 for token_id in spm.encode(words[word_pos])]
      if len(tokens) + len(x) >= max_length:
        break
      else:
        for i in range(len(tokens) - 1):
          x.append(tokens[i])
          y_mask.append(0)
        x.append(tokens[-1])

        y_mask.append(1)
        word_pos += 1

    x.append(2)
    y_mask.append(0)

    if len(x) < max_length:
      x = x + [1 for _ in range(max_length - len(x))]
      y_mask = y_mask + [0 for _ in range(max_length - len(y_mask))]

    attn_mask = [1 if token != 1 else 0 for token in x]
    x = np.expand_dims(x, axis=0)
    attn_mask = np.expand_dims(attn_mask, 0)
    input_values = {"input_ids": x, "attention_masks": attn_mask}
    logits = session.run(None, input_values)[0]
    outputs = np.argmax(logits, axis=2).squeeze(0)

    for idx, value in enumerate(y_mask):
      if value != 1:
        continue
      label_id = outputs[idx]
      yield (words[decode_idx], TOKEN_IDX_MAP[label_id], label_id)
      decode_idx += 1
