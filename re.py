import re

text = "hello world"
regex = re.compile("[a-z]+.[a-z]")
result =  regex.match(text)

print(result)