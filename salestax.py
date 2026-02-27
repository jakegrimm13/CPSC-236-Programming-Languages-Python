taxrate = 0.06

def calctax(total):
    tax = total * taxrate
    return round(tax, 2)

def calcaftertax(total):
    totafter = total + calctax(total)
    return round(totafter, 2)