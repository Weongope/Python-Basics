def myfunc(a):
    b=""
    index_count = 0
    for letter in a:
        if index_count % 2 == 0:
            b += letter.lower()
        else:
            b += letter.upper()
    index_count += 1
        
    return b

myfunc("abcdefg")	