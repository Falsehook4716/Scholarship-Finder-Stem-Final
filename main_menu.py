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

def questionnaire(questionnaire_data):

    last_element = str(len(questionnaire_data) + 1)
    list_length = len(questionnaire_data)

    while True:
        print("=== QUESTIONAIRE ===")
        for index in range(list_length):
            print(f"{index+1}. {questionnaire_data[index]}")
        match input(f"{last_element}. Return to main menu\n"):
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
        "Are you receiveing government aid?",
        "What is your overall GPA?",
        "Do you belong to a minority group?",
        "Sports involvement/extracurricular?",
        "Local and community groups?",
        "Income?"
        ]

def main():
    main_menu(questionnaire_data, club_data)

if __name__ == "__main__":
    main()
