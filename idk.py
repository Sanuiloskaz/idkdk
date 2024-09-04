from machine import Pin, PWM
import time

# Configuración del pin del botón y el servomotor
boton = Pin(23, Pin.IN, Pin.PULL_UP)  # Configuración del pin del botón con pull-up interno
servo = PWM(Pin(33), freq=50)  # Configuración del pin del servomotor con frecuencia de 50Hz

# Función para mover el servomotor a un ángulo específico
def mover_servo(angulo):
    # Rango de pulsos de servomotor típico: 0.5ms (0 grados) a 2.5ms (180 grados)
    # El valor de duty para PWM se calcula: duty = (angulo/180) * rango + mínimo
    rango = 102  # Rango entre 0.5ms y 2.5ms para PWM de 10 bits (0-1023)
    duty = int((angulo / 180.0) * rango + 26)  # Ajusta estos valores según tu servomotor
    servo.duty(duty)

# Bucle principal
while True:
    if boton.value() == 0:  # Verifica si el botón está presionado (valor bajo)
        mover_servo(90)  # Mueve el servomotor a 90 grados
        time.sleep(1)  # Espera un segundo
        mover_servo(0)  # Retorna el servomotor a 0 grados (o la posición inicial deseada)
        time.sleep(0.1)  # Pequeña espera para evitar rebotes
