import telemetry as tm
def choose_club_menu(club_data):
    '''Displays a list of clubs and takes user input to select a club to join.  Also saves the club that user joins.  This function was created to dynamically update to a changing list of clubs.'''
    print("\nSelect a club.\n")
    choose_club_menu = ""    #initialize an empty string to store the menu of clubs in
    for i in range(len(club_data)):    #for each club in the club_data
        choose_club_menu = choose_club_menu + f"{i+1}. {club_data[i][0]}" + "\n"  #this creates a numbered list of all the club names.  It was done this way so more clubs could be added and this would dynamically adjust to the number of clubs displayed.

    last_element = len(club_data) + 1
    list_length = len(club_data)
    choose_club_menu = choose_club_menu + f"{last_element}. Return to Browse Clubs\n"  #Once all clubs have been added, concatenate the final option to leave the menu

    while True:  #this loop is set to run infinitely until user provides valid input, and will break when user selects to exit the menu
        try:
            match int(input(choose_club_menu)):  #display the numbered list of clubs and ask user to choose a club from the list
                case a if a > 0 and a <= list_length:   #if user chooses from among the numbered clubs...
                    print(f"Joined {club_data[a-1][0]}.  An email will be sent shortly.")  #then show them successfully joining that said club
                    tm.clubs[a-1] = 1   #and save the user's selected club data to telemetry
                case b if b == last_element:  #if the user chooses the last_element on the numbered list, then that means they have chosen to return to the previous menu
                    break   #exit the loop and return to the previous menu
        except:  #if user inputs a non-integer value,
            continue   #loop the menu again until they provide valid input


def display_clubs(club_data):
    '''Displays all support networks (clubs) and a description of them along with contact info.'''

    clubs_menu = "1.Choose a club to join\n2. Return to Main Menu.\n"  #This is used for the menu for user input, used in the input function on line 38
    while True:  #this will loop infinitely until user provides one of the choices on line 39 and 41
        print("=== SUPPORT NETWORKS ===") #Display a menu of support networks (clubs)

        for club in club_data:  #This will display the club name, contact info, and description for each club in the club_data list
            print(f"Club Name: {club[0]}")
            print(f"Contact Info: {club[1]}")
            print(f"Club Description: {club[2]}")
            print("\n")

        match input(clubs_menu):  #Display the options of selecting a club to join, or exit back to the previous menu
            case "1":  #if user selects 1, then go to the menu to choose a club to join
                choose_club_menu(club_data)
            case "2":  #if user selects 2, then return to the previous menu
                break

def questionnaire_govaid(questionnaire_data):
    '''Takes input and saves user data to answer Government Aid question on scholarship questionnaire.'''

    while True:  #loops infinitely until user provides either 0 or 1 for no or yes
        print("1.", questionnaire_data[0])  #Ask user if they are receiving gov aid
        match input("Please enter 0 for no or 1 for yes: "):  #ask for user input
            case "0":  #if the user inputs 0 for no,
                tm.q_data[0] = 0   #save user data as a no in telemetry
                break   #return to questionnaire
            case "1":  #if the user inputs 1 for yes
                tm.q_data[0] = 1   #save user data as a yes in telemetry
                break  #return to questionnaire


def questionnaire_gpa(questionnaire_data):
    '''Takes input and saves user GPA for the scholarship questionnaire.'''
    gpa = 0

    while True:  #loops infinitely until user provides valid float 0-4
        print("2.", questionnaire_data[1])  #Ask the user for their GPA
        try:  #ensures user enters a float
            gpa = float(input("Please enter your GPA: "))
            if not (gpa >= 0 and gpa <= 4.0):  #repeat the loop if user enters a value outside 0-4
                raise ValueError
            break  #return to questionnaire once received valid input
        except ValueError:  #repeat the loop if user enters a non-float
            print("Please enter a GPA from 0-4")
            continue

    tm.q_data[1] = gpa  #before returnning to questionnaire, once we've received valid gpa as a float 0-4, save that float as user's GPA in telemetry

def questionnaire_minority(questionnaire_data):
    '''Takes input and saves data on user as a minority for scholarship questionnaire.'''

    while True:  #loops infinitely until user inputs a 0 for no or 1 for yes
        print("3.", questionnaire_data[2])  #Ask the user if they are a minority
        match input("Please enter a 0 for no or a 1 for yes: "):  #take user input
            case "0":  #if user enters 0 for no
                tm.q_data[2] = 0  #enter a no in user data telemetry
                break  #return to questionnaire
            case "1":   #if user enters 1 for yes
                tm.q_data[2] = 1  #enter a yes in user data telemetry
                break  #return to questionnaire

def questionnaire_extracurricular(questionnaire_data):
    '''Takes user input and saves data on user's extracurricular activity for scholarship questionnaire.'''

    while True:  #loops infinitely until user inputs 0 for no or 1 for yes
        print("4.", questionnaire_data[3])  #Ask user if they participate in extracurricular activities
        match input("Please enter a 0 for no or a 1 for yes: "):  #take user input
            case "0":  #if user inputs 0 for no
                tm.q_data[3] = 0   #enter a no for user data in telemetry
                break   #return to questionnaire
            case "1":   #if user inputs 1 for yes
                tm.q_data[3] = 1  #enter a yes for user data in telemetry
                break   #return to questionnaire

def questionnaire_volunteer(questionnaire_data):
    '''Takes user input and saves data for user's volunteer work for scholarship questionnaire.'''
    while True:   #loops infinitely until user enters 0 for no or 1 for yes
        print("5.", questionnaire_data[4])   #Ask user if they participate in volunteer work.
        match input("Please enter a 0 for no or a 1 for yes: "):  #take user input
            case "0":  #if user says 0 for no
                tm.q_data[4] = 0   #then save no as user data in telemetry
                break   #return to questionnaire
            case "1":    #if user says 1 for yes
                tm.q_data[4] = 1    #then save yes as user data in telemetry
                break    #return to questionnaire

def questionnaire_income(questionaire_data):
    '''Takes input and saves user data for income level for scholarship questionnaire.'''
    while True:    #loops infinitely until user selects an income range of 1-7
        print("6.", questionnaire_data[5])    #Ask user for their income range
        print("Please choose your income level from the following options:")   #Display the income ranges
        print("1. $0 - $18,000")
        print("2. $18,001 - $27,000")
        print("3. $27,001 - $56,000")
        print("4. $56,001 - $68,000")
        print("5. $68,001 - $79,000")
        print("6. $79,001 - $100,000")
        print("7. $100,001 and above")
        try:   #ensures user enters an integer
            match int(input("Please enter a number from 1-7: ")):  #ask for user input
                case a if a >= 1 and a <= 7:    #If user inputs a valid number from 1-7
                    tm.q_data[5] = a   #Save the income range number they choose to user data telemetry
                    break   #return to questionnaire
        except ValueError:   #if user inputs a non-numerical value
            continue   #ask user for input again

def questionnaire(questionnaire_data):
    '''Displays the full scholarship questionnaire and allows users to select a question to answer.'''
    last_element = str(len(questionnaire_data) + 1)   #in this case is 7.  dynamically find the number to assign the option to exit the questionnaire menu
    list_length = len(questionnaire_data)  #used to set the upper range for iteration

    while True:   #will loop infinitely until user chooses a question on the menu from 1-6 or 7 to exit
        print("=== QUESTIONAIRE ===")
        for index in range(list_length):    #iterate through and print out all of the questions in the scholarship quesionnaire
            print(f"{index+1}. {questionnaire_data[index]}")
        match input(f"{last_element}. Return to main menu\n"):  #take user input while printing last option to return to main menu
            case "1":   #if user chooses the Gov Aid question
                questionnaire_govaid(questionnaire_data)  #they are taken to function that allows them to enter their response
            case "2":    #if user choose the GPA question
                questionnaire_gpa(questionnaire_data)   #they are taken to the function that allows them to enter their response
            case "3":   #Minority question
                questionnaire_minority(questionnaire_data)   #function for minority question
            case "4":    #Extracurricular question
                questionnaire_extracurricular(questionnaire_data)  #function for extracurricular question
            case "5":    #Volunteer work question
                questionnaire_volunteer(questionnaire_data)   #function for volunteer question
            case "6":    #Income range question
                questionnaire_income(questionnaire_data)  #function for income range question
            case a if a == last_element:  #if user chooses 7 which is the last option on the list, then that means they want to exit back to main menu
                break   #return to main menu


def main_menu(questionnaire_data, club_data):
    main_menu = "=== MAIN MENU ===\n1. Take Questionnaire\n2. Join a Support Network\n3. Display Club Chart\n4. Exit program\n"

    while True:   #will loop infinitely until user inputs a valid choice 1-3
        match input(main_menu):  #Display main menu and ask user input
            case "1":   #If user selects 1, they will be guided to the scholarship questionnaire
                questionnaire(questionnaire_data)
            case "2":   #If user selects 2, they will be guided to browse and join support networks (clubs)
                display_clubs(club_data)
            case "3":   #If user selects 3, they will see a display of the club data chart
                tm.c_chart()
            case "4":   #If user selects 4, they will end program
                print("Goodbye")
                break   #end program entirely

#Data for clubs that user can join.  [Club Name, Contact Info, Club description]
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

#Questions for the scholarship questionnaire.
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
                ["Community First Scholarship", "https://communityfirst.org", '', 3.2, '', 1, '', 1],
                ["Hispanic Heritage Fund", "https://hispanicheritage.edu", '', 3.0, 1, '', '', ''],
                ["Blue Ribbon Academic", "https://blueribbonacademy.org", '', 3.9, '', 1, 1, ''],
                ["Rural Opportunity Grant", "https://ruralopportunity.gov", 1, 3.1, '', '', 1, 3],
                ["Minority Engineers Alliance", "https://minorityengineers.org", '', 3.4, '', 1, 1, ''],
                ["Youth Volunteer Corps", "https://youthvolunteer.org", '', 2.8, '', '', 1, 4],
                ["Presidential Scholarship", "https://presidential.edu", '', 4.0, '', 1, 1, 7]
                  ]


def main():
    main_menu(questionnaire_data, club_data)

if __name__ == "__main__":
    main()
