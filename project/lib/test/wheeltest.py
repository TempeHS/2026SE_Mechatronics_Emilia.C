from wheel import Wheel
from time import sleep

pinL = 20
pinR = 18

def wheeltest():
    wheel = Wheel(pinleft=pinL, pinright=pinR)
    print("Going forward")
    wheel.forward(2)
    print("Going backward")
    wheel.backward(2)
    print("Turning left")
    wheel.left(2)
    print("Turning right")
    wheel.right(2)
    print("Pausing")
    wheel.pause(2)
    print("Stopping")
    wheel.stop()

if __name__ == "__main__":
    wheeltest()