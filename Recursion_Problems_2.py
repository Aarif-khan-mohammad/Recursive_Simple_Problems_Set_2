def sum_of_first_n_natural_numbers(n):
    if n==1:
        return 1
    x = n + sum_of_first_n_natural_numbers(n-1)
    return x
print(sum_of_first_n_natural_numbers(10))

def sum_of_first_n_odd_natural_numbers(n):
    if n==1:
        return 1
    x = 2*n-1 + sum_of_first_n_odd_natural_numbers(n-1)
    return x
print(sum_of_first_n_odd_natural_numbers(10))

def sum_of_first_n_even_natural_numbers(n):
    if n==1:
        return 1
    x = 2*n + sum_of_first_n_even_natural_numbers(n-1)
    return x
print(sum_of_first_n_even_natural_numbers(10))

def factorial_of_number(n):
    if n==0:
        return 1
    x = n * factorial_of_number(n-1)
    return x
print(factorial_of_number(5))

def sum_of_square_of_first_n_natural_numbers(n):
    if n==1:
        return 1
    x = n**2 + sum_of_square_of_first_n_natural_numbers(n-1)
    return x
print(sum_of_square_of_first_n_natural_numbers(5))