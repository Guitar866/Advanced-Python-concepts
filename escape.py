import re

text = "a.b"
pattern = re.escape(text)

print(pattern)
print(re.findall(pattern, "a.b ab"))