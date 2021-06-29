# re

## 정규표현식이란
```
문자열을 처리하는 방법중 하나로 특정한 조건의 문자를 검색하거나 추출, 치환 하는데 사용됩니다.
```
### 기본 메타 문자
기호|설명
---|---
. | 모든 문자
\| | or
[] | 구성원중 하나와 일치
^ | []안에 사용된경우 제외(위치지정자와 같음)
\- | 범위 정의
\\ | 다음에 오는 문자를  이스케이프

<br>
<br>
<br>

### 수량자
기호|설명
---|---
\* | 앞의 문자를 0개 이상 탐욕적으로 찾기
\*? | *를 lazy 수량자로 찾기
\+ | 하나이상 반복
+? | +를 lazy 수량자로 찾기
? | 앞의 문자를 0개나 1개 찾기
{n} | 정확히 n번 일치하는 경우 찾기
{n,m} | n번에서 m번 일치하는 경우 찾기

<br>
<br>
<br>

### 위치 관련(\를 사용할떄는 r을 사용)
기호 | 설명
---|---
^|시작부분에서 검사
$|문자열의 끝과 일치
\b|단어경계와 일치
\B|단어 비경계 일치
\A|^와 동일하지만 re.MULTILINE을 사용한경우에도 처음에만 매치

<br>
<br>
<br>

### 특수 기능
기호 | 설명
---|---
\d | 모든 숫자와 일치
\D | \d의 반대
\s | 공백과 일치
\S | \s의 반대
\w | 영숫자 문자 밑줄 과 일치
\W | \w의 반대

<br>
<br>
<br>

## Regex 모듈 re
```
re.compile의 결과로 돌려주는 reex 객체를 사용합니다.
```
```python
import re

text = "hello world"
regex = re.compile("[a-z]+")
```

### 컴파일된 객체의 메서드

메서드 | 기능
---|---
match() | 처음부터 정규식과 매치되는지 확인
search() | 전체를 검색하여 정규식과 매치되는지 확인
findall() | 매치되는 모든 문자열을 list로 반환
finditer() | 정규식과 매치되는 모든 문자열을 iter 객체로 반환

### match()
```python
import re

text = "hello world"
regex = re.compile("[a-z]+.[a-z]")
result =  regex.match(text)
print(result)
```

### search()
```python
import re

text = "12345 hello world"
regex = re.compile("[a-z]+.[a-z]")
result =  regex.search(text)
print(result)
```

### findall()
```python
import re

text = "life is too shrot"
regex = re.compile("[a-z]+")
result =  regex.findall(text)
print(result)
```

### finditer()
```python
import re

text = "life is too shrot"
regex = re.compile("[a-z]+")
result =  regex.finditer(text)
print(result)
```

## match 객체의 메서드
```
match 객체는 검색된 문자열과, 위치를 확인하는 메서드를 제공합니다.
group, start, end, span 메서드를 통해 확인할 수 있습니다.
저는 result라는 변수명에 담아놓았습니다.
```

```python
import re
text = "12345 hello world"
regex = re.compile("[a-z]+.[a-z]")
result =  regex.search(text)
print(result)
```

## 모듈 단위로 축약하여 사용
```python   
import re
text = "hello world"
result = re.match('[a-z]', text)
print(result)
```

## 컴파일 옵션
옵션 | 기능
---|---
DOTALL(S)|. 이 줄바꿈 문자를 포함하여 모든 문자와 매치
IGNORECASE(I) | 대소문자에 관계 없이 매치
MULTILINE(M) | 여러줄과 매치(^, $를 사용하여 확인)
VERBOSE | verbose모드를 사용


### DOTALL, S
```python
# DOTALL 예제
import re
regex1 =  re.compile('a.b')
result1 = regex1.match('a\nb')

regex2 = re.compile('a.b', re.DOTALL)
result2 = regex2.match('a\nb')
```
```
여러줄로 이루어진 문자열에서 \n에 상관없이 검색이 가능합니다.
```

### IGNORECASE, I
```python
# IGNORECASE 예제
import re
regex =  re.compile('[a-z]+', re.I)
result = regex.match('HELLO')
print(result)
```

### MULTILINE, M
```python
# MULTILINE 예제
import re

# python으로 시작하고 space를 하나 포함하고 word가 반복
p = re.compile("^python\s\w+", re.MULTILINE)

data = """python one
life is too short
python two
you need python
python three"""

print(p.findall(data))
```
```
re.MULTILINE 옵션을 사용하면  
 ^, $ 메타 문자를 문자열의 모든 줄에 적용할수 있습니다.
```

### VERBOSE, X
줄바꿈, 주석을 위해 사용됩니다.
[]외부에 들어간 주석, whitespace는 모두 제거됩니다.

```python
import re
data = """
aa@gmail.com
bb@naver.com
"""
regex = re.compile("""
^[a-z0-9]+          # 숫자나 문자 반복
@[a-z]+             # @에 숫자조합 반복
.[a-z]{2,4}$        # .에 2~4번 반복되는 문자 반복(.com)
"""
,re.MULTILINE|re.IGNORECASE|re.VERBOSE)
result = regex.findall(data)
print(result)
```

### 백슬래시 관련
\section 등 백슬래시가 들어간 문자열을 찾기위한 정규식에서 사용됩니다.  
정규식 앞에 r을 추가합니다.
```python
import re

data = "\section"
regex1 = re.compile("\section")
result1 = regex1.match(data)
print(result1)

print("#################################")

# 백슬래시는 뒤에 문자를 문자 그대로 읽으라는 기호이므로 
# \\을 \로 변경시키고, 총 네개의 백슬래시가 필요합니다.
regex2 = re.compile("\\\\section")
result2 = regex2.match(data)
print(result2)

print("#################################")

# 앞에 r을 붙여 두개만 사용합니다.
regex3 = re.compile(r"\\section")
result3 = regex3.match(data)
print(result3)

```

### 그루핑
()기호를 사용하여 group 화 시켜서 사용할 수 있다.
```python
import re

data = "Tom 010-1234-5678"

regex = re.compile(r"""
(\w+)\s             # 문자반복, 공백
(\d+[-]\d+[-]\d+)   # 숫자반복-숫자반복-숫자반복
""", re.VERBOSE)

result = regex.search(data)
print(result.group(1))
print(result.group(2))

# output 
# Tom
# 010-1234-5678
```

### 그루핑 재참조
그룹된 부분을 /1 /2 등을 사용하여 재참조 할 수 있습니다.
```python
import re

data = "hello world world hello"

regex = re.compile(r"""
(\w+)          # 단어 반복
\s             # 공백
\1             # 1번 그룹을 재참조
""", re.VERBOSE)

result = regex.search(data)
print(result.group(1))
```

### 그룹에 이름 부여하기
(?P<그룹명>...) 를 사용하여 그룹에 이름을 부여할 수 있습니다.
```python
import re

data = "Tom 010-1234-5678"

regex = re.compile(r"""
(?P<name>\w+)\s              # 문자반복, 공백
(?P<phone>\d+[-]\d+[-]\d+)   # 숫자반복-숫자반복-숫자반복
""", re.VERBOSE)

result = regex.search(data)
print(result.group("name"))
print(result.group("phone"))

# output 
# Tom
# 010-1234-5678
```

### 긍정형 전방 탐색
<p>
http://127:0.0.1 라는 문자열에서 http:를 탐색하되, :는 제외하는 예제입니다.<br>
(?=...) 를 사용하여 탐색합니다.
</p>

```python
import re

data = "http://127.0.0.1"
regex = re.compile(".+(?=:)")
result = regex.search(data)
print(result.group())

# output
# http
```

### 부정형 전방 탐색

```python
import re

data = """
example.py
test.txt
myjava.java
mycsharp.cs
mycplusplus.cpp
"""

# .cpp로 끝나는 파일을 제외한 파일만 추출
import re

data = """
example.py
test.txt
myjava.java
mycsharp.cs
mycplusplus.cpp
"""

# .cpp로 끝나는 파일을 제외한 파일만 추출
regex = re.compile("""
^[a-z]+                 # 소문자로 된 문자 반복
[.]                     # .을 꼭 포함([]안에 넣지 않으면 어떤문자든 인식하는기호)
(?!cpp$)                # cpp를 탐색하지 않는다.
[a-z]+$                 # 소문자로 된 문자가 반복되어 끝
""", re.MULTILINE|re.VERBOSE)
result = regex.findall(data)
print(result)

# output
# ['example.py', 'test.txt', 'myjava.java', 'mycsharp.cs']
```

### 문자열 바꾸기
sub 메서드를 사용하여 매치되는 부분을 다른 문자로 변경(\g로 그루핑된부분 참조)
```py
import re

data = """
750101-1010101
800101-2020202
"""

# 주민등록번호 뒷자리 가리기
regex = re.compile("""
([0-9]{6})      # 숫자 6번반복된 부분을 찾고 그루핑
[-]             # - 기호 포함
[0-9]{7}        # 숫자 7자리 반복
""")
result = regex.sub("\g<1>-*******",data)
print(result)

# output
# 750101-*******
# 800101-*******
```


### Greedy vs Non-Greedy
```py
import re

data = "<tr><td>a</td><td>b</td><tr>"

# tr 태그 뽑기
regex = re.compile('<.*>')
result = regex.match(data)
print(result.group())
# *은 greedy한 특성때문에 마지막에 있는 tr까지 찾아버립니다.


# Non-Greedy
regex = re.compile('<.*?>')
result = regex.match(data)
print(result.group())
# non-greedy한 문자인 ?를 이용하여 *의 탐욕을 제거합니다.
```