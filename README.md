## Punctuation Restoration for Khmer language

Built with [[xashru/punctuation-restoration]](https://github.com/xashru/punctuation-restoration) using [[xlm-roberta-khmer-small]](https://huggingface.co/seanghay/xlm-roberta-khmer-small) and then exported to `onnxruntime`


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
អយ្យការអមសាលាដំបូងរាជធានីភ្នំពេញ បានព្រមានថា នឹងចេញដីកាបញ្ជាឱ្យបង្ខំ និងឱ្យឃុំខ្លួនតាមនីតិវិធី ប្រសិនបើលោក រ៉ុង ឈុន ដែលបច្ចុប្បន្នជាទីប្រឹក្សាគណបក្សកម្លាំងជាតិ មិនបានបង់ប្រាក់ពិន័យចំនួន២លានរៀល ឱ្យបានមុនថ្ងៃទី០៤ខែមីនា ឆ្នាំ២០២៤ទេនោះ 
```


### Example

The example below is available on [[Google Colab]](https://colab.research.google.com/drive/18lHUdJGHD55TTklwWz4d6CNOVfRYMoFG?usp=sharing)

Model file is hosted on [[HuggingFace]](https://huggingface.co/seanghay/khmer-punctuation-restore)


### Evaluation

**XLM RoBERTa Khmer: (49M params)**


| Precision | 0.95528402 | 0.79168481 | 0.85507246 | 0.74523436 | 0.7877551  | 0.79452055 | 0.62296801 | 0.96415685 | 0.98617407 | 0.67324778 | 0.57505285 | 0.8240493  |
|-----------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
| Recall    | 0.96957471 | 0.73475191 | 0.13947991 | 0.86194329 | 0.69010727 | 0.63736264 | 0.08452508 | 0.96852034 | 0.99192858 | 0.22035541 | 0.21068939 | 0.77592102 |
| F1 score  | 0.96237631 | 0.76215662 | 0.2398374  | 0.79935128 | 0.73570521 | 0.70731707 | 0.14885353 | 0.96633367 | 0.98904296 | 0.33203505 | 0.30839002 | 0.79926129 |

Accuracy: 0.930086988701306


---

**XLM RoBERTa Base (279M params)**

| Metric    | 1          | 2          | 3          | 4          | 5          | 6          | 7          | 8          | 9          | 10         | 11         | 12         |
|-----------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|------------|
| Precision | 0.96143204 | 0.82657744 | 0.88399072 | 0.79077633 | 0.82349285 | 0.85393258 | 0.55724225 | 0.96397178 | 0.98844483 | 0.72191436 | 0.67759563 | 0.8508466  |
| Recall    | 0.97304725 | 0.77059714 | 0.45035461 | 0.90182234 | 0.78963051 | 0.83516484 | 0.18804696 | 0.97943409 | 0.99381541 | 0.46300485 | 0.43222308 | 0.81077656 |
| F1 score  | 0.96720478 | 0.79760625 | 0.59671104 | 0.84265665 | 0.80620627 | 0.84444444 | 0.28120013 | 0.97164142 | 0.99112284 | 0.56417323 | 0.52778435 | 0.83032843 |
| Accuracy  | 0.9399183767909306 |            |            |            |            |            |            |            |            |            |            |            |


### License

`MIT`