import re


def condition_normalization(c):
    match c:
        case "Nové s visačkou":
            return 1
        case "Nové bez visačky":
            return 2
        case "Veľmi dobré":
            return 3
        case "Dobré":
            return 4
        case "Uspokojivé":
            return 5

def time_normalization(t):
    match t:
        case "Práve teraz":
            return 0
        case "pred hodinou":
            return 60
        case "pred dňom":
            return 1440
        case "pred týždňom":
            return 1440*7
        case "pred mesiacom":
            return 1440*30
        case _ if re.fullmatch(r'pred .+ hodinami', t):
            return (int(t.split(" ")[1])*60)
        case _ if re.fullmatch(r'pred .+ dňami', t):
            return ((int(t.split(" ")[1])*24)*60)
        case _ if re.fullmatch(r'pred .+ týždňami', t):
            return (((int(t.split(" ")[1])*7)*24)*60)
        case _ if re.fullmatch(r'pred .+ mesiacmi', t):
            return (((int(t.split(" ")[1])*30)*24)*60)
        case _:
            return None

def price_normalization(p):
    return float(str(p).replace(",", "."))

