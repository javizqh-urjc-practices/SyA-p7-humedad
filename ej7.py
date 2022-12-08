#!/usr/bin/python
import RPi.GPIO as GPIO
import signal
import sys
import http.client, urllib


ledPin = 3
humedadState = True # No humidity

humedadPin = 16

def callbackSalir(senial, cuadro):
    '''Clear the GPIO pin and exits the program'''
    GPIO.cleanup()
    sys.exit(0)

def callbackCambioHumedad(canal):
    '''Turns the led on or off according to the last state'''
    global humedadState
    if(humedadState):
        # Humidity detected
        humedadState = False
        GPIO.output(ledPin, GPIO.HIGH) 
    else:
        # No humidity
        humedadState = True
        GPIO.output(ledPin, GPIO.LOW)
        send_notif("Need to water plant")

def send_notif(message:str):
    '''Send a notification to the mobile Pushover app'''
    # Only works this specified device because the app is not free
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "afh9nq8q8spscntnyhd8ermfbtdw8c",
        "user": "uxdu1c5hgwci8kdonu8no8792jwynh",
        "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()

def main():
    
    send_notif("Humidity program started successfully")

    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(humedadPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
    GPIO.setup(ledPin, GPIO.OUT)

    GPIO.add_event_detect(humedadPin, GPIO.BOTH,callback=callbackCambioHumedad, bouncetime=5)
    signal.signal(signal.SIGINT, callbackSalir)

    signal.pause()
                  
   
          
main()
