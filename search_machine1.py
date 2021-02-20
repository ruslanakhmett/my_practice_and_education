'''На вход программе подается натуральное число n, затем n строк, 
затем число k — количество поисковых запросов, затем k строк — поисковые запросы. 
Напишите программу, которая выводит все введенные строки, 
в которых встречаются все поисковые запросы.'''

list1, list2, list3 = [], [], []
s = ''

n = int(input())
for i in range(n):
    s = input()
    list1.append(s)

k = int(input())

for i in range(k):
    list2.append(input())

for i in range(len(list1)):
    p = 0
    for j in range(len(list2)):
        if list2[j].lower() in list1[i].lower():
            p += 1
    if p == k:
        list3.append(list1[i])            
            
print(*list3, sep = '\n')  