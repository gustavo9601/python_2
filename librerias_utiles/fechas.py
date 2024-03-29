# libreria de tiempo
import datetime
# o from datetime import datetime

# trae la hora universal
hoy_utc = datetime.datetime.utcnow()
print("hoy_utc", hoy_utc)

hoy = datetime.datetime.now()
print("hoy", hoy)

fecha1 = datetime.date(2020, 1, 20)
print("fecha1.fecha1", fecha1)
print("fecha1.fecha1.day", fecha1.day)
print("fecha1.fecha1.month", fecha1.month)
print("fecha1.fecha1.year", fecha1.year)
print("fecha1.fecha1.weekday()", fecha1.weekday())
print("fecha1.fecha1.isoweekday()", fecha1.isoweekday())

fecha2 = datetime.datetime(2020, 6, 3, 18, 50, 42)
print("fecha2", fecha2)

resta_1_dia = hoy - datetime.timedelta(days=1)
print("resta_1_dia", resta_1_dia)

# Formateo de fechas de datetime a string
print("fecha2.strftime('%Y-%m-%d')", fecha2.strftime('%Y-%m-%d'))
print("fecha2.strftime('%Y/%m/%d %H:%M:%S')", fecha2.strftime('%Y/%m/%d %H:%M:%S'))

# Fromateo de fechas de string a datetime
fecha3 = datetime.datetime.strptime('2020-06-01', '%Y-%m-%d')
print("fecha3", fecha3)


# Libreria que permite ver las zonas horarias del mundio
# pip3 install pytz
import pytz

print("Todas las zonas horarias", pytz.all_timezones)
hora_spain = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
hora_bogota = datetime.datetime.now(pytz.timezone('America/Bogota'))
print("hora_spain", hora_spain)
print("hora_bogota", hora_bogota)