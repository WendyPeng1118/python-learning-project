# score = int(input("你的成績:"))

# if score >= 95:
#   print("去歐洲")
# elif score >= 80:
#   print("去日本")
# elif score >= 70:
#   print("在台灣")
# else:
#   print("都不去")

# sex = input("性別 (M / F):")
# height = eval(input("身高 (cm):"))
# weight = eval(input("體重 (kg):"))
# bmi = weight / (height / 100) ** 2

# if sex == "M":
#   if bmi > 25:
#     print("過重")
#   elif bmi < 20:
#     print("過輕")
#   else:
#     print("適中")
# else:
#   if bmi > 22:
#     print("過重")
#   elif bmi < 18:
#     print("過輕")
#   else:
#     print("適中")

# numberA = int(input("第一個整數: "))
# numberB = int(input("第二個整數: "))
# operator = input("請輸入運算子: ")

# if operator == "*":
#   result = numberA * numberB
#   print("{} * {} = {}".format(numberA, numberB, result))
# elif operator == "+":
#   result = numberA + numberB
#   print("{} + {} = {}".format(numberA, numberB, result))
# else:
#   print("您的運算子不在此範圍")

# # 測試 result 變數值是否一直存在
# print("result", result)

year = int(input("請輸入西元年: "))
# if year % 4 == 0:
#   if year % 100 == 0:
#     if year % 400 == 0:
#       print("閏年")
#     else:
#       print("非閏年")
#   else:
#     print("閏年")
# else:
#   print("非閏年")

if (year % 4 != 0) or ((year % 100 == 0) and (year % 400 != 0)):
  print("非閏年")
else:
  print("閏年")
