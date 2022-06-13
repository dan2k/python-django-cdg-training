numbers = [-1, 2, 5, 8, 10, 13]
names = ['Mateo', 'Danny', 'James', 'Thomas', 'Luke']
mixed_type = [-2, 5, 84.2, "Mountain", "Python"]
print(numbers)
print(numbers[3])
print(names[3])
print(mixed_type[0])

print(numbers[-1])
print(names[-2])


number2=[] #empty list
# เพิ่ม list
number2.append(5)
number2.append(10)
number2.append(15)
number2.append(20)
print(number2)

sum = 0
for n in numbers:
    print(n, end=' ')
    sum += n
print('sum = ', sum)

# index,value
for i,v in enumerate(numbers):
    print(i,v)
    

for i in range(0, len(names)):
    print(names[i].upper(), end=' ')
