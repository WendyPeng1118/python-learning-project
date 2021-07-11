"""
Created on Mon Jun 14 16:23:01 2021

@author: windypeng
"""

"""
x = int( input() )
print(x)
"""

"""
\n 換行
\t 空白
\\抵銷斜線功能
"""
print("c:\note\temp")
print("c:\\note\\temp")


"""
int 整數
float 浮點數
str 字串
bool 布林值
"""
print(type(5))
print(type(5.5))
print(type("5"))
print(type(True))

"""
＋串接
＊重複
字串與數值間不能直接串接獲重複，需為同類才行
"""
print("Hello! " + "Joseph.")
print("Hello!" * 3)
print(5+5)
print("5" + "5")
# TypeError: can only concatenate str (not "int") to str
# print("5" + 5)
print("5" + str(5))
print(int("5") + 5)
"""
bool(0) False，其他數字皆為 True
bool("") False，其他字串皆為 True
bool(" ") True
有算術運算子時，False=0，True=1
"""
print(bool(0) + bool(5))
print(bool("0") + bool("5"))
print(bool(""))
print(bool(" "))
print(bool(5) + 5)

"""
ord("") 字元轉成 Unicode (小寫 > 大寫 > 數字)
chr() Unicode 轉成字元
"""
print(ord('A'))
print(ord('a'))
print(ord('1'))
print(chr(57))
print(chr(90))
print(chr(122))
