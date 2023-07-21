N=int(input())
def printed(N):
    if (N==1):
        print( 1,end=" ")
        return 0
    printed(N-1)
    print(N,end=" ")
printed(N)
