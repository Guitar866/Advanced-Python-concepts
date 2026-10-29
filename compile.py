import re

pattern = re.compile(r'\d+')
text = "I have 25 books and 10 pens"

result = pattern.findall(text)
print(result)