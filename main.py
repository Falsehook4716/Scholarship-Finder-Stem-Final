import telemetry as tm
import os
import main_menu as mm

if not os.path.exists("data.csv"):
    tm.create()


mm.main_menu(mm.questionnaire_data, mm.club_data)
tm.c_append(tm.clubs)
tm.q_append(tm.q_data)

q_fieldnames = ["Gov_Aid", "GPA", "Minority", "Extracurricular", "Volunteer", "Income"]
def get_scholarships():
        return
