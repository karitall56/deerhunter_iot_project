import time                   # Allows use of time.sleep() for delays
from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO
import ubinascii              # Conversions between binary data and various encodings
import machine                # Interfaces with hardware components
import micropython            # Needed to run any MicroPython code
from machine import Pin       # Define pin

## Number of detections per hour
nodetection=int
nodetection=0
## Hour variables for checking when new hour and time to write total number of detections
currenthour=" "
prevhour=" "
client=" "

## Initiate start datetime
presenttime=time.localtime()
## presenttime is a tuple an object 3 is hour
currenthour=presenttime[3]
prevhour=presenttime[3]

led = Pin("LED", Pin.OUT)   # led pin initialization for Raspberry Pi Pico W

# Wireless network
WIFI_SSID = "Telia-B7F738"
WIFI_PASS = "Y6mJ8JpaFe6fKrtt" # No this is not our regular password. :)

# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "karitall"
AIO_KEY = "aio_diQe94Bopg3E8c1AGiWkBl1raLyz"
AIO_CLIENT_ID = ubinascii.hexlify(machine.unique_id())  # Can be anything
AIO_DEER_FEED = "karitall/feeds/deerhunter"
client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)

led = machine.Pin("LED", machine.Pin.OUT)
PirSensor = Pin(28, Pin.IN, Pin.PULL_DOWN)

# FUNCTIONS

#Check if sensor indication any motions
def check_move():
    
    global currenthour
    global prevhour
    global nodetection
    
    ## Get current datetime
    currenttime=time.localtime()
    ## currenttime is a tuple an object 3 is hour
    currenthour=currenttime[3]
    
    #Check if new period (hour) - set true to create item with total detections per hour to Adafruit
    #
    if prevhour != currenthour:
        print ("Timme nu ", currenthour, " Timme då ", prevhour, " tid ", currenttime, " Antal ", nodetection)
        prevhour = currenthour
        print ("Antal rörelser sätter true ", nodetection)
        return True
    
    #Check if motion - add to total detections in period (hour) - Set False not to send to Adafruit since same hour
    if PirSensor.value() ==1: # status of PIR output
        print("motion detected") # print the response
        led.on()
        nodetection = nodetection +1    
        print ("Antal rörelser ", nodetection)    
        
        return False
    
    #If no detections, just switch off Led lamp 
    led.off()
    return False

# Function to connect Pico to the WiFi
def do_connect():
    #import keys
    import network
    from time import sleep
    import machine
    wlan = network.WLAN(network.STA_IF)         # Put modem on Station mode

    if not wlan.isconnected():                  # Check if already connected
        print('connecting to network...')
        wlan.active(True)                       # Activate network interface
        # set power mode to get WiFi power-saving off (if needed)
        wlan.config(pm = 0xa11140)
        wlan.connect("Telia-B7F738", "Y6mJ8JpaFe6fKrtt")  # Your WiFi Credential
        print('Waiting for connection...', end='')
        # Check if it is connected otherwise wait
        while not wlan.isconnected() and wlan.status() >= 0:
            print('.', end='')
            sleep(1)
    # Print the IP assigned by router
    ip = wlan.ifconfig()[0]
    print('\nConnected on {}'.format(ip))
    return ip 
    
# Function to publish number of detection to Adafruit IO MQTT server at fixed interval (hour)
def send_adafruit():
    
    
    global nodetection    
    total_detect = nodetection
    nodetection=0
    print("Publishing on Adafruit:  ", total_detect, " Nya ack ", nodetection)
    #In a controlled way handle issues if call to Adafruit fails
    try:
        client.publish(topic=AIO_DEER_FEED, msg=str(total_detect))
        print("DONE ADAFRUIT", total_detect)
    except Exception as e:
        print("FAILED")
        print("TYP ", type(e))
        print("ARG ", e.args)
        print("Text ", e)
    finally:
        last_random_sent_ticks = time.ticks_ms()
    

# Try WiFi Connection
def connect_wifi():
    try:
        ip = do_connect()
    except Exception as e:
        print("FAILED")
        print("TYP ", type(e))
        print("ARG ", e.args)
        print("Text ", e)

# Use the MQTT protocol to connect to Adafruit IO
def connect_adafruit():
    global client
    try:
        
        client = MQTTClient(AIO_CLIENT_ID, AIO_SERVER, AIO_PORT, AIO_USER, AIO_KEY)
        client.connect()
    except Exception as e:
        print("FAILED client connect ADAFRUIT")

#print("Connected to %s, subscribed to %s topic" % (AIO_SERVER, AIO_LIGHTS_FEED))



try:                      # Code between try: and finally: may cause an error
                          # so ensure the client disconnects the server if
                          # that happens.
    while 1:			  # Repeat this loop forever
        
        if check_move():
            #Connect to wifi
            connect_wifi()
            #Connect to adafruit for sending message
            connect_adafruit()
            
            client.check_msg()# Action a message if one is received. Non-blocking.
            
            #Send the message to adafruit 
            send_adafruit()     # Send a random number to Adafruit IO if it's time.
            
            #disconnect from adafruit
            client.disconnect()   # ... disconnect the client and clean up.
            client = None    
        time.sleep(3)
except KeyboardInterrupt:
        print("Keyboard interrupt")    
finally:
   # If an exception is thrown ...
   
   client.disconnect()   # ... disconnect the client and clean up.
   client = None
   print("Disconnected from Adafruit IO.")
