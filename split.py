import re

text = "apple,banana;orange mango"
result = re.split(r'[,; ]', text)

print(result)