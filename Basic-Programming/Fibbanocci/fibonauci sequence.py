
N = int(input("enter the number"))
def fibo_bottom_up_app(N):
    if N ==0 or N==1:
        return 1
    bottom_up = [None]*(N)
    bottom_up[0]=0
    bottom_up[1]=1
    for i in range(2,N):
        bottom_up[i] = bottom_up[i-1] + bottom_up[i-2]
    return bottom_up[0:]
result = fibo_bottom_up_app(N)
formatted_result = ' '.join(map(str, result))
print(formatted_result)
