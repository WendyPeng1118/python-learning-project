import math

coordinateAX = eval(input('輸入 A 點的 X 座標: '))
coordinateAY = eval(input('輸入 A 點的 Y 座標: '))
coordinateBX = eval(input('輸入 B 點的 X 座標: '))
coordinateBY = eval(input('輸入 B 點的 Y 座標: '))

distance = math.sqrt(
  (coordinateAX - coordinateBX) ** 2 + (coordinateAY - coordinateBY) ** 2
)

resultA = 'A 點座標為 ({}, {})\t'.format(coordinateAX, coordinateAY)
resultB = 'B 點座標為 ({}, {})\t'.format(coordinateBX, coordinateBY)
resultDistance = '兩點距離為 {:.4f}'.format(distance)

print(resultA, resultB, resultDistance)
