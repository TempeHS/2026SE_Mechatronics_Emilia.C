from PiicoDev_Ultrasonic import PiicoDev_Ultrasonic
from PiicoDev_Unified import sleep_ms

class UltrasonicSensor(object):
    def __init__(self, id=None):
        self.sensor = PiicoDev_Ultrasonic(id=id)
    
    def get_distance(self):
        return self.sensor.read()
    
    def wait_distance(self, threshold_millimetres, check_interval_ms=100):
        while True:
            distance = self.get_distance()
            if distance is not None and distance < threshold_millimetres:
                return distance
            sleep_ms(check_interval_ms)
