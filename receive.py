import machine
import time

rx = machine.ADC(0)

threshold = 768
binstr = ""

count = 10

while count > 0:
    
    time.sleep(0.25)
    
    analog = rx.read()
    
    if analog < threshold:
        binstr += "0"
    elif analog > threshold:
        binstr += "1"
        
    time.sleep(0.25)

    count -= 1


def predict(bindata):

    bindata = bindata.lstrip("0")
    bindata = bindata[0:10]
    p1 = int(bindata, 2)
    
    return p1


print(predict(binstr))






