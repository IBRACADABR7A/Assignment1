import csv 
import json

def csv_till_json(csv_fil, json_fil):
    data = []
    with open(csv_fil, 'r', encoding='utf-8-sig') as csvfil:  # Ange teckenuppsättningen utf-8-sig
        läsare = csv.DictReader(csvfil)
        for rad in läsare:
            data.append(rad)
    
    with open(json_fil, 'w', encoding='utf-8') as jsonfil:  # Ange teckenuppsättningen utf-8
        json.dump(data, jsonfil, indent=4, ensure_ascii=False)  # Ange ensure_ascii=False för att behålla icke-ASCII-tecken

if __name__ == "__main__":
    csv_fil = "profiles1.csv"
    json_fil = "data.json"
    csv_till_json(csv_fil, json_fil)
