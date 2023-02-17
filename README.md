Project Goals: 

Create an IoT themed device that gathers weather data (air quality), then provides information and action to the user.

Two main sections: 
App - A place for the information to be displayed

Device - Using raspberry pi and add ons, create a device that is able to take in data about the air quality. Will also do data processing. Local storage for the last 7 days, older historical data to perhaps be stored remotely? To be decided.

Project End:

Marketing Website - stingray-cobalt-lrr6.squarespace.com
         Password - embeddedhairline

Operating Website: 
    Clone repo, download the following:
    install flask, firebase, ... 
    navigate to the Web App folder
    run server.py: python3 server.py
    open http://127.0.0.1:8000
    View the site!

Pi Overview: 
    install CircuitPython, smbus, I2C, Adafruit-Blinka
    Data is collected from sensors using I2C bus. 
    This data is averaged out with the previous 60 values to provide a moving average.
    This flattens fluctuations in the data.
    The average is then sent approximately every 5 seconds, according to the "counter" variable.
    This uses a simple modulus check.

Backendoverview: 
    server.py runs all of the html and other python scripts.
    Calls are made to the firebase database for the realtime data updates
    Refreshing the page gives new advice. 





