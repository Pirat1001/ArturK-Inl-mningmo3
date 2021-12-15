# Tabell skatt

# Skapar en tuple för alla värden som finns i instruktionerna 
månadsinkomst = (1500, 5000, 10000, 15000, 20000, 25000, 30000, 35000, 40000, 45000, 50000, 55000, 60000)

# Funktionerna för de olika skatterna samt andra beräkningar som använder de olika värden i tuplen 
def årslön(a):
    return a*12

def kommunalskatt(a):
    return round(a*0.2136)

def landstingss(a):
    return round(a*0.1148)

def statligskatt(a):
    return round(a*0.2)

def värnskatt(a):
    return round(a*0.05)

# Ganska stor utskrift i form av tabell, jag använder mig av en f string eftersom då har man bättre koll på vart sakerna ligger, ifall jag skulle använda exempelvis .format skulle det vara väldigt svårt att hålla koll på ordningen
# I Utskriften använder jag mig av de olika funktionerna och specifika index i tupeln, därför får jag olika sorters värde i utskriften
print(f""" Månadsinkomst     |  Årsinkomst       |  Total skatt       |  Total skatt i %      |  Netto / mån     |  Kommunals.     |  Landstingss.     |  Statlig s.     |  Värns.    |
___________________________________________________________________________________________________________________________________________________________________________________
       {månadsinkomst[0]} kr     |   {årslön(månadsinkomst[0])} kr        |   0 kr             |   0.00 %              |   {månadsinkomst[0]} kr        |   0 kr          |   0 kr            |   0 kr          |   0 kr     |
       {månadsinkomst[1]} kr     |   {årslön(månadsinkomst[1])} kr        |   {kommunalskatt(månadsinkomst[1]) + landstingss(månadsinkomst[1])} kr          |   {21.36 + 11.48} %             |   {månadsinkomst[1] - (kommunalskatt(månadsinkomst[1]) + landstingss(månadsinkomst[1]))} kr        |   {kommunalskatt(månadsinkomst[1])} kr       |   {landstingss(månadsinkomst[1])} kr          |   0 kr          |   0 kr     | 
       {månadsinkomst[2]} kr    |   {årslön(månadsinkomst[2])} kr       |   {kommunalskatt(månadsinkomst[2]) + landstingss(månadsinkomst[2])} kr          |   {21.36 + 11.48} %             |   {månadsinkomst[2] - (kommunalskatt(månadsinkomst[2]) + landstingss(månadsinkomst[2]))} kr        |   {kommunalskatt(månadsinkomst[2])} kr       |   {landstingss(månadsinkomst[2])} kr         |   0 kr          |   0 kr     | 
       {månadsinkomst[3]} kr    |   {årslön(månadsinkomst[3])} kr       |   {kommunalskatt(månadsinkomst[3]) + landstingss(månadsinkomst[3])} kr          |   {21.36 + 11.48} %             |   {månadsinkomst[3] - (kommunalskatt(månadsinkomst[3]) + landstingss(månadsinkomst[3]))} kr       |   {kommunalskatt(månadsinkomst[3])} kr       |   {landstingss(månadsinkomst[3])} kr         |   0 kr          |   0 kr     |
       {månadsinkomst[4]} kr    |   {årslön(månadsinkomst[4])} kr       |   {kommunalskatt(månadsinkomst[4]) + landstingss(månadsinkomst[4])} kr          |   {21.36 + 11.48} %             |   {månadsinkomst[4] - (kommunalskatt(månadsinkomst[4]) + landstingss(månadsinkomst[4]))} kr       |   {kommunalskatt(månadsinkomst[4])} kr       |   {landstingss(månadsinkomst[4])} kr         |   0 kr          |   0 kr     | 
       {månadsinkomst[5]} kr    |   {årslön(månadsinkomst[5])} kr       |   {kommunalskatt(månadsinkomst[5]) + landstingss(månadsinkomst[5])} kr          |   {21.36 + 11.48} %             |   {månadsinkomst[5] - (kommunalskatt(månadsinkomst[5]) + landstingss(månadsinkomst[5]))} kr       |   {kommunalskatt(månadsinkomst[5])} kr       |   {landstingss(månadsinkomst[5])} kr         |   0 kr          |   0 kr     |
       {månadsinkomst[6]} kr    |   {årslön(månadsinkomst[6])} kr       |   {kommunalskatt(månadsinkomst[6]) + landstingss(månadsinkomst[6])} kr          |   {21.36 + 11.48} %             |   {månadsinkomst[6] - (kommunalskatt(månadsinkomst[6]) + landstingss(månadsinkomst[6]))} kr       |   {kommunalskatt(månadsinkomst[6])} kr       |   {landstingss(månadsinkomst[6])} kr         |   0 kr          |   0 kr     |
       {månadsinkomst[7]} kr    |   {årslön(månadsinkomst[7])} kr       |   {kommunalskatt(månadsinkomst[7]) + landstingss(månadsinkomst[7])} kr         |   {21.36 + 11.48} %             |   {månadsinkomst[7] - (kommunalskatt(månadsinkomst[7]) + landstingss(månadsinkomst[7]))} kr       |   {kommunalskatt(månadsinkomst[7])} kr       |   {landstingss(månadsinkomst[7])} kr         |   0 kr          |   0 kr     | 
       {månadsinkomst[8]} kr    |   {årslön(månadsinkomst[8])} kr       |   {kommunalskatt(månadsinkomst[8]) + landstingss(månadsinkomst[8]) + statligskatt(månadsinkomst[8])} kr         |   {21.36 + 11.48 + 20.00} %             |   {månadsinkomst[8] - (kommunalskatt(månadsinkomst[8]) + landstingss(månadsinkomst[8]) + statligskatt(månadsinkomst[8]))} kr       |   {kommunalskatt(månadsinkomst[8])} kr       |   {landstingss(månadsinkomst[8])} kr         |   {statligskatt(månadsinkomst[8])} kr       |   0 kr     |
       {månadsinkomst[9]} kr    |   {årslön(månadsinkomst[9])} kr       |   {kommunalskatt(månadsinkomst[9]) + landstingss(månadsinkomst[9]) + statligskatt(månadsinkomst[9])} kr         |   {21.36 + 11.48 + 20.00} %             |   {månadsinkomst[9] - (kommunalskatt(månadsinkomst[9]) + landstingss(månadsinkomst[9]) + statligskatt(månadsinkomst[9]))} kr       |   {kommunalskatt(månadsinkomst[9])} kr       |   {landstingss(månadsinkomst[9])} kr         |   {statligskatt(månadsinkomst[9])} kr       |   0 kr     |
       {månadsinkomst[10]} kr    |   {årslön(månadsinkomst[10])} kr       |   {kommunalskatt(månadsinkomst[10]) + landstingss(månadsinkomst[10]) + statligskatt(månadsinkomst[10])} kr         |   {21.36 + 11.48 + 20.00} %             |   {månadsinkomst[10] - (kommunalskatt(månadsinkomst[10]) + landstingss(månadsinkomst[10]) + statligskatt(månadsinkomst[10]))} kr       |   {kommunalskatt(månadsinkomst[10])} kr      |   {landstingss(månadsinkomst[10])} kr         |   {statligskatt(månadsinkomst[10])} kr      |   0 kr     |
       {månadsinkomst[11]} kr    |   {årslön(månadsinkomst[11])} kr       |   {kommunalskatt(månadsinkomst[11]) + landstingss(månadsinkomst[11]) + statligskatt(månadsinkomst[11])} kr         |   {21.36 + 11.48 + 20.00} %             |   {månadsinkomst[11] - (kommunalskatt(månadsinkomst[11]) + landstingss(månadsinkomst[11]) + statligskatt(månadsinkomst[11]))} kr       |   {kommunalskatt(månadsinkomst[11])} kr      |   {landstingss(månadsinkomst[11])} kr         |   {statligskatt(månadsinkomst[11])} kr      |   0 kr     |
       {månadsinkomst[12]} kr    |   {årslön(månadsinkomst[12])} kr       |   {kommunalskatt(månadsinkomst[12]) + landstingss(månadsinkomst[12]) + statligskatt(månadsinkomst[12]) + värnskatt(månadsinkomst[12])} kr         |   {21.36 + 11.48 + 20.00 + 5.00} %             |   {månadsinkomst[12] - (kommunalskatt(månadsinkomst[12]) + landstingss(månadsinkomst[12]) + statligskatt(månadsinkomst[12]) + värnskatt(månadsinkomst[12]))} kr       |   {kommunalskatt(månadsinkomst[12])} kr      |   {landstingss(månadsinkomst[12])} kr         |   {statligskatt(månadsinkomst[12])} kr      |   {värnskatt(månadsinkomst[12])} kr  |  """)