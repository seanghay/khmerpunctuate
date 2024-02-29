from khmernormalizer import normalize
from khmercut import tokenize
from khmerpunctuate import punctuate

text = normalize(
  "អយ្យការអមសាលាដំបូងរាជធានីភ្នំពេញបានព្រមានថានឹងចេញដីកាបញ្ជាឲ្យបង្ខំនិងឲ្យឃុំខ្លួនតាមនីតិវិធីប្រសិនបើលោករ៉ុងឈុនដែលបច្ចុប្បន្នជាទីប្រឹក្សាគណបក្សកម្លាំងជាតិមិនបានបង់ប្រាក់ពិន័យចំនួន២លានរៀលឲ្យបានមុនថ្ងៃទី០៤ខែមីនាឆ្នាំ២០២៤ទេនោះ"
)
tokens = tokenize(text)

output_text = ""
for token, punctuation, punctuation_id in punctuate(tokens):
  output_text += token + punctuation

print(output_text)
