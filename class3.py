# import 寫在一份檔案的最前面
import math

"""
算術運算子
// 整數商 （ / 的結果為浮點數）
％ 求餘數
** 指數
"""
print(8 / 5)
print(8 // 5)
# 無限小數有上限
print(1 / 3)
print(1 // 3)
print(8 % 5)
print(2 ** 3)

"""
比較運算子
==
!= 不等於
>=
<=
"""
x = (8 == 8)
print(x)

"""
邏輯運算子
and, or, not
"""
x = 8 > 3 and 6 > 9
print(x)

x = not 8 > 3
print(x)

"""
指派運算子
(算術運算子)=
口訣：13124
"""
x = 5
# x = x + 5
x += 5
print(x)

x /= 2
print(x)

# 若浮點數求整數商，結果仍為浮點數
x = 5.0
x //= 2
print(x)

x = 5
x //= 2
print(x)

"""
python 內建函數與引入模組(import)
"""
print(round(3.14159, 3))
# 不會出現 1.200
print(round(1.2, 3))
print(math.ceil(3.14159))
