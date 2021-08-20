li = []
while True:
    temp = input()
    if li == "\n":
        break
    else:
        li.append(temp)

odd = []
even = []

for i in range(0, len(li)):
    if i % 2 == 0:
        even.append(li[i])
    else:
        odd.append(li[i])

for e in even:
    print(e)
for e in odd:
    print(e)
