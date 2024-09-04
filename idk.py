from machine import Pin, PWM
import time

boton = Pin(23, Pin.IN, Pin.PULL_UP)
servo = PWM(Pin(33), freq=50)

def mover_servo(angulo):
    rango = 102
    duty = int((angulo / 180.0) * rango + 26)
    servo.duty(duty)

while True:
    if boton.value() == 0:
        mover_servo(90)
        time.sleep(1)
        mover_servo(0)
        time.sleep(0.1)
