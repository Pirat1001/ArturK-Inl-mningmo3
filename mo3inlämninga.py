# Skatt uppgift

# Frågar användaren om hur mycket den tjänar i brutto(hela kronor)
bruttoInkomst = int(input("Ange ditt bruttolön i hela kronor: "))

#skapar en funktion som jag sedan använder sedan i utskriften för att kunna räkna ut den avrundade värden för hur mycket skatt man betalar
def kommunalskatt(a):
    return round(a*0.2136)

def landstingss(a):
    return round(a*0.1148)

# Här använder jag den inmatade värden och funktionerna för att beräkna nettolön, alltså lön efter skatten
nettoinkomst = bruttoInkomst - (kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst))

# Utskriften där jag berättar hur mycket skatt man betalar i kronor 
print(""" Din brutton inkomst: {} kr
 Kommunal skatt: {} kr 
 Landstingsskatt: {} kr 
 Nettoinkomst: {} kr""".format(bruttoInkomst, kommunalskatt(bruttoInkomst), landstingss(bruttoInkomst), nettoinkomst))