Project Goals: 

Create an IoT themed device that gathers weather data (air quality), then provides information and action to the user.

Two main sections: 
Website: Takes data from the database that has originated from the device, and displays the current exposure as well as 
relevant advice. 

Device - Using raspberry pi I2C connections with si7021 (temp and humidity), bmp280(atmospheric pressure) and ccs811(co2 and TVoC*)
sensors, gather environmental data, process and export it to a database.

Project End:

Marketing Website - stingray-cobalt-lrr6.squarespace.com
         Password - embeddedhairline

Operating Website: 
    Clone repo, download the following:
    install the following dependencies: 
    request, flask, firebase_admin.
    To do this, use the command : python3 -m pip install _name_
    navigate to the Web App folder
    run server.py: python3 server.py
    open http://127.0.0.1:8000
    View the site!

Pi Overview: 
    Data is collected from sensors using I2C bus. 
    This data is averaged out with the previous 60 values to provide a moving average.
    This flattens fluctuations in the data.
    The average is then sent approximately every 5 seconds, according to the "counter" variable.
    This uses a simple modulus check.

Backend overview: 
    server.py runs all of the html and other python scripts.
    Calls are made to the firebase database for the realtime data updates
    Refreshing the page gives new advice. 


*TVoC is a measure of Total Volatile Organic Compounds











