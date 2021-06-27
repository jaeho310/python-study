# stringprep

```
파이썬의 내부 문자는 내부적으로 유니코드, 코드포인트로 저장됩니다.
stringprep은 RFC 3454에 정의된 유니코드 문자를 식별하는데 사용됩니다.
```

```py
# 유니코드 확인
data = '\u0061' 
print(data)
# output : a
```

```python
import stringprep
a = '\u0020'
print(a) # 빈 공간


print("##################################")

b = '\u06DD'
print(b) # 비 아스키 제어 문자 (ARABIC END OF AYAH)

print("###################################")


# 아스키 공백문자 안에 \u0020가 있는지 확인
print(stringprep.in_table_c11(a))
# ouput : true

# 아스키 제어문자에 b가 있는지 확인
print(stringprep.in_table_c22(b))
# ouput : true
```

