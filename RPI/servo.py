import RPi.GPIO as GPIO

SERVO_FREQ = 50

class Servo:
    def __init__(self, BCM_PORT, init_deg):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(BCM_PORT, GPIO.OUT)
        self.servo = GPIO.PWM(BCM_PORT, SERVO_FREQ)
        self.servo.start(self._deg2duty(init_deg))

    def change_deg(self, deg):
        self.servo.ChangeDutyCycle(self._deg2duty(deg))

    def _deg2duty(self, deg):
        return (deg / 18) + 2

    def __del__(self):
        self.servo.stop()
