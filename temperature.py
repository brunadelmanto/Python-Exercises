
t = eval(input('Digite a temperatura atual:'))

def temperature(t):
    if t > 32 and t < 86:
        print("Cold!")
    elif t > 86:
        print("Hot!")
    else:
        print("Freezing!")

temperature(t)