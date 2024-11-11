a = []
while True:
    c = input('Напишите элемент списка, если хотите прервать цикл, напишите "0"')
    if c == "0":
        break
    else:
        a.append(c)

print(sorted(a, reverse=True))
