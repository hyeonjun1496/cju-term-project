from __futer__ import print_function                        
import RPi.GPIO as GPIO   #서브 모터 제어에 사용할 RIP.GPIO 모듈을 임포트함 
import time               #시간 함수 임포트함

def measure():
    GPIO.output(GPIO_TRIGGER, True)     #  초음파 GPIO 출력 
    time.sleep(0.0001)                  #  0.0001초 동안 초음파 측정
    GPIO.output(GPIO_TRIGGER, False)    
    start = time.time()
    
    while GPIO.input(GPIO_ECHO)==0:     #  GPIO ECHO에 대한 입력값이 측정되지 않음
        start = time.time()             
         
    while  GPIO.input(GPIO_ECHO)==1:    #   GPIO ECHO가 1(측정됨)일때 stop
        stop time.time() 
        
    elapsed = stop-start                # 초음파의 측정된 값 
    distance = (elapsed * 34300)/2      # 왕복 거리 2로 나누기(음파 속력은 340m/s)
    
    return distance 
    
def measure_average():
    distance1=measure()
    time.sleep(0.1)
    distance2=measure()
    time.sleep(0.1)
    distance3=measure()
    distance = distance1 + distance2 + distance3 # 좀더 정밀한 값을 측정하기 위해 
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


    while True
    
        distance  = measure_average()        
        print("Distance : %.1f" % distance)  
        time.sleep(1)                        
        
        if distance >=10 and distance <= 20:  //만약 거리가 10보다 크고 20 보다 작을경우
           print("angle: 1")                     //각도1을 프린트 
           p.ChangedutyCycle(3)                //듀티사이클이 3% 일경우 
        elif distance >20 and distance <= 30:   
           print("angle: 2")                      
           p.ChangedutyCycle(4)                  //듀티사이클 4%로 변경
        elif distance >30 and distance <= 40:        
          print("angle: 3")
          p.ChangedutyCycle(5)
        elif distance >40 and distance <= 50:
          print("angle: 4")
          p.ChangedutyCycle(6)
        elif distance >50 and distance <= 60:
          print("angle: 5")
          p.ChangedutyCycle(7)
        elif distance >60 and distance <= 70:
          print("angle: 6")
          p.ChangedutyCycle(8)
        elif distance >70 and distance <= 80:
          print("angle: 7")
          p.ChangedutyCycle(9)
        elif distance >80 and distance <= 90:
          print("angle: 8")
          p.ChangedutyCycle(10)
        

except keyboardinterrupt:
