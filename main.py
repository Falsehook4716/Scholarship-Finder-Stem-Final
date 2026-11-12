import telemetry as tm
import os
import main_menu as mm

if not os.path.exists("data.csv"):
    tm.create()


#mm.main_menu(mm.questionnaire_data, mm.club_data)
#tm.c_append(tm.clubs)
#tm.q_append(tm.q_data)

#q_fieldnames = ["Gov_Aid", "GPA", "Minority", "Extracurricular", "Volunteer", "Income"]


def get_scholarships(data):
    qualified = []

    #compare values
    for scholarship in mm.scholarship_data:
        #checks
        qual = False
        for value in range(2, len(scholarship)):
            match value:
                case 2:
                    if scholarship[value] == '' or data[0] == scholarship[value]:
                        qual = True
                    else:
                        qual = False
                case 3:
                    if scholarship[value] == '' or data[0] >= scholarship[value]:
                        qual = True
                    else:
                        qual = False

                case 4:
                    if scholarship[value] == '' or data[0] == scholarship[value]:
                        qual = True
                    else:
                        qual = False

                case 5:
                    if scholarship[value] == '' or data[0] == scholarship[value]:
                        qual = True
                    else:
                        qual = False

                case 6:
                    if scholarship[value] == '' or data[0] == scholarship[value]:
                        qual = True
                    else:
                        qual = False

                case 7:
                    if scholarship[value] == '' or data[0] <= scholarship[value]:
                        qual = True
                    else:
                        qual = False

        if qual:
            qualified.append(scholarship)


    return qualified



print(get_scholarships(tm.q_data))
