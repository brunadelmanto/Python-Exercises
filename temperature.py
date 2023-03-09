
t = eval(input('Enter the current temperature:'))

def temperature(t):
    if t > 32 and t < 86:
        print("Cold!")
    elif t > 86:
        print("Hot!")
    else:
        print("Freezing!")

temperature(t)