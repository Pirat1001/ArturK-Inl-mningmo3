# Skatt uppgift

# Ställer en fråga till användaren om hur mycket hen tjänar i brutto(innan skattavdrag)
bruttoInkomst = int(input("Ange ditt bruttolön i hela kronor: "))

# Skapar funktioner som använder på flera olika sätt den inmatade värden t.ex. att räkna ut årlön, värnsskatt etc, de olika float värden motsvarar procentuella andel för skatten 
def värnskatt(a):
    return round(a*0.02)

def årslön(a):
    return round(a*12)

def kommunalskatt(a):
    return round(a*0.2136)

def landstingss(a):
    return round(a*0.1148)

def statligskatt(a):
    return round(a*0.2)

# Skapar en if sats där jag börjar med den största värden för att ha en ordning på vad programmed ska kontrollera först, ifall funktionen årslön av bruttolön är större än 675700 händer följande:
if årslön(bruttoInkomst) > 675700:
    # Ifall påståendet är sant finns en formel för nettoinkomsten där alla olika skatter finns
    nettoinkomst = bruttoInkomst - (kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst) + statligskatt(bruttoInkomst) + värnskatt(bruttoInkomst))
    # Utskriften ifall påståenden är sant, där de olika skatten skrivs ut(avrundat) samt nettolön och bruttolön
    print(""" Din brutton inkomst: {} kr (Årslön: {} kr)
     Kommunal skatt: {} kr 
     Landstingsskatt: {} kr 
     Statligskatt: {} kr
     Värnskatt: {} kr
     Nettoinkomst: {} kr""".format(bruttoInkomst, årslön(bruttoInkomst), kommunalskatt(bruttoInkomst), landstingss(bruttoInkomst), statligskatt(bruttoInkomst), värnskatt(bruttoInkomst),nettoinkomst))

# Ifall påsåenden innan inte är sant kontrollerar den ifall funktionen årslön av bruttoinkomst är större än 468700 kommer följande att hända:
elif årslön(bruttoInkomst) > 468700:

    netto = bruttoInkomst - (kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst) + statligskatt(bruttoInkomst))
    print(""" Din brutton inkomst: {} kr (Årslön: {} kr)
     Kommunal skatt: {} kr 
     Landstingsskatt: {} kr 
     Statligskatt: {} kr 
     Nettoinkomst: {} kr""".format(bruttoInkomst, årslön(bruttoInkomst), kommunalskatt(bruttoInkomst), landstingss(bruttoInkomst), statligskatt(bruttoInkomst), netto))
# -:-
elif årslön(bruttoInkomst) > 19247:
    nettoinkomst = bruttoInkomst - (kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst))
    print(""" Din brutton inkomst: {} kr (Årslön: {} kr)
     Kommunal skatt: {} kr 
     Landstingsskatt: {} kr 
     Nettoinkomst: {} kr""".format(bruttoInkomst, årslön(bruttoInkomst), kommunalskatt(bruttoInkomst), landstingss(bruttoInkomst), nettoinkomst))

else:  
    print(""" Din bruttoinkomst: {} kr (årsinkomst: {})
     Nettoinkomst: {} kr 
     Eftersom du tjänar under brytpunkten dras ingen skatt""".format(bruttoInkomst, årslön(bruttoInkomst), bruttoInkomst))
