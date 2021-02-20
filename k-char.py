'''На вход программе подается натуральное число n и n строк, а затем число k. 
Напишите программу, которая выводит k-ую букву из введенных 
строк на одной строке без пробелов.'''

n = int(input())
list_string = []
list1 = []
str0 = ''
str1 = ''
str2 = ''

for i in range(n):
    str0 = input()
    list_string.append(str0)

k = int(input())

for j in range(len(list_string)):
    str1 = list_string[j]
    if len(str1) >= k:
        str2 += str1[k - 1]
    else:
        continue

print(str2)