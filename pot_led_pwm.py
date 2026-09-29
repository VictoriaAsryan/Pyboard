from pyb import Timer, Pin

pot = pyb.ADC( 'X20')
timmer = pyb.Timer(5, freq=500)
channel = timmer.channel(3, Timer.PWM, pin=Pin('X1'), pulse_width_percent=100)

while True:
    val_pot=pot.read()
    val_pot=(val_pot/4095)*100
    print("Val : ",val_pot)
    channel.pulse_width_percent(val_pot)
    pyb.delay(200)
