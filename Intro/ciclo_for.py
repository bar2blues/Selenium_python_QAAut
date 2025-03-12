'''
for x in range(10):
    print("fede " + str(x +1))

colores =["rojo", "azul", "amarillo", "verde"]

for x in colores:
    print(x)
'''

for num in range(10, 30, 5):
    print(num)

for num in range(0, 100, 7):
    if (num >= 75):
        break
    print(num)

for num in range(10):
    if (num == 3 or num == 6 or num ==9):
        continue
    print(num)