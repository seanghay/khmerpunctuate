from khmernormalizer import normalize
from khmercut import tokenize
from khmerpunctuate import punctuate

text = normalize("អយ្យការអមសាលាដំបូងរាជធានីភ្នំពេញបានព្រមានថានឹងចេញដីកាបញ្ជាឲ្យបង្ខំនិងឲ្យឃុំខ្លួនតាមនីតិវិធីប្រសិនបើលោករ៉ុងឈុនដែលបច្ចុប្បន្នជាទីប្រឹក្សាគណបក្សកម្លាំងជាតិមិនបានបង់ប្រាក់ពិន័យចំនួន២លានរៀលឲ្យបានមុនថ្ងៃទី០៤ខែមីនាឆ្នាំ២០២៤ទេនោះ")
tokens = tokenize(text)

output_text = ""
for token, punct, punct_id in punctuate(tokens):
  # exclude special tokens like I-NUMBER, B-NUMBER, I-QOUTE and B-QOUTE
  if punct_id < 7:
    output_text += token + punct
  else:
    output_text += token

print(output_text)

# អយ្យការអមសាលាដំបូងរាជធានីភ្នំពេញ បានព្រមានថា នឹងចេញដីកាបញ្ជាឱ្យបង្ខំ និងឱ្យឃុំខ្លួនតាមនីតិវិធី ប្រសិនបើលោក រ៉ុង ឈុន ដែលបច្ចុប្បន្នជាទីប្រឹក្សាគណបក្សកម្លាំងជាតិ មិនបានបង់ប្រាក់ពិន័យចំនួន២លានរៀល ឱ្យបានមុនថ្ងៃទី០៤ខែមីនា ឆ្នាំ២០២៤ទេនោះ 
