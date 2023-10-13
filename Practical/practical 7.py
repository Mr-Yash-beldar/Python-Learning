# import re
# txt="Walk when you talk"
# x=re.sub("\s","@",txt)
# print(x)


# import re
# name="Yashodip Beldar  Pursuing B.Tech from RCPIT Shirpur"
# y=re.sub("\s","*",name,2)
# print(y)

# import re
# name="Yashodip Beldar Pursuing B.Tech from RCPIT Shirpur"
# y=re.search("\s",name)
# print(y)

# import nltk
# from nltk.tokenize import word_tokenize
# from nltk import pos_tag
# import string

# Download NLTK data (only need to do this once)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')

# Input sentence
# sentence = "NLTK . is, powerf?ul library ? for natural language processing."

# words = word_tokenize(sentence)
# # Remove punctuation
# words = [word for word in words if word not in string.punctuation]

# # Perform part-of-speech tagging
# # pos_tags = pos_tag(words)

# # Print the part-of-speech tags
# print(words)


import nltk
from nltk.tokenize import RegexpTokenizer

# Create a custom tokenizer that splits on tabs
tokenizer = RegexpTokenizer(r'\t')

# Input string with tabs
text = "This\tis\ta\ttab\tseparated\tstring."

# Tokenize the string using the custom tokenizer
tokens = tokenizer.tokenize(text)

# Print the tokens
print(tokens)


