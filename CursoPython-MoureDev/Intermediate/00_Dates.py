### Dates ###

from datetime import datetime, time, date

now = datetime.now()

def imprimir_fecha(now):
    print(now.year)
    print(now.month)
    print(now.day)
    print(now.hour)
    print(now.minute)
    print(now.second)
    print(now.microsecond)
    timestamp = now.timestamp()
    print(timestamp)


imprimir_fecha(now)


año_2023 = datetime(2023, 1, 1)

print(año_2023 - now)


imprimir_fecha(año_2023)


tiempo = time(23, 12, 23)

print(tiempo.hour)

fecha = date(2024, 2, 2)

print(fecha.day)

año = date.year 

print(fecha.year)