print('bubble_sort with flag,if the list did not need to exchange number position,then the recycle is break')
lst = [1,2,3,4,5,6,7,9,8]
length = len(lst)
count_swap = 0
count = 0
for i in range(length):
    flag = False
    for j in range(length - 1 - i):
        count += 1
        if lst[j] > lst[j+1]:
            tmp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = tmp
            count_swap += 1
            #lst[j],lst[j+1] = lst[j+1],lst[j]
    if not flag:
        break
print(lst,count_swap,count)

print('--------------------------------------------------------')

print('bubble_sort without flag,it not good method')
lst = [1,2,3,4,5,6,7,9,8]
length = len(lst)
count_swap = 0
count = 0
for i in range(length):
    for j in range(length - 1 - i):
        count += 1
        if lst[j] > lst[j+1]:
            tmp = lst[j]
            lst[j] = lst[j+1]
            lst[j+1] = tmp
            count_swap += 1
print(lst,count_swap,count)
