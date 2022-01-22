import math
a = []
for i in range(24):
    b = []
    for j in range(6):
        x = round((j*50+121)*(math.cos(3.14*(i)/12 + 0.13))+400,2)
        y = round((j*50+121)*(math.sin(3.14*(i)/12 + 0.13))+400,2)
        b.append([x,y])
    a.append(b)
print(a)