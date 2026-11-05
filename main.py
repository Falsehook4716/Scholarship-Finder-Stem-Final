import telemetry
import os

if not os.path.exists("data.csv"):
    telemetry.create()
telemetry.append("jason", "brody")
