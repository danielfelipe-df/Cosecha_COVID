import re
import math

#Esta función me da el peso del vínculo
def ZipfGravity(k,pop1,pop2,distance):
    return k*pop1*pop2/distance

#Esta función me convierte a grados las latitudes y longitudes
def todegree(latorlong):
    deg, minutes, seconds, direction = re.split('[°\'"]', latorlong)
    degree = (float(deg) + float(minutes)/60 + float(seconds)/3600)*(-1 if direction in ['W', 'S'] else 1)
    return degree

#Esta función me da la distancia entre los dos puntos
def coordinatetodistance(lat1,long1,lat2,long2):
    #Convierto los grados a radianes
    lat1 = math.radians(lat1)
    lat2 = math.radians(lat2)
    long1 = math.radians(long1)
    long2 = math.radians(long2)

    #Hallo las diferencias entre las posiciones
    dlon = long2-long1
    dlat = lat2-lat1

    #Hallo un cateto y el ángulo que forman ambos lugares con respecto al centro
    a = math.sin(dlat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dlon/2)**2
    c = 2*math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    #Defino el radio de la Tierra y hallo el arco
    R = 6371.0
    return R*c
