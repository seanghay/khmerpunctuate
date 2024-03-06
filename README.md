## Punctuation Restoration for Khmer language

Built with [[xashru/punctuation-restoration]](https://github.com/xashru/punctuation-restoration) using [[xlm-roberta-base]](https://huggingface.co/FacebookAI/xlm-roberta-base) and then exported to `onnxruntime`


### Install

```shell
pip install khmerpunctuate

# Or
pip install git+https://github.com/seanghay/khmerpunctuate.git
```

### Usage

Supported token types are

```python
{
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
```

```python
from khmernormalizer import normalize
from khmercut import tokenize
from khmerpunctuate import punctuate

text = normalize("អយ្យការអមសាលាដំបូងរាជធានីភ្នំពេញបានព្រមានថានឹងចេញដីកាបញ្ជាឲ្យបង្ខំនិងឲ្យឃុំខ្លួនតាមនីតិវិធីប្រសិនបើលោករ៉ុងឈុនដែលបច្ចុប្បន្នជាទីប្រឹក្សាគណបក្សកម្លាំងជាតិមិនបានបង់ប្រាក់ពិន័យចំនួន២លានរៀលឲ្យបានមុនថ្ងៃទី០៤ខែមីនាឆ្នាំ២០២៤ទេនោះ")
tokens = tokenize(text)

output_text = ""
for token, punct, punct_id in punctuate(tokens):
  # exclude special tokens like I-NUMBER, B-NUMBER, I-QUOTE and B-QUOTE
  if punct_id < 7:
    output_text += token + punct
  else:
    output_text += token

print(output_text)
```

```
អយ្យការអមសាលាដំបូងរាជធានីភ្នំពេញ បានព្រមានថា នឹងចេញដីកាបញ្ជាឱ្យបង្ខំ និងឱ្យឃុំខ្លួនតាមនីតិវិធី ប្រសិនបើលោក រ៉ុង ឈុន ដែលបច្ចុប្បន្នជាទីប្រឹក្សាគណបក្សកម្លាំងជាតិ មិនបានបង់ប្រាក់ពិន័យចំនួន២លានរៀលឱ្យបានមុនថ្ងៃទី០៤ខែមីនា ឆ្នាំ២០២៤ទេនោះ
```


### Example

The example below is available on [[Google Colab]](https://colab.research.google.com/drive/18lHUdJGHD55TTklwWz4d6CNOVfRYMoFG?usp=sharing)

Model file is hosted on [[HuggingFace]](https://huggingface.co/seanghay/khmer-punctuation-restore)


### License

`MIT`