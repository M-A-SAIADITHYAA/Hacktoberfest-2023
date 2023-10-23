
def pascaltriangle(X):
    prev = 1
    print(prev, end=' ')
    for i in range(1,X+1):
        curr = (prev * (X - i + 1)) // i
        print( curr, end = ' ')
        prev = curr
X = int(input("enter the row"))
pascaltriangle(X)