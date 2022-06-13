from turtle import Turtle


a = 3
b = 4.95
c = "Python programming"
print(a)
print(b)
print(c)
print(a, b, c)


x = y = z = 10
print(x,y,z)

j,k,m=5,10,15
print(j,k,m)

#Boolean
status=True
mag=False

print(status,mag)
print(True==1)

# การแสดงตัวแปรร่วมกับข้อความ
# ทำได้ 3 วิธี
# วิธีที่ 1 concat string

a=3
b=4.951
c="sangtong"
print(a,b,c)
print(a,"{:.2f}".format(b),c)

# วิธีที่ 2 ใช้ interpolation string
print("%d %.2f %s" %(a,b,c))

# วิธี 3 ใช้ format string
print(f"xxxxxxx {a} yyyyyyy{b} zzzzzzz {c} ")
print(f"xxxxxxx {a} yyyyyyy{b:.2f} zzzzzzz {c} ")
s=f"xxxxxxx {a} yyyyyyy{b:.2f} zzzzzzz {c} "
print(s)