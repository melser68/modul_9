def factorial_n(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial_n(n-1)

def factorial_k(k):
    if k == 1 or k == 0:
        return 1
    else:
        return k * factorial_k(k-1)


def factorial_n_k(inp):
    if inp == 1 or inp == 0:
        return 1
    else:
        return inp * factorial_k(inp-1)


def number_of_groups(n, k):
    fact_n = factorial_n(n)
    fact_k = factorial_k(k)
    fact_n_k = factorial_n_k(n-k)
    variants = fact_n / (fact_n_k * fact_k)
    return int(variants)
    
    
    

print(number_of_groups(50,7))   


