# struct

## struct의 기능
- struct모듈내 pack, unpack 등의 메서드를 이용하여 byte객체로 변환하는데 사용됩니다.
- format을 지정하여 지정된 타입으로 변환합니다.

## pack, unpack example
```python
import struct
 
# iii 는 int형 세자리를 사용한다는 format이입니다.
# 1byte는 8bit(11111111) 이므로 1byte는 최대 255(11111111 = 0xff)까지 표현가능합니다.
var = struct.pack('iiiii', 15, 16, 17,255,256)
print(var)
# output b'\x0f\x00\x00\x00\x10\x00\x00\x00\x11\x00\x00\x00\xff\x00\x00\x00\x00\x01\x00\x00'
 
# unpack시 
upvar = struct.unpack('iiiii', var)
print(upvar)
print(type(upvar))
# output <class 'tuple'>

# byte 사이즈 확인
size = struct.calcsize('iiiii')
print(size)
# output 20
```

## struct를 사용하는 이유
- 실제로 byte데이터를 읽어와야 할때 사용합니다.
- tcp 통신 같은곳에서는 실제로 byte 배열을 사용합니다.(모듈이 갖춰져있어도 내부적으로는 byte[]형식을 주고받습니다)
- c언어같은 곳에서는 byte단위로 파일을 저장합니다.(파이썬에서 직접 pack 하여 저장하는것과 같은 원리입니다.)
- c언어로 struct를 저장하여 binary파일을 만들어 file을 읽는 예제입니다.


```c
#include <stdio.h>
typedef struct { 
    double v; // 8byte
    int t;  // 4byte
    char c; // 1byte
} save_type;

int main() {
    // 8 + 4 + 1 = 13 이지만 구조체는 4byte씩 공간을 확보하므로 13 -> 16byte로 저장된다.
    save_type s = {7.5f, 15, 'A'};

    FILE *f = fopen("output", "w");
    fwrite(&s, sizeof(save_type), 1, f);
    fclose(f);
    return 0;
}
```
```python
# binary로 저장된 파일을 python에서 읽습니다.
import struct
with open('output', 'rb') as f:
    # 8 + 4 + 1 = 13 이지만 구조체는 4바이트씩 공간을 확보하므로 16바이트를 읽어야한다.
    chunk = f.read(16)
    result = struct.unpack('dicccc', chunk)
    print(result)

# 뒤에 3자리는 패딩값
# output (7.5, 15, b'A', b'V', b'\x00', b'\x00')
```

## txt파일과 binary파일의 차이점
### UNICODE
- 유니코드는 인코딩방식이 아니라 모든 문자를 2bytes의 숫자로 매핑시키는 방식입니다.
- 컴퓨터상에서 우리눈에 보이는 모든 문자,특수기호들은 모두 UNICODE에 매핑되어있습니다.
- 유니코드 여러가지로 표현하는 인코딩 방식이 존재합니다.(ASCII, UTF-8 등)

### 대표적인 문자 인코딩 종류
- ASCII
    - 7bit를 사용하여 영어,숫자,특수문자를 표현(2**7이므로 128까지)
    - A는 American의 약자로 영어를 위해 만들어진 문자이다.
- ANSI
    - 8bit로 구성되어 256개의 문자를 표현
    - ANSI = ASCII + CodePage(1bit)
- UTF-8(Universal Coded Character Set + Transformation Format – 8-bit)
    - 유니코드를 위한 가변 길이 문자 인코딩(한글은 3byte 영어는 1byte)
    - ANSI의 단점을 보완한 방식

### txt 파일이란?
- 유니코드가 1~3 byte의 UTF-8 방식으로 인코딩되어 저장되는 파일(사람이 읽을수 있다)
- ASCII코드로 인코딩이 가능한경우에는 ASCII 코드로만 인코딩된다.

### 확인방법
```
file -i test.txt
xxd test.txt
txt파일로 저장되면 ascii utf등으로 저장된다.(charset은 ASCII로 저장이 가능하면 ASCII로 필요에따라 UTF-8로 자동변환)

output2 에는 {1,'A'}를 struct로 저장
output3 에는 {'A'}을 struct로 저장

1byte는 8bit
10진수로 0~256
2진수로 0 ~ 1111 1111
16진수로 0 ~ 0xFF
```



