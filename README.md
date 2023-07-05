# deerhunter_iot_project
Keeping animals away from my garden

2023-07-05                    2

# Innehåll
[Project Deer hunter	2](#_toc139381156)

[Project overview:	2](#_toc139381157)

[Problem:	2](#_toc139381158)

[Vision:	2](#_toc139381159)

[Project overview:	2](#_toc139381160)

[Time:	2](#_toc139381161)

[Objective	2](#_toc139381162)

[Why this project?	2](#_toc139381163)

[Purpose of the project:	3](#_toc139381164)

[Project insights:	3](#_toc139381165)

[Material	3](#_toc139381166)

[Computer setup	4](#_toc139381167)

[Chosen IDE	4](#_toc139381168)

[Some thoughts	5](#_toc139381169)

[Installation and preparation	5](#_toc139381170)

[Putting everything together	6](#_toc139381171)

[C-SR501 PIR Sensor	6](#_toc139381172)

[Loudspeaker 8 ohm 0,25 W direct connection	6](#_toc139381173)

[Loudspeaker 8 ohm 0,25 W via amplifier class-D 2,5 W mono connection	6](#_toc139381174)

[Components to put all together	6](#_toc139381175)

[The current solution/functions	7](#_toc139381176)

[Next steps	7](#_toc139381177)

[The code	7](#_toc139381178)

[Current solution code	7](#_toc139381179)

[Main.py	7](#_toc139381180)

[mqtt.py	9](#_toc139381181)

[circljud.py	9](#_toc139381182)

[mixer.py	9](#_toc139381183)

[Transmitting the data / connectivity	9](#_toc139381184)

[Presenting the data	10](#_toc139381185)

[Download of Adafruit motion data	10](#_toc139381186)

[Finalizing the design	10](#_toc139381187)






# <a name="_toc139381156"></a>Project Deer hunter

Kari Talltjärn - kt222qq
## <a name="_toc139381157"></a>Project overview:
### <a name="_toc139381158"></a>Problem: 
Deer’s are eating my garden plants.
### <a name="_toc139381159"></a>Vision: 
Get a solution that detects the animals, trigger some sound and get them running away. 
## <a name="_toc139381160"></a>Project overview: 
1. Gather knowledge about technical platform, communication, sensors, programming and environment for presentation of statistics. 
1. Establish a test environment with motion detector, play sound and get statistics when animals visit the garden. The latter in order to be able to take further action.     
1. Establish a technical solution to be able to use the solution outdoors and in Nordic climate. 
## <a name="_toc139381161"></a>Time: 
Estimated total time for delivery of the above strategies: 80+40+80 hours
# <a name="_toc139381162"></a>Objective

## <a name="_toc139381163"></a>Why this project? 

The main reason is that I want to preserve my seedlings in the garden. Every year I sow seeds or buy plants / bulbs that I want to build my garden with. 

I do not want the deer’s to eat them. 

Another reason is my interest in IOT. During my last years in worklife, I learned how to make applications for mobile phones using google as “teacher”. 

Developed some mobile apps where you can use the phone in (Volvo Eskilstuna) factory. E.g. Maintenance reporting and Transmission inspection.

At the same time, there were many test activities to buy different sensors that were connected to suppliers' cloud services. The solutions were suppliers' closed systems. Many experiments but no strategy!

Would like to learn how to establish more open solutions and use them in my home. Have meanwhile invested in building solutions such as Ikea lighting, control of floor heating via mobile application, solar cells, geothermal heating, google home, etc. 

There is more to learn and to do. This is now a hobby for me. 
## <a name="_toc139381164"></a>Purpose of the project: 
Via a motion detector receive signals to an application, send a “frightening” sound to a speaker and hopefully scare the animals away. 

Optionally add flashing lights, etc. as an addition. 

Collect statistics and present a graph of the periods during when the animals visit the garden. The latter is to take other actions such as using e.g. "Gold Water". For more information on this, I refer to google! 
## <a name="_toc139381165"></a>Project insights: 
In addition to hopefully getting a solution for the garden, I hope to learn about microcomputer environment. 

I already have a red-white Rasberry pie that I haven't really done anything with. It is just collecting dust!

With insight into this environment, in addition to the possibilities of the microcomputer, I get to learn sensors and their opportunities, Python (for microcomputers), communication solutions, cloud services for presentation. 

As a private person, I appreciate that there are solutions that can be established at low costs.
# <a name="_toc139381166"></a>Material

Included material and components in this project:


|**Component**|**Usage**|**Price SEK**|**Supplier**|**Comment**|
| :- | :- | :- | :- | :- |
|Rasberry pie pico W|CPU and 40 connections for sensors, etc. |<p>Included in startkit</p><p>310\.2[^1]</p>|Electro:kit|Low cost cpu with enough amount of connections for IN/OUT signals and host applications with logic|
|Cables|Connecting Rasberry Pie with sensors and output devices |310\.2<sup>1</sup>|Electro:kit||
|PIR motion detector HC-SR501|Trigger motions in front of sensor and causing event in program|39\.2|Electro:kit||
|Speaker 8 ohm  0,25 W|Testing output sound when motion triggered|7\.6|Electro:kit|Required CircuitPython (my knowledge?). Sound became just noise and not just as an .mp3 file|
|<p>Amplifier klass-D 2,5W mono PAM8302A</p><p></p>|To improve the sound. Connected between CPU and speaker|47\.2|Electro:kit|Required CircuitPython (my knowledge?). Could not get this to work.|
|<p>Python 3</p><p></p>|Programming of application logic|Free|https://www.python.org/||
|<p>Circuit Python</p><p></p>|Programming of application logic. For testing sound.|Free|https://circuitpython.org/|Tried to install Adafruit-Blinka 8.19.0 and Adafruit-PlatformDetect-3.46.0 to run both python 3 and Circuit Python. Not enough space to install both.|
|Adafruit|Presentation GUI as cloud service. Showing no of motions per hour |<p>Some maximum limitations but enough for this project</p><p>Free[^2]</p><p></p>|Adafruit industries||
|Thonny|Development and testing environment|<p>Free</p><p></p>|https://thonny.org/|Did not get VS Code with PyMakr to work for Rasberry Pie. Took too much time and used Thonny instead.|
|Private wifi|Sending motion messages via internet to presentation in Adafruit IO|Free|||
# <a name="_toc139381167"></a>Computer setup
## <a name="_toc139381168"></a>Chosen IDE

I tried a number of times to install VS Code, Node js and PyMakr but failed to get program running on my unit Rasberry Pie Pico W. 

I normally use Visual Studio for creating applications in C# and Xamarin, Windows Forms, WFP so I would prefer to work in similar environment.

I instead installed and use Thonny as IDE. Can be downloaded for free and you will work with two file systems. Windows dictionary and Rasberry Pie dictionary. Normally you edit your program version in Windows dictionary, copy it to Rasberry Pie dictionary and then execute the code in Rasberry Pie.

The interpreter (making source code to machine code) informs you with row number and error text if there are any issues with the code. The code used is Python 3.

Hint: Be aware in what version you are editing. In Windows filesystem or in Rasberry pi. I always close files when starting new activity and always edit in windows filesystem version.

Most used actions are below. Just right click on mouse and select.

- Save
- Open in thonny
- Upload to Rasberry pie
- Open in thonny (Rasberry pie version/file system) and run 

![C:\Users\karitall\Documents\Privat\Utbildning\IOT grund\Examen\Thonny.JPG](Aspose.Words.7eeb2578-4603-4dfa-8af5-59ef5d40d9d4.001.jpeg)
## <a name="_toc139381169"></a>Some thoughts

This technology area is very much new for me and during these weeks I have become aware of other technologies within same solution area. 

It seems that there is a variety of brands, platforms, services in this fast growing area. IOT was “hot” in my last years in work life and I understand it still is?

So the interesting question is what will be the “global standards” in future or segments big enough to provide solutions and “earn money”? 

Some areas I have touched:

- Rasberry pie Pico W – Arduino Uno
  - E.g. Kjell and company are providing equipment for the Arduino platform
- Python 3 – Circuit Python
  - E.g. I found only sound solutions made with Circuit Python on google
- Communication solutions/protocols
- Cloud solutions

The future will be interesting. 
## <a name="_toc139381170"></a>Installation and preparation
As mentioned above I decided to use Thonny as IDE.

Steps to prepare environment:

1. Download and install Thonny - <https://github.com/thonny/thonny/wiki/Windows>
1. Install python 3 - <https://www.python.org/downloads/>
   1. Download the package
   1. Connect an USB cable to your Rasberry Pico. Do not connect to your Windows computer
   1. Hold down the white button on your Rasberry pico and connect the USB cable to your Windows computer.
   1. Release button and you will see a new logical disk is showing in file explorer
   1. Copy the python download file to the new disk. Python is initiated/flashed and the disk disappear in file explorer. Done!
1. Create a folder in windows file explorer where you store different project folders/applications
1. Adafruit configuration
   1. See the tutorial - <https://learn.adafruit.com/welcome-to-adafruit-io/getting-started-with-adafruit-io>
1. Sound test – It seems that supporting sound from Rasberry Pico I need to use circuit python. I did some installations and testing but did not get this to work. Here is a summary
   1. Installed just circular python to test connecting a loudspeaker directly to Rasberry pie. Got some noise but not as my sound file (.mp3)
   1. Added an amplifier to the a solution but did not get any sound at all
   1. Since the found solution for sound required Circuit Python I tried to install Adafruit blinka and Adafruit platform detect to use both python 3 and circuit python code. This failed because lack of space.


# <a name="_toc139381171"></a>Putting everything together
Circuit diagram for used platforms are shown as below. Images in Github.
## <a name="_toc139381172"></a>C-SR501 PIR Sensor 

The HC-SR501 has a 3-pin connector. The markings are hidden by the Fresnel lens, so refer to the following image for pinout.

See image in Github.
## <a name="_toc139381173"></a>Loudspeaker 8 ohm 0,25 W direct connection

Simple loudspeaker.

See imaged in Github.
## <a name="_toc139381174"></a>Loudspeaker 8 ohm 0,25 W via amplifier class-D 2,5 W mono connection 

Simple loudspeaker vid amplifier between Rasberry Pie Pico W and Loudspeaker.

See image in Github.
## <a name="_toc139381175"></a>Components to put all together

Until now I have not found any solution for the loudspeaker. Do I have to use circular python? Learning Python 3 is new for me and Circular Python will be the same. In my current timeplan I am just focusing that current used components should work together.

I have made inquiries about motion detectors for outdoor conditions. Request made to:

- Kjell och Company – They have solutions but all are “closed” using the supplier’s presentation GUI. Have not yet found a solution where I could e.g. export the motion detector file
- Electro:kit – No response 

The current solution is limited to detecting motions and sending motion info to Adafruit for presentation. The presentatiuon is of secondary interest for taking other actions avoiding deer’s in gardens. Taking the info presented (Date/Time of day/night) to take actions. 

Since this is not prioritized I just selected a cloud service that was simple to setup. I am not going to upgrade to a paid service. 

Another alternative is to investigate how to just create a file and load it into a local Excel-sheet or similar. The sensor data is simple – number of motions per hour, date and time.

The next step is to find sensor and loudspeaker for outdoor conditions. I also need to find out how to set up a solution for sound in Python (or do I have to convert to Circuit Python?).
## <a name="_toc139381176"></a>The current solution/functions
- One time activity - Setup Dashboard and data feed in Adafruit cloud service
- Program summary
  - Login to WiFi
  - Create client for connecting/sending data to Adafruit data feed
  - Execute a loop checking sensor for motions
    - If motions 
      - add one to summary of motions
      - set Led lamp on Rasberry Pico on
    - If new hour
      - Enable Adafruit client
      - Send summary motions to Adafruit
      - Disable Adafruit client
    - If no motions
      - Disable Led lamp
## <a name="_toc139381177"></a>Next steps
- Solve sound solution
  - This is the core of this solution. I want to frighten the deer’s with some scary sound.
- Find outdoor equipment’s	 
# <a name="_toc139381178"></a>The code

## <a name="_toc139381179"></a>Current solution code

Below is an overview of included functions in the program used for the current solution:

- Main.py – Main program defining variables, functions, execution. Done in Python 3.
- MQTTClient.py – Program for describe in detail all functions for using the MQTT client/transport protocol communicating with Adafruit dashboard. Done in Python 3. 
- Circljud.py – For testing sound with direct connected loudspeaker. Done in Circuit Python. 
- Mixer.py – For testing sound with amplifier and loudspeaker. Done in Circuit Python. 
### <a name="_toc139381180"></a>Main.py

**Initialization**

Use code in other modules needed for the program

import time                   # Allows use of time.sleep() for delays

from mqtt import MQTTClient   # For use of MQTT protocol to talk to Adafruit IO – MQTTClient program contains all functions needed to define actions for the MQTT-client

import machine                # Interfaces with hardware components

import micropython            # Needed to run any MicroPython code

from machine import Pin       # Define pin

Define variables like no of motions and current/prev hour. Initiate the variables in start

Define Pin for setting LED lamp

Set user and password for accessing WiFi

Set variables for access and where to send motion data to Adafruit dashboard

**FUNCTIONS**

Check if sensor indication any motions

Check current hour against prev hour

Set true if new hour	

If motion

Add 1 to number of motions per hour

Set led lamp on

Set false

If no motion

Set led lamp off

Set false

Function to connect Pico to the WiFi

Check if already connected

If not connected

Connect to Wifi

Confirm with IP address if connected



Function to publish number of detection to Adafruit IO MQTT server at fixed interval (hour)

Send the total numbers of motions to Adafruit using the predefined client



Try WiFi Connection

Check of connection to Wifi

Do above connect function

Check if failed

If failed print error text

Use the MQTT protocol to connect to Adafruit IO

Connect to Adafruit with prior deined client

Check if failed

If failed print error text

Program loop with main functions

Repeat this loop forever until user interupting

Do check motions as above

If new hour

Do Connect to wifi

Do      connect\_adafruit()

Do Send the message to adafruit 



disconnect from adafruit



KeyboardInterrupt:

`      `If user stop the program
### <a name="_toc139381181"></a>mqtt.py

The program contains of a number of detailed functions for communicate via the MQTT-client/protocol to selected server (Adafruit in this case). The module is generic and the main application (main.py) are requesting each function with required parameters. The functions used in mgtt.py are connect, disconnect and publish. 
### <a name="_toc139381182"></a>circljud.py

Installed CircuitPython just to check if I get any sound. Did get some “noice” but no sound as used .mp3 file. Code as attachment. This is not implemented since I did not manage to use both Python 3 and CircuitPython. 

### <a name="_toc139381183"></a>mixer.py

Installed CircuitPython just to check if any sound. Got no sound at all. Code as attachment. I did not investigate what went wrong since did not manage to use both Python 3 and CircuitPython. 
# <a name="_toc139381184"></a>Transmitting the data / connectivity

The data sent to presentation dashboard is managed by below steps:

1. login to WiFi with user-id and password
1. Define a MQTT client with user keys as defined in Adafruit.
   1. MQTT client is an all-round client that runs an MQTT library. In this case sending messages and acts as publisher
1. Loop until user interruption 
   1. When new hour send a message to Adafruit Feed which is part of a Dashboard. The data is only number of motions per last hour
      1. Logon to WiFi and get internet access (if not connected)
      1. Connect MQTT-client to Adafruit 
      1. Send message – number of motions - via MQTT-client to Adafruit
      1. Disconnect MQTT-Client

The package contains just feed-name (defined in Adafruit as to be presented in dashboard) and number of motions. The package is sent once per hour.

Reusing my private WiFi to get to internet and MQTT protocol which seems to be “standard” for IOT solutions.

` `I have not yet looked into a battery solution. The testing of motion sensor loop is what I guess the primary energy user. 

# <a name="_toc139381185"></a>Presenting the data

The data presentation is just a simple line diagram showing number of motions per hour. In future solution I will import the file and just make a diagram in e.g. Excel to see time of year when deers/other animals are visiting the garden. Will be used for adding some other physical actions to keep animal away from the garden. 

## <a name="_toc139381186"></a>Download of Adafruit motion data


It is very easy to download a file with data from Adafruit. It can be of format .json or .csv and when in “production” mode it could be a routine e.g. once a week. The volume of data is small and the solution could also be changed that hours with 0 motions data not will be sent. 

![](Aspose.Words.7eeb2578-4603-4dfa-8af5-59ef5d40d9d4.002.png)

# <a name="_toc139381187"></a>Finalizing the design

The vision and strategy for this project are fulfilled when it comes to objective 1 and 2.

I have learned about Microcomputer Raspberry Pie Pico W, Sensors, Thonny, Python 3, Adafruit as cloud solution, communications and also provided and running a first test environment.

I have put in some print statements in the program code just to see the flow.

![](Aspose.Words.7eeb2578-4603-4dfa-8af5-59ef5d40d9d4.003.png)

Presentation of GUI is showed above.

Had some challenges in python programming when it came to use of variables and calling functions. Python is totally new for me.

Had good guidance using the components from the roadmap document in this course. It was pretty easy to make a program using the python code provided. Had some Python challenges as above.

I was not successful in installing the IDE Visual Studio code. Have to look into this further on.

Main source of support has been as always – Google. There seems to be solutions/answers for “everything” in the “competence space”. 

Next step will be investigating objective 3 to find sensors and setup for outdoor solution.

IOT is interesting and hope to come up with more solutions combining Mobile Apps, Windows forms/WFP, Google home, automated home solutions and solutions based on microcomputers, sensors and python.   

[^1]: 
[^2]: 
