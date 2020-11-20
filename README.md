from __futer__ import print_function
import RPi.GPIO as GPIO
import time

def measure():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER, False)
    start = time.time()
    
    while GPIO.input(GPIO_ECHO)==0:
        start = time.time()
        
    while GPIO.input(GPIO_ECHO)==1:
        stop time.time() 
        
    elapsed = stop-start
    distance = (elapsed * 34300)/2
    
    return distance
    
def measure_average():
    distance1=measure()
    time.sleep(0.1)
    distance2=measure()
    time.sleep(0.1)
    distance3=measure()
    distance = distance1 + distance2 + distance3
    distance = distance / 3
    return distance
    
GPIO_setmode(GPIO.BCM)

GPIO_TRIGGER = 23
GPIO_ECHO    = 24
servo        = 18
print("Ultrasonic Measurement")

from__future__import print_function
import time
import RPi.GPIO as GPIO

def measure() :
   GPIO.output(GPIO_TRIGGER, True)
   time.sleep(0.00001)
   GPIO.output(GPIO_TRIGGER, False)
   start = time.time()
