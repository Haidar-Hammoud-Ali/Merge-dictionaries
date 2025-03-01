def merge_dict1 (dect1, dect2):
    return (dect1|dect2)

def merge_dict2 (Dect1,Dect2):
    return ({**Dect1,**Dect2})

Positiv_aa={"arginin":"R", "histidine": "H", "lysine":"k",}
Negative_aa= {"aspartic-acid": "D", "glutamic-acid": "E", "histidine": "Y"}

results = merge_dict1 (Positiv_aa, Negative_aa)
print (results)

result= merge_dict2 (Positiv_aa, Negative_aa)
print (result)
