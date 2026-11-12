import telemetry as tm
import os
import main_menu as mm

if not os.path.exists("c_data.csv"):
    tm.create()


mm.main_menu(mm.questionnaire_data, mm.club_data)
tm.c_append(tm.clubs)
tm.q_append(tm.q_data)



def get_scholarships(data):
    qualified = []

    print("Scholarships you may qualify for:\n")
    #compare values
    for scholarship in mm.scholarship_data:
        #checks
        qual = False
        for value in range(2, len(scholarship)):
            match value:
                case 2:
                    if (scholarship[value] == '' or data[0] == None) or data[0] == scholarship[value]:
                        qual = True
                    else:
                        qual = False
                case 3:
                    if (scholarship[value] == '' or data[1] == None) or data[1] >= scholarship[value]:
                        qual = True
                    else:
                        qual = False

                case 4:
                    if (scholarship[value] == '' or data[2] == None) or data[2] == scholarship[value]:
                        qual = True
                    else:
                        qual = False

                case 5:
                    if (scholarship[value] == '' or data[3] == None) or data[3] == scholarship[value]:
                        qual = True
                    else:
                        qual = False

                case 6:
                    if (scholarship[value] == '' or data[4] == None) or data[4] == scholarship[value]:
                        qual = True
                    else:
                        qual = False

                case 7:
                    if (scholarship[value] == '' or data[5] == None) or data[5] <= scholarship[value]:
                        qual = True
                    else:
                        qual = False

        if qual:
            qualified.append(scholarship)
            print(f"{scholarship[0]}")
            print()
            print(f"Website: {scholarship[1]}")
            print()
            print()





get_scholarships(tm.q_data)

tm.c_chart()
