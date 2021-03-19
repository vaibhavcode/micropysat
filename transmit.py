  
import machine
import time
import dht

sensor = dht.DHT11(machine.Pin(4))
tx = machine.Pin(15, machine.Pin.OUT)


def measuretemp():
    
    time.sleep(0.25)
    sensor.measure()
    time.sleep(0.25)
    temp = sensor.temperature()
    time.sleep(0.25)

    data = int(temp)
    return data


def transmit(data):

    txbin = bin(data).replace("0b", "")
    txbin = str(txbin)
    txbinarr = []

    for i in txbin:
        i = int(i)
        txbinarr.append(i)
    
    tx.value(0)
    time.sleep(0.5)

    for i in txbinarr:
        tx.value(i)
        time.sleep(0.5)
    
    tx.value(0)
    time.sleep(0.5)


pack = measuretemp()
transmit(pack)







