# int() 參數轉型後不得為浮點數
# int(只能是整數)
height = float(input("請輸入身高(cm): ")) / 100
weight = float(input("請輸入體重(kg): "))
bmi = weight / (height ** 2)
result = round(bmi, 2)

print('您的 BMI 為: ', result)
