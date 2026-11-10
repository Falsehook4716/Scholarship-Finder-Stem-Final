import telemetry as tm
import os
import main_menu as mm

if not os.path.exists("data.csv"):
    tm.create()


mm.main_menu(mm.questionnaire_data, mm.club_data)
tm.append(tm.clubs)
tm.chart()
