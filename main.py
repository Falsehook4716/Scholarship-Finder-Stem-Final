import telemetry
import os

if not os.path.exists("data.csv"):
    telemetry.create()
telemetry.append(2, 3)
telemetry.append(1, 3, 4)
telemetry.append(data3=5)

telemetry.chart()
