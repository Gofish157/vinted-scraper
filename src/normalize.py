import re

ALPHA_RE = re.compile(r"^(XXXS|XXS|XS|S|M|L|XL|XXL|XXXL)$", re.I)
WAIST_RE = re.compile(r"^W\s*(\d{2})$", re.I)
EU_RE = re.compile(r"^(3[4-9]|4[0-9]|5[0-4])$", re.I)

def _parce_part(s: str) -> dict:

    if s == "Univerzálna": return {"size_system": "universal"}

    m = ALPHA_RE.fullmatch(s)
    if m:
        return {"size_system": "alpha", "size_alpha": m.group(1).upper()}
    
    m = WAIST_RE.fullmatch(s)
    if m:
        return {"size_system": "waist", "size_waist": int(m.group(1))}
    
    m = EU_RE.fullmatch(s)
    if m:
        return {"size_system": "eu", "size_eu": int(m.group(1))}
    
    return {"size_system": "unknown"}


def size_normalization(raw: str) -> dict:

    out ={
        "size_system": "unkwnow",
        "size_alpha": None,
        "size_eu": None,
        "size_waist": None,
        "raw": raw
    }

    if not raw: return out

    parsed = [_parce_part(part.strip()) for part in raw.split("|")]

    if not parsed:return out

    systems = set()
    for d in parsed:
        systems.add(d.get("size_system", "unknown"))
        size_system = d["size_system"]
        out["size_system"] = size_system
        if size_system == "alpha":
            out["size_alpha"] = d["size_alpha"]
        elif size_system == "waist":
            out["size_waist"] = d["size_waist"]
        elif size_system == "eu":
            out["size_eu"] = d["size_eu"]
    
    systems.discard("unknown")
    if len(systems) > 1:
        out["size_system"] = "mixed"

    return out
    

def condition_normalization(c: str):
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

def time_normalization(t: str) -> int:
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

def price_normalization(p: str) -> float:
    return float(p.replace(",", "."))

