import re

text = "life is too shrot"
regex = re.compile("[a-z]+")
result =  regex.finditer(text)
print(result)