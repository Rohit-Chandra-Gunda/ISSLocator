"""
    Copyright 2018 Gunda Rohit Chandra

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""
import json
import urllib.request
import turtle
import time
import math

url = 'http://api.open-notify.org/astros.json'

print("The url  http://api.open-notify.org/astros.json works during may 2018")

response = urllib.request.urlopen(url)

result = json.loads(response.read().decode())

print("Number of people in ISS ", result['number'])

people = result['people']

for p in people:
    print(p['name'])

url = 'http://api.open-notify.org/iss-now.json'

response = urllib.request.urlopen(url)

result = json.loads(response.read().decode())

location = result['iss_position']
latitude = location['latitude']
longitude = location['longitude']

print("\nLatitude of the ISS station is ", latitude)
print("Longitude of the ISS station is ", longitude)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('map.gif')

screen.register_shape('iss.gif')
iss = turtle.Turtle()
iss.shape('iss.gif')
iss.pu()
iss.setheading(90)
iss.goto(int(float(longitude)), int(float(latitude)))

turtle.mainloop()
