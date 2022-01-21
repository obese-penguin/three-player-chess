with open('coords.txt') as f:
    coords = f.readlines()

temp = [x.replace('\n', '') for x in coords]
data = []
for i in temp:
    for j in range(len(i)):
        if i[j] == ' ' and i[j+1] == '[':
            i = i[:j] + '|' + i[j+1:]   

    data.append(i)
final = [x.replace('[', '').replace(']', '').split(',|') for x in data] 

data = []
for i in final:
    row = []
    for j in i:
            row.append((float(j.split(', ')[0]), float(j.split(', ')[1])))
    data.append(row)

print(data[0][0])
print()
print(data)
