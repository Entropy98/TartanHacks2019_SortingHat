from playsound import playsound

def range(x):
    print(x)
    try:
        return int(x)
    except:
        return int(x.real + x.imag)

def switch(arg):
    switcher = {
        0: "griffindor",
        1: "hufflepuff",
        2: "ravenclaw",
        3: "slitherin"
    }
    return switcher.get(arg%4, "wizard harry")

def threshold(vals):
    a = sum(vals)/len(vals)
    return switch(range(a))

def place(vals):
    house = threshold(vals)
    playsound(house + ".wav")
