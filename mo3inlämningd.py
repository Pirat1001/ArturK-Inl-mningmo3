# Skatt uppgift

bruttoInkomst = int(input("Ange ditt bruttolön i hela kronor: "))

def värnskatt(a):
    return round(a*0.05)

def årslön(a):
    return round(a*12)

def kommunalskatt(a):
    return round(a*0.2136)

def landstingss(a):
    return round(a*0.1148)

def statligskatt(a):
    return round(a*0.2)

if årslön(bruttoInkomst) > 675700:
    nettoinkomst = bruttoInkomst - (kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst) + statligskatt(bruttoInkomst) + värnskatt(bruttoInkomst))
    totalskattandel = 5.0 + 20.0 + 11.48 + 21.36
    totalskatt = kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst) + statligskatt(bruttoInkomst) + värnskatt(bruttoInkomst)
    print(""" Din brutton inkomst: {} kr (Årslön: {} kr)
     Kommunal skatt: {} kr 
     Landstingsskatt: {} kr 
     Statligskatt: {} kr
     Värnskatt: {} kr
     Andel betalad skatt: {} %
     Total skatt: {} kr 
     Nettoinkomst: {} kr""".format(bruttoInkomst, årslön(bruttoInkomst), kommunalskatt(bruttoInkomst), landstingss(bruttoInkomst), statligskatt(bruttoInkomst), värnskatt(bruttoInkomst), totalskattandel, totalskatt, nettoinkomst))

elif årslön(bruttoInkomst) > 468700:
    netto = bruttoInkomst - (kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst) + statligskatt(bruttoInkomst))
    skattandel = 20.0 + 21.36 + 11.48
    Totalsk = kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst) + statligskatt(bruttoInkomst)
    print(""" Din brutton inkomst: {} kr (Årslön: {} kr)
     Kommunal skatt: {} kr 
     Landstingsskatt: {} kr 
     Statligskatt: {} kr 
     Andel betalad skatt: {}%
     Total skatt: {} kr 
     Nettoinkomst: {} kr""".format(bruttoInkomst, årslön(bruttoInkomst), kommunalskatt(bruttoInkomst), landstingss(bruttoInkomst), statligskatt(bruttoInkomst), skattandel, Totalsk, netto))

elif årslön(bruttoInkomst) > 19247:
    nettoinkomst = bruttoInkomst - (kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst))
    skattand = 21.36 + 11.48
    Totalskatten = kommunalskatt(bruttoInkomst) + landstingss(bruttoInkomst)
    print(""" Din brutton inkomst: {} kr (Årslön: {} kr)
     Kommunal skatt: {} kr 
     Landstingsskatt: {} kr 
     Total skatt {} kr 
     Andel betalad skatt: {}%
     Nettoinkomst: {} kr""".format(bruttoInkomst, årslön(bruttoInkomst), kommunalskatt(bruttoInkomst), landstingss(bruttoInkomst),Totalskatten, skattand, nettoinkomst))

else:  
    print(""" Din bruttoinkomst: {} kr (årsinkomst: {})
     Nettoinkomst: {} kr 
     Eftersom du tjänar under brytpunkten dras ingen skatt""".format(bruttoInkomst, årslön(bruttoInkomst), bruttoInkomst))
