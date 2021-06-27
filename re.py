import re
data = """
aa@gmail.com
bb@naver.com
"""
regex = re.compile("^[a-z0-9]+@[a-z]+.[a-z]{2,4}$",re.MULTILINE|re.IGNORECASE)
result = regex.findall(data)
print(result)

