import telemetry
import os
import main_menu as mm

if not os.path.exists("data.csv"):
    telemetry.create()


mm.main_menu(mm.questionnaire_data, mm.club_data)

telemetry.chart()
