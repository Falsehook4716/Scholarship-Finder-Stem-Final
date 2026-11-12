import telemetry as tm
def choose_club_menu(club_data):

    print("\nSelect a club.\n")
    choose_club_menu = ""
    for i in range(len(club_data)):
        choose_club_menu = choose_club_menu + f"{i+1}. {club_data[i][0]}" + "\n"

    last_element = len(club_data) + 1
    list_length = len(club_data)
    choose_club_menu = choose_club_menu + f"{last_element}. Return to Browse Clubs\n"

    while True:
        try:
            match int(input(choose_club_menu)):
                case a if a > 0 and a <= list_length:
                    print(f"Joined {club_data[a-1][0]}.  An email will be sent shortly.")
                    tm.clubs[a-1] = 1
                case b if b == last_element:
                    break
        except:
            continue


def display_clubs(club_data):

    clubs_menu = "1.Choose a club to join\n2. Return to Main Menu.\n"
    while True:
        print("=== SUPPORT NETWORKS ===")

        for club in club_data:
            print(f"Club Name: {club[0]}")
            print(f"Contact Info: {club[1]}")
            print(f"Club Description: {club[2]}")
            print("\n")

        match input(clubs_menu):
            case "1":
                choose_club_menu(club_data)
            case "2":
                break

def questionnaire_govaid(questionnaire_data):

    while True:
        print("1.", questionnaire_data[0])
        match input("Please enter 0 for no or 1 for yes: "):
            case "0":
                tm.q_data[0] = 0
                break
            case "1":
                tm.q_data[0] = 1
                break


def questionnaire_gpa(questionnaire_data):
    gpa = 0

    while True:
        print("2.", questionnaire_data[1])
        try:
            gpa = float(input("Please enter your GPA: "))
            if not (gpa >= 0 and gpa <= 4.0):
                raise ValueError
            break
        except ValueError:
            print("Please enter a GPA from 0-4")
            continue

    tm.q_data[1] = gpa

def questionnaire_minority(questionnaire_data):

    while True:
        print("3.", questionnaire_data[2])
        match input("Please enter a 0 for no or a 1 for yes: "):
            case "0":
                tm.q_data[2] = 0
                break
            case "1":
                tm.q_data[2] = 1
                break

def questionnaire_extracurricular(questionnaire_data):

    while True:
        print("4.", questionnaire_data[3])
        match input("Please enter a 0 for no or a 1 for yes: "):
            case "0":
                tm.q_data[3] = 0
                break
            case "1":
                tm.q_data[3] = 1
                break

def questionnaire_volunteer(questionnaire_data):

    while True:
        print("5.", questionnaire_data[4])
        match input("Please enter a 0 for no or a 1 for yes: "):
            case "0":
                tm.q_data[4] = 0
                break
            case "1":
                tm.q_data[4] = 1
                break

def questionnaire_income(questionaire_data):

    while True:
        print("6.", questionnaire_data[5])
        print("Please choose your income level from the following options:")
        print("1. $0 - $18,000")
        print("2. $18,001 - $27,000")
        print("3. $27,001 - $56,000")
        print("4. $56,001 - $68,000")
        print("5. $68,001 - $79,000")
        print("6. $79,001 - $100,000")
        print("7. $100,001 and above")
        try:
            match int(input("Please enter a number from 1-7: ")):
                case a if a >= 1 and a <= 7:
                    tm.q_data[5] = a
                    break
        except ValueError:
            continue

def questionnaire(questionnaire_data):

    last_element = str(len(questionnaire_data) + 1)
    list_length = len(questionnaire_data)

    while True:
        print("=== QUESTIONAIRE ===")
        for index in range(list_length):
            print(f"{index+1}. {questionnaire_data[index]}")
        match input(f"{last_element}. Return to main menu\n"):
            case "1":
                questionnaire_govaid(questionnaire_data)
            case "2":
                questionnaire_gpa(questionnaire_data)
            case "3":
                questionnaire_minority(questionnaire_data)
            case "4":
                questionnaire_extracurricular(questionnaire_data)
            case "5":
                questionnaire_volunteer(questionnaire_data)
            case "6":
                questionnaire_income(questionnaire_data)
            case a if a == last_element:
                break


def main_menu(questionnaire_data, club_data):
    main_menu = "=== MAIN MENU ===\n1.Take Questionnaire\n2.Join a Support Network\n3. Exit program\n"

    while True:
        match input(main_menu):
            case "1":
                questionnaire(questionnaire_data)
            case "2":
                display_clubs(club_data)
            case "3":
                print("Goodbye")
                break

club_data = [
        ["African Diaspora Club",
        "DeLon Lewis dellewis@everettcc.edu",
        "Our mission is to provide a place for students and staff to meet, connect, and exchange ideas and to give members the opportunity to share and learn about the African culture."
         ],

        ["Asian Student Union",
         "Lijao Serven lsevern@everettcc.edu",
         "Our mission is to have our members feel like they belong in a community where they can feel safe to be themselves. They can get to learn about other cultures that they may have never heard of and enjoy many experiences of what that culture is like. Being able to educate our members help them to learn more about the diversity of different ethnicities in the Asian community. People can come meet and connect with those who they may share interests in and we can operate this by going to temples, fun activities, having a Lunar new year party or learn about the meanings behind Asian cultures. There’s a big difference between Asians as they come from many different places."
         ],

        ["Black Student Union",
         "bsu@everettcc.edu",
         "The Everett Community College Black Student Union (BSU) is a student-led organization that promotes cultural, academic, intellectual, and economic advancement. The BSU is open to all interested persons with a genuine interest in Black culture and the betterment of the Black community."
        ]
        ]

questionnaire_data = [
        "Are you a participant in an assistance program?",
        "What is your overall GPA?",
        "Do you belong to a minority group?",
        "Sports involvement/extracurricular?",
        "Local and community groups?",
        "Income?"
        ]
#name, web, desc, gov_aid: 0/1, gpa: float, minority: 0/1, sports/activity: 0/1, volunteer: 0/1, income: 1-7
scholarship_data = [
                ["Merit Excellence Award", "https://meritexcellence.org", '', 3.85, '', 1, '', ''],
                ["Federal Pell Grant", "https://fafsa.gov/pell", 1, '', '', '', '', 1],
                ["STEM Future Leaders", "https://stemleaders.edu", '', 3.6, '', 1, 1, ''],
                ["Community First Scholarship", "https://communityfirst.org", '', 3.2, '', 1, '', 1, ''],
                ["Hispanic Heritage Fund", "https://hispanicheritage.edu", '', 3.0, 1, '', '', ''],
                ["Blue Ribbon Academic", "https://blueribbonacademy.org", '', 3.9, '', 1, 1, ''],
                ["Rural Opportunity Grant", "https://ruralopportunity.gov", 1, 3.1, '', '', 1, 3],
                ["Minority Engineers Alliance", "https://minorityengineers.org", '', 3.4, '', 1, 1, '', ''],
                ["Youth Volunteer Corps", "https://youthvolunteer.org", '', 2.8, '', '', 1, 4],
                ["Presidential Scholarship", "https://presidential.edu", '', 4.0, '', 1, 1, 7]
                  ]


def main():
    main_menu(questionnaire_data, club_data)

if __name__ == "__main__":
    main()
