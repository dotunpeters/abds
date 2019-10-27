
from random import randint
from math import ceil
def generateRandom():
    location = {"agege-oshodi":randint(10, 300), 
                "ojota-ketu": randint(10, 300), 
                "bariga-ilupeju": randint(10, 300), 
                "apapa-ikeja": randint(10, 300),
                "oshodi-obalende": randint(10, 300),
                "egbeda-ojo": randint(10, 300),
                "obalende-lekki": randint(10, 300),
                "ojo-magodo": randint(10, 300),
                "mile2-oshodi":randint(10, 300),
                "magodo-ikeja":randint(10, 300)
                }
    return location

def assignRoute():
    location = generateRandom()
    busCapacity = randint(10, 50)
    sellingTicket = {}
    for key, value in location.items():
        deploy = ceil(value / busCapacity)
        sellingTicket[key] = value
        location[key] = deploy
    deploying = location
    return (deploying, sellingTicket, busCapacity)