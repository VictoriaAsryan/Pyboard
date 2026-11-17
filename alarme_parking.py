from time import sleep, ticks_ms, ticks_diff, ticks_add
from ultrasonic import Ultrasonic
import tm1637

display = tm1637.TM1637(clk=pyb.Pin('X3'), dio=pyb.Pin('X4'))
sr04 = Ultrasonic(pyb.Pin('X1'), pyb.Pin('X2') )
led = pyb.Pin( 'X5', pyb.Pin.OUT_PP)


def get_distance():
    try:
        distance=sr04.distance_in_cm()
    except:
        distance=None
    return distance

def display_distance(distance):
    print("Distance : ", distance, "cm")
    if distance!=None:
        display.number(int(distance))
        

start=ticks_ms()
while True:
    distance=get_distance()
    display_distance(distance)
    if distance != None:
        if distance>100:
            led.low()
        elif distance<5:
            led.high()
        else:
            waiting=(distance*10)/2
            deadline=ticks_add(start,int(waiting))
            if ticks_diff(start,ticks_ms)>deadline:
                led.high()
                start=ticks_ms
            
    sleep(0.1)
    led.low()
    
    
    
