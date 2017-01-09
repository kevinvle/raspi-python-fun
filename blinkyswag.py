import RPi.GPIO as GPIO 
inpin = 7 
pin = 5
GPIO.setmode(GPIO.BOARD)
GPIO.setup(inpin, GPIO.IN)
GPIO.setup(pin, GPIO.OUT) 
GPIO.setwarnings(False) 

while True: 
    value = GPIO.input(inpin)
    if value == 1:
        GPIO.output(pin, GPIO.HIGH) 
        print "Not Pressed"
    else : 
        GPIO.output(pin, GPIO.LOW)
        print "Pressed"
GPIO.cleanup()
