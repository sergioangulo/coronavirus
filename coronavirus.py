import math
from datetime import datetime, timedelta


def sim(rate, period, contagious_period):
    infected = (1-rate**period) /(1-rate)
    if period>contagious_period:
        released= (1-rate**(period-contagious_period))/(1-rate)
    else:
        released=0
    return int(infected-released)

def suma(lista):
    monto=0
    for valor in lista:
        monto += valor
    return monto

def test_infected():
    rate = 1.3
    period = 53
    contagious_period = 14
    first_date=datetime(2020, 3, 3, 0, 0, 00, 00000)
    maxima_capacidad=1000
    porcentaje_enfermos_graves=0.7
    pacientes_sin_atender=[]
    print( "\nPara  una tasa de", rate, "y dada una permanencia de", contagious_period,"Se estima"
            "que se tendran", sim(rate,period,contagious_period), "casos de coronavirus al dia", period,".","\nSi se tiene en cuenta que se tiene una maxima capacidad hospitalaria de 1000 camas")
    for i in range(period):
        if(i>0):
            total=sim(rate,i,contagious_period)
            ocupa_cama=int(total*porcentaje_enfermos_graves)
            nuevos_ocupan_cama=ocupa_cama-total
            if len(pacientes_sin_atender) >3:
                print("    mueren:", pacientes_sin_atender.pop(0))
            print("day",i,first_date.strftime('%d/%m :') ,sim(rate,i,contagious_period),"infectados. De estos,", ocupa_cama, "ocupan cama")
            if(ocupa_cama>maxima_capacidad):
                suma(pacientes_sin_atender)
                pacientes_sin_atender.append(ocupa_cama-maxima_capacidad)
                print("    Existen", ocupa_cama-maxima_capacidad, "pacientes sin cama.")
            first_date= first_date+timedelta(days=1)
