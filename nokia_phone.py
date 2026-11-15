mainMenu = """
1 for Phonebook menu
2 for Messages menu
3 for chat menu
4 for call register menu
5 for Tones menu
6 for Settings menu
7 for Call divert menu
8 for Music menu
9 for Games menu
10 for Calculator menu
11 for Reminders menu
12 for Clock menu
13 for Profile menu
14 for WAP services menu
15 for SIM services
"""

print(mainMenu)
mainMenuOption = int(input("Enter your option: "))


if mainMenuOption == 1:

    phonebookMenu = """
    1 for Search
    2 for Service Nos.
    3 for Add name
    4 for Erase
    5 for Edit
    6 for Copy
    7 for Assign tone
    8 for Send b'card
    9 for Options
    10 for Speed dials
    11 for Voice tags
    """

    print(phonebookMenu)
    phonebookOption = int(input("Enter your option: "))

    if phonebookOption == 1:
        print("Search")

    elif phonebookOption == 2:
        print("Service Nos")

    elif phonebookOption == 3:
        print("Add name")

    elif phonebookOption == 4:
        print("Erase")

    elif phonebookOption == 5:
        print("Edit")

    elif phonebookOption == 6:
        print("Copy")

    elif phonebookOption == 7:
        print("Assign tone")

    elif phonebookOption == 8:
        print("Send b'card")

    elif phonebookOption == 9:

        optionsMenu = """
        1 for Memory in use
        2 for Types of view
        3 for Memory status
        """

        print(optionsMenu)
        optionsOption = int(input("Enter your option: "))

        if optionsOption == 1:
            print("Memory in use")

        elif optionsOption == 2:
            print("Type of view")

        elif optionsOption == 3:
            print("Memory status")

        else:
            print("Please enter the correct number")

    elif phonebookOption == 10:
        print("Speed dials")

    elif phonebookOption == 11:
        print("Voice tags")

    else:
        print("Wrong input")


elif mainMenuOption == 2:

    messageMenu = """
    1 for Write messages
    2 for Inbox
    3 for Outbox
    4 for Picture message
    5 for Templates
    6 for Smileys
    7 for Message setting
    8 for Info service
    9 for Voice mailbox number
    10 for Service command editor
    """

    print(messageMenu)
    messageOption = int(input("Enter your option: "))

    if messageOption == 1:
        print("Write messages")

    elif messageOption == 2:
        print("Inbox")

    elif messageOption == 3:
        print("Outbox")

    elif messageOption == 4:
        print("Picture")

    elif messageOption == 5:
        print("Templates")

    elif messageOption == 6:
        print("Smileys")

    elif messageOption == 7:

        messagesettingsMenu = """
        1 for Set 1
        2 for Common
        """

        print(messagesettingsMenu)
        messagesettingsOption = int(input("Enter your option: "))

        if messagesettingsOption == 1:

            print("Set 1")

            optionsMenu = """
            1 for Message centre number
            2 for Messages sent as
            3 for Message validity
            """

            print(optionsMenu)
            messagesettingOption = int(input("Enter your option: "))

            if messagesettingOption == 1:
                print("Message centre number")

            elif messagesettingOption == 2:
                print("Messages sent as")

            elif messagesettingOption == 3:
                print("Message validity")

            else:
                print("Please enter the correct number")

        elif messagesettingsOption == 2:

            print("Common")

            commonMenu = """
            1 for Delivery report
            2 for Reply via same centre
            3 for Character support
            """

            print(commonMenu)
            commonOption = int(input("Enter your option: "))

            if commonOption == 1:
                print("Delivery report")

            elif commonOption == 2:
                print("Reply via same centre")

            elif commonOption == 3:
                print("Character support")

            else:
                print("Please enter the correct number")

        else:
            print("Please enter the correct number")

    elif messageOption == 8:
        print("Info service")

    elif messageOption == 9:
        print("Voice mailbox number")

    elif messageOption == 10:
        print("Service command editor")

    else:
        print("Wrong input")


elif mainMenuOption == 3:

    print("chat")


elif mainMenuOption == 4:

    callRegisterMenu = """
    1 for Missed calls
    2 for Received calls
    3 for Dialled numbers
    4 for Erase recent call lists
    5 for Show call duration
    6 for Show call cost
    7 for Call cost settings
    8 for Prepaid credit
    """

    print(callRegisterMenu)
    callRegisterOption = int(input("Enter your option: "))

    if callRegisterOption == 1:
        print("Missed calls")

    elif callRegisterOption == 2:
        print("Received calls")

    elif callRegisterOption == 3:
        print("Dialled numbers")

    elif callRegisterOption == 4:
        print("Erase recent call lists")

    elif callRegisterOption == 5:

        showCallDurationMenu = """
        1 for Last call duration
        2 for All calls' duration
        3 for Received calls' duration
        4 for Dialled calls' duration
        5 for Clear timers
        """

        print(showCallDurationMenu)
        showcalldurationOption = int(input("Enter your option: "))

        if showcalldurationOption == 1:
            print("Last call duration")

        elif showcalldurationOption == 2:
            print("All calls duration")

        elif showcalldurationOption == 3:
            print("Received calls duration")

        elif showcalldurationOption == 4:
            print("Dialled calls' duration")

        elif showcalldurationOption == 5:
            print("Clear timers")

        else:
            print("Please enter the correct number")

    elif callRegisterOption == 6:

        showcostMenu = """
        1 for Last call cost
        2 for All calls' cost
        3 for Clear counters
        """

        print(showcostMenu)
        showCostOption = int(input("Enter your option: "))

        if showCostOption == 1:
            print("Last call cost")

        elif showCostOption == 2:
            print("All calls' cost")

        elif showCostOption == 3:
            print("Clear counters")

        else:
            print("Please enter the correct number")

    elif callRegisterOption == 7:

        callsettingsoptionMenu = """
        1 for Call cost limit
        2 for Show cost in
        """

        print(callsettingsoptionMenu)
        callsettingsoptionOption = int(input("Enter your option: "))

        if callsettingsoptionOption == 1:
            print("Call cost limit")

        elif callsettingsoptionOption == 2:
            print("Show cost in")

        else:
            print("Please enter the correct number")

    elif callRegisterOption == 8:
        print("Prepaid credit")

    else:
        print("Please enter the correct number")


elif mainMenuOption == 5:

    tonesMenu = """
    1 for Ringing tone
    2 for Ringing volume
    3 for Incoming call alert
    4 for Message alert tone
    5 for Keypad tones
    6 for Warning tones
    7 for Vibrating alert
    8 for Screen saver
    """

    print(tonesMenu)
    toneOption = int(input("Enter your option: "))

    if toneOption == 1:
        print("Ringing tone")

    elif toneOption == 2:
        print("Ringing volume")

    elif toneOption == 3:
        print("Incoming call alert")

    elif toneOption == 4:
        print("Message alert tone")

    elif toneOption == 5:
        print("Keypad tones")

    elif toneOption == 6:
        print("Warning tones")

    elif toneOption == 7:
        print("Vibrating alert")

    elif toneOption == 8:
        print("Screen saver")

    else:
        print("Please enter the correct number")


elif mainMenuOption == 6:

    settingsMenu = """
    1 for Call setting
    2 for Phone settings
    3 for Security setting
    4 for Restore factory settings
    """

    print(settingsMenu)
    settingsOption = int(input("Enter your option: "))

    if settingsOption == 1:

        callsettingsMenu = """
        1 for Automatic redial
        2 for Speed dialling
        3 for Call waiting options
        4 for Own number sending
        5 for Phone line in use
        6 for Automatic answer
        """

        print(callsettingsMenu)
        callsettingOption = int(input("Enter your option: "))

        if callsettingOption == 1:
            print("Automatic redial")

        elif callsettingOption == 2:
            print("Speed dialling")

        elif callsettingOption == 3:
            print("Call waiting options")

        elif callsettingOption == 4:
            print("Own number sending")

        elif callsettingOption == 5:
            print("Phone line in use")

        elif callsettingOption == 6:
            print("Automatic answer")

        else:
            print("Please enter the correct number")

    elif settingsOption == 2:

        phonesettingMenu = """
        1 for Language
        2 for Cell info display
        3 for Welcome note
        4 for Network selection
        5 for Confirm SIM service actions
        """

        print(phonesettingMenu)
        phonesettingOption = int(input("Enter your option: "))

        if phonesettingOption == 1:
            print("Language")

        elif phonesettingOption == 2:
            print("Cell info display")

        elif phonesettingOption == 3:
            print("Welcome note")

        elif phonesettingOption == 4:
            print("Network selection")

        elif phonesettingOption == 5:
            print("Confirm SIM service actions")

        else:
            print("Please enter the correct number")

    elif settingsOption == 3:

        securitysettingMenu = """
        1 for PIN code request
        2 for Call barring service
        3 for Fixed dialling
        4 for Closed user group
        5 for Security level
        6 for Change access codes
        """

        print(securitysettingMenu)
        securitysettingOption = int(input("Enter your option: "))

        if securitysettingOption == 1:
            print("PIN code request")

        elif securitysettingOption == 2:
            print("Call barring service")

        elif securitysettingOption == 3:
            print("Fixed dialling")

        elif securitysettingOption == 4:
            print("Closed user group")

        elif securitysettingOption == 5:
            print("Security level")

        elif securitysettingOption == 6:
            print("Change access codes")

        else:
            print("Please enter the correct number")

    elif settingsOption == 4:
        print("Restore factory settings")

    else:
        print("Please enter the correct number")


elif mainMenuOption == 7:

    print("Call divert menu")


elif mainMenuOption == 8:

    musicMenu = """
    1 for Music player
    2 for Radio
    3 for Recorder
    4 for Track list
    """

    print(musicMenu)
    musicOption = int(input("Enter your option: "))

    if musicOption == 1:
        print("Music player")

    elif musicOption == 2:
        print("Radio")

    elif musicOption == 3:
        print("Recorder")

    elif musicOption == 4:
        print("Track list")

    else:
        print("Please enter the correct number")


elif mainMenuOption == 9:

    print("Games menu")


elif mainMenuOption == 10:

    print("Calculator menu")


elif mainMenuOption == 11:

    print("Reminders menu")


elif mainMenuOption == 12:

    clockMenu = """
    1 for Alarm clock
    2 for Clock settings
    3 for Date setting
    4 for Stopwatch
    5 for Countdown timer
    6 for Auto update of date and time
    """

    print(clockMenu)
    clockOption = int(input("Enter your option: "))

    if clockOption == 1:
        print("Alarm clock")

    elif clockOption == 2:
        print("Clock settings")

    elif clockOption == 3:
        print("Date setting")

    elif clockOption == 4:
        print("Stopwatch")

    elif clockOption == 5:
        print("Countdown timer")

    elif clockOption == 6:
        print("Auto update of date and time")

    else:
        print("Please enter the correct number")


elif mainMenuOption == 13:

    print("Profile menu")


elif mainMenuOption == 14:

    print("WAP services menu")


elif mainMenuOption == 15:

    print("SIM services")


else:

    print("Please enter the correct number")
