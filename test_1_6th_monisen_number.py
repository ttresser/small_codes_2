def primalidade(n):
    j = 2
    primo = True
    if n == 0 or n == 1:
        primo = False
    else:
        while j < n and primo:
            if (n % j) == 0:
                primo = False
            j = j + 1
    return primo

def main():
    ordem = p = 0
    t = True
    while t:
        primo1 = primalidade(p)
        if primo1:
            m = (2**p) - 1
            primo2 = primalidade(m)
            if primo2:
                ordem += 1
                if ordem == 6:
                    t = False
        p += 1
    print(m)

main()
