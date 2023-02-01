def fact(n):
    lst = list(range(1,n+1))
    mult = 1
    while len(lst)!=0:
        mult*=lst.pop()
    return mult

def multiply(n,m):
    i = 0
    res = 0
    for i in range(0,m):
        res += n
    return res

def multiply_lst(*numeros):
    res = 1
    if isinstance(*numeros, range):
        lst = list(*numeros)
        lst.append(max(lst)+1)
        while len(lst) != 0:
            res *= lst.pop()
        return print(res)
    else: 
        lst = list(numeros)
        while len(lst) != 0:
            res *= lst.pop()
        return print(res)

print(fact(7))
multiply_lst(range(1,7))


