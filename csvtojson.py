import csv #att importera och arbeta med CSV filen 
import json #att importera och arbeta med json filen

#skapa en funktion (convertera CSV till Json)
def csv_till_json(csv_fil, json_fil):
    data = []
    with open(csv_fil, 'r', encoding='utf-8-sig') as csvfil:  # utf-8-sig. det är för svenska bokstäverna (å, ä och ö)
        läsare = csv.DictReader(csvfil) #den läser innehållet från csv filen.
        for rad in läsare:
            data.append(rad)
    
    with open(json_fil, 'w', encoding='utf-8') as jsonfil:  # det är för svenska bokstäverna (å, ä och ö)
        json.dump(data, jsonfil, indent=4, ensure_ascii=False)  
#skapa if-sats
if __name__ == "__main__":
    csv_fil = "profiles1.csv"
    json_fil = "data.json"
    csv_till_json(csv_fil, json_fil) #printa resultat. 
