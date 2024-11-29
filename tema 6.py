def factorial(n):
    return n * factorial(n-1) if n>1 else 1
if __name__ == '__main__':
    print(factorial(5))

def fibonacci(n):
    init = [0,1]
    if n==0:
        return 0
    else:
        return 1 if n==1 else fibonacci(n-1) + fibonacci(n-2)
if __name__=="__main__":
    print(fibonacci(10))

sir = "recursivitate"
def inversare_sir(sir):
    n = len(sir)
    if n > 0:
        return sir[-1] + inversare_sir(sir[: n-1])
    else:
        return ""
print(inversare_sir(sir))


def putere(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    else:
        return a * putere(a,b - 1)
print(putere(2,3))
