def myfunc(a):
    b=""
    for letter in range(len(a)):
        if letter % 2 ==0:
            b = b + a[letter].lower()
        else:
            b = b + a[letter].upper()
    return b

myfunc("Supercalifragilisticexpialidocious")	