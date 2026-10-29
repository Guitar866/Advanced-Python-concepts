import re

text = "My numbers are 10, 20, 30"
result = re.findall(r'\d+', text)

print(result)