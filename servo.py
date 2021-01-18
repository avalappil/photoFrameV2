import maestro
import time
servo = maestro.Controller()
def move(ac, speed, target):
    servo.setAccel(0, ac)
    servo.setSpeed(0, speed)
    servo.setTarget(0, target)

print("moving to vertical")
move(25, 5, 6350)
time.sleep(8)
print("moving to horizontal")
move(25, 5, 2680)
time.sleep(8)

servo.close


