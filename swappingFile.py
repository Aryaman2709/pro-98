x = input()
y = input()

def swapFileData(x, y):
    with open(x, 'r') as a:
        data_a = a.read()
    with open(y, 'r') as a:
        data_b = a.read()
    with open(y, 'w') as b:
        b.write(data_a)
    with open(x, 'w') as b:
        b.write(data_b)

swapFileData(x, y)