#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X




n = int(input())
a = map(int, input().split())
x = int(input())

closest = x + 2001
mindiff = 2001

for el in a:
	if abs(x - el) <= mindiff:
		if abs(x - el) == mindiff:
			closest = min(closest, el)
		else:
			closest = el			
			mindiff = abs(x - el)

print(closest)