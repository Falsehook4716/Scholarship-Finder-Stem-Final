import telemetry
import os

if not os.path.exists("data.csv"):
    telemetry.create()
x=input("get x; ")
y=input("get y; ")
z=input("get z; ")
telemetry.append(x,y,z)
telemetry.chart()
