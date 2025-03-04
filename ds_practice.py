from collections import deque
bicycles = ['trek', 'cannon', 'redline', 'specialized']
print(bicycles)
print(bicycles[-1])
bicycles.insert(10,'ducati')
del bicycles[1]
print(bicycles)
print(bicycles.pop())
bicycles.append('ducate')
# print(bicycles.peek())

bicycles.append('s1')
bicycles.append('rt')
q = deque()

bicycles.sort()
bicycles.append("apple")
bicycles.append("tesla")
# print(bicycles)
sortedBikes = sorted(bicycles)
print(bicycles)
print(sortedBikes)
print(len(bicycles))

#  looping
for bike in bicycles:
    print(f'{bike.title()}, best bike Ever!')

print('End For')

numlist = list(range(7))
print(numlist)
print(range(7))

numlist = [i**2 for i in range(2, 11, 3)]
print(numlist)
print(min(numlist))
print(max(numlist))
print(sum(numlist))
print(numlist[0:2])

numlist_copy = numlist[:]
numlist_copy.append(98)
print(numlist_copy)
print(numlist)