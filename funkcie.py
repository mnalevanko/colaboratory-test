def pozdrav(meno="Michal Nalevanko"):
    return 'Ahoj, {}'.format(meno)

def sucet(a, b):
    return a + b

def sucin(a, b):
    return a * b

def podiel(a, b):
    try:
        return a / b
    except:
        return None
