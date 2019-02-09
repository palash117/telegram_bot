
def cook():
    t = int(input())
    for i in range(t):

        n, a, b, k = [int(x) for x in input().split()]
        diva = n/a
        divb = n/b
        divab= n/((a*b)/gcd(a,b))
        diva = diva- divab
        divb = divb- divab

        if (diva+divb>=k):
            print('Win')
        else:
            print('Lose')

def gcd(a, b):
    if (a%b)==0:
        return b
    return gcd(b, a%b)

# print gcd(1540,14490)
cook()