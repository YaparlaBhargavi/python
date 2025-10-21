numbers=[5,2,1,1,7,4]
numbers.append(20)
numbers.insert(0,43)
numbers.remove(5)
#numbers.clear()
numbers.pop()
# print(numbers.index(50)) we get an error becoz there is no 50 in list
print(numbers)
print(50 in numbers)
print(numbers.count(1)) #repeated
numbers.sort() #ascending order
numbers.reverse()
numbers2=numbers.copy()
numbers.append(10)
print(numbers2)
print(numbers)