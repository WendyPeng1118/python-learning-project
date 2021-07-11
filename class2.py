"""
Created on Sat Jun 19 19:31:16 2021

@author: windypeng
"""

"""
命名
第一個字元：英文、底線、中文
不能包含空白
變數：小駝峰式 (lower camel case)、lower snake case
常數：upper snake case
"""

"""
＝ 指定運算子
變數 ＝ 運算後結果
左邊只能是變數，不能是運算式
"""
x = 5
print(x)

x = 5 * 6
print(x)

y = x + 5
print(y)

x = y = z = 3
print(x, y, z)

x, y, z = 2, 5.8, "Hello"
print(x, y, z)

"""
input 輸入的內容讀取預設為字串
eval 數值（若為整數則轉為整數，為浮點數則轉為浮點數）

"""
x = input("請輸入成績：")
print(x, type(x))

score = int(input("請輸入成績："))
print(score, type(score))

"""
print(value,..., sep = " ", end = "\n", file = sys.tdout)
sep, end, file 皆為選擇性參數，沒特別定義則為預設
file 設定輸出的裝置，預設為螢幕
"""
print(x, y, z, sep = "/")
print(x, y, z, end = "_")
print("Wendy")
