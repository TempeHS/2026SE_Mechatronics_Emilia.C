from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

front = PiicoDev_Ultrasonic(id=[0, 0, 0, 0])
side = PiicoDev_Ultrasonic(id=[0, 0, 0, 1]) 

while True:
    print(f"Front distance: {front.distance_mm}", f"Side distance: {side.distance_mm}")
    sleep_ms(100)