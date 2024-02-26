def numeroConsec(*args):
    anterior = 999999999999
    for arg in args:
        if arg == anterior:
            return True
        else:
            anterior = arg
    return False


print(numeroConsec(3,2,5,3,2,1,1))
