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

GPIO.setup(servo,GPIO.OUT)
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)
GPIO.setup(GPIO_ECHO,GPIO.IN)

GPIO.output(GPIO_TRIGGER, False)

p=GPIO.PWM(servo, 50)
p.start(2.5)
try: 

  while True:
  
    distane = measure_average()
    print("Distance : %.1f" % distance
    time. sleep(1)
    
    if distance <=10:
    print("angle: 1")
    p. ChangeDutyCycle(2.5)
    else :
    print("angle: 5")
    p. ChangeDutyCycle(7.5)
    
except KeyboardInterrupt:
  GPIO.cleanup()
