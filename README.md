## Punctuation Restoration for Khmer language

Built with [[xashru/punctuation-restoration]](https://github.com/xashru/punctuation-restoration) using [[xlm-roberta-base]](https://huggingface.co/FacebookAI/xlm-roberta-base) and then exported to `onnxruntime`


### Install

```shell
pip install khmerpunctuate

# Or
pip install git+https://github.com/seanghay/khmerpunctuate.git
```

### Usage

```python
from khmernormalizer import normalize
from khmercut import tokenize
from khmerpunctuate import punctuate

text = normalize("អយ្យការអមសាលាដំបូងរាជធានីភ្នំពេញបានព្រមានថានឹងចេញដីកាបញ្ជាឲ្យបង្ខំនិងឲ្យឃុំខ្លួនតាមនីតិវិធីប្រសិនបើលោករ៉ុងឈុនដែលបច្ចុប្បន្នជាទីប្រឹក្សាគណបក្សកម្លាំងជាតិមិនបានបង់ប្រាក់ពិន័យចំនួន២លានរៀលឲ្យបានមុនថ្ងៃទី០៤ខែមីនាឆ្នាំ២០២៤ទេនោះ")
tokens = tokenize(text)

output_text = ""

for token, punct, punct_id in punctuate(tokens):
  output_text += token + punct

print(output_text)
```

```
អយ្យការអមសាលាដំបូងរាជធានីភ្នំពេញ បានព្រមានថា នឹងចេញដីកាបញ្ជាឱ្យបង្ខំ និងឱ្យឃុំខ្លួនតាមនីតិវិធី ប្រសិនបើលោក រ៉ុង ឈុន ដែលបច្ចុប្បន្នជាទីប្រឹក្សាគណបក្សកម្លាំងជាតិ មិនបានបង់ប្រាក់ពិន័យចំនួន២លានរៀល ឱ្យបានមុនថ្ងៃទី០៤ ខែមីនា ឆ្នាំ២០២៤ទេនោះ។
```

### License

`MIT`