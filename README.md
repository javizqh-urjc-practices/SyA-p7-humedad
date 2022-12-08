# P7-Humedad
## Hardware problems
The problem we encountered was that the humidity sensor only worked when we connected it with two wires, we don't know the reason for that, but we think that it is because the GPIO pins are digital, so they only have two states and we didn't achieve to change this behaviour using the PWM.

## Observations
The code is almost the same as the previous excercise because the behaviours are almost the same.

We used a normal led instead of a rgb one because it doesn't matter as much as in previous excercises.
The led turns on when the humidity is detected and off when not.
```python
GPIO.setup(ledPin, GPIO.OUT)
```

An extra feature thet we decided to add is the sending of notofications to a mobile device using [Pushover](https://pushover.net/). This  is only implemented for demonstration purposes because we are using a free trial. Also it only works for my device, because if not we would have had to manually sign up every other device, and also we would have had to paid for the standard version.
```python
    # Only works this specified device because the app is not free
    conn = http.client.HTTPSConnection("api.pushover.net:443")
    conn.request("POST", "/1/messages.json",
    urllib.parse.urlencode({
        "token": "afh9nq8q8spscntnyhd8ermfbtdw8c",
        "user": "uxdu1c5hgwci8kdonu8no8792jwynh",
        "message": message,
    }), { "Content-type": "application/x-www-form-urlencoded" })
    conn.getresponse()
```

So when the sensor doesn't detect humidity it sends a notification to the mobile phone, to reminder the user to water the soil.