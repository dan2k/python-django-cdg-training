def hello():
    print("Hello Python")


# เรียกใช้งานฟังค์ชั่น
hello()

# การสร้างฟังค์ชั่นแบบมี argument


def info(msg):
    print("welcom to ", msg)


info("tongdang")

# รับค่า return ค่า
def area(width, height):
    result = width*height
    return result


print(area(10, 20))

#Default Argument Values
def show_info(name="", salary = 84360, lang = "Python"):
    print('Name: %s' % name)
    print('Salary: %d' % salary)
    print('Language: %s' % lang)
    print()

# calling function
show_info()
show_info('Mateo')
show_info('Mateo', 105000)
show_info('Danny', 120000, 'Java')
