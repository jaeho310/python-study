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

### 위치 관련
기호 | 설명
---|---
^|시작부분에서 검사
$|문자열의 끝과 일치
\b|단어경계와 일치
\B|단어 비경계 일치

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


### DOTALL
```python
# DOTALL 예제
import re
regex1 =  re.compile('a.b')
result1 = regex1.match('a\nb')

regex2 = re.compile('a.b', re.DOTALL)
result2 = regex2.match('a\nb')
```
여러줄로 이루어진 문자열에서 \n에 상관없이 검색이 가능합니다.


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
주석을 달기 위해 사용됩니다.
[]외부에 들어간 주석, whitespace는 모두 제거됩니다.

