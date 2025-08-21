import time
from servo import Servo
from machine import Pin, PWM


servo_pwm = PWM(Pin(18))
servo_pwm2 = PWM(Pin(20))


freq = 50
min_us = 500
max_us = 2500
dead_zone_us = 1500

my_servo = Servo(
    pwm=servo_pwm, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

my_servo2 = Servo(
    pwm=servo_pwm2, min_us=min_us, max_us=max_us, dead_zone_us=dead_zone_us, freq=freq
)

def forward():
    my_servo.set_duty(500)
    my_servo2.set_duty(2500)
    time.sleep(2)

def left():
    my_servo.set_duty(1300)
    my_servo2.set_duty(1500)
    time.sleep(2.85)

def right():
    my_servo.set_duty(1500)
    my_servo2.set_duty(1700)
    time.sleep(2.25)

def backward():
    my_servo.set_duty(2500)
    my_servo2.set_duty(500)
    time.sleep(2)

def pause():
    my_servo.set_duty(1500)
    my_servo2.set_duty(1500)
    time.sleep(2)

def stop():
    my_servo.stop()
    my_servo2.stop()
    time.sleep(2)