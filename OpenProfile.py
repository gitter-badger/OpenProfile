'OpenProfile is a free and open-source easy to use autobiography and biography creator written in Python. Copyright (C) 2014 DeavmiOSS'
'Below we start setting up strings'
app_name = "OpenProfile"
app_name_short = "OP"
app_version_number = "1.4.0.0"
app_version_stableness = "pre-beta"
app_version_complete = app_version_number + " " + app_version_stableness
'######### Some stuff that makes everthing work awesomely #########'
'change this for different builds of OpenProfile'
'######'
app_environment_build_type = "OpenProfile"
'######'

'###### OpenProfile ######'
if app_environment_build_type == "OpenProfile":
    app_environment_build_machine_type = "[Windows/Mac OSX/GNU-Linux]"
    app_environment_gui_enabled = "true"
'#################################'

'###### OpenProfile-lite ######'
if app_environment_build_type == "OpenProfile-lite":
    app_environment_build_machine_type = "[Windows/Mac OSX/GNU-Linux (lite)]"
    app_environment_gui_enabled = "false"
'#################################'

'###### OpenProfile-for-iOS ######'
if app_environment_build_type == "OpenProfile-for-iOS":
    app_environment_build_machine_type = "[iOS]"
    app_environment_gui_enabled = "false"
'#################################'

'End of awesome stuff'
'Next stage of awesome stuff'
if app_environment_gui_enabled == "true":
    'Imports the "tkinter" library"'
    import tkinter
'######### End of next stage awesome stuff #########'    
'Some GUI stuff'
app_gui_window_main_title = app_name + " v" + app_version_number + " (gui)"
app_gui_window_about_title = "About " + app_name
app_gui_window_main_size = "300x300"
app_gui_window_about_size = "300x250"
'End of GUI stuff'
app_orginization = "DeavmiOSS"
app_orginization_message = "This is free and open-source software from " + app_orginization + "."
app_description = app_name + " is a free and open-source easy to use autobiography and biography creator written in Python."
app_description_part1 = app_name + " is a free and open-source easy to use "
app_description_part2 = "autobiography and biography creator written in Python."
'Licensing stuff here'
app_license_url = "http://gnu.org/licenses/gpl.txt"
app_license = "GPLv3"
app_license_description = app_name + " is registered under " + app_license + "."
app_license_year = "2014"
app_license_startupmsg_line1 = app_name + " Copyright (C) " + app_license_year + " " + app_orginization
app_license_startupmsg_line2 = "This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'."
app_license_startupmsg_line3 = "This is free software, and you are welcome to redistribute it"
app_license_startupmsg_line4 = "under certain conditions; type `show c' for details."
'End licensing stuff'
app_info_online_site_url = "http://bit.ly/getopenprofile"
app_info_online_repository_url = "https://github.com/deavmi/OpenProfile"
app_info_online_feedback_url = "https//deavmi.github.io/OpenProfile/feedback"
app_info_online_wiki_url = "https://github.com/deavmi/OpenProfile/wiki"
app_ui_console_welcomemsg = "Welcome to " + app_name + "!"
'Getting everything referenced so that we can, "refer"-lol, to them when we need to a.k.a go to them-(the definitions)'
def exit():
    print()
    print("Thank you for using " + app_name + ".")
    exit
def about():
    print()
    print("-------------------------------------------------------")
    print("                      " + app_name)
    print("                   v" + app_version_complete)
    print()
    print(app_description_part1)
    print(app_description_part2)
    print()
    print(app_license_description)
    print()
    print(app_orginization_message)
    print()
    print("Below are some helpful links:")
    print()
    print("License: " + app_license_url)
    print("Project site: " + app_info_online_site_url)
    print("Wiki: " + app_info_online_wiki_url)
    print("Source code: " + app_info_online_repository_url)
    print("Feedback: " + app_info_online_feedback_url)
    print()
    commandline()
def credits():
    print()
    print("Credits of " + app_name + " v" + app_version_number + " .")
    print()
    print()
    'I wanted three back slahes but apprently you always have to add +1 to the amount of slahes any way two slahes is enough'
    print("\\\Developers")
    print()
    print("Deavmi - <http://bit.ly/thedeavmi>")
    print()
    print("\\\Graphics")
    print()
    print("Graphicsfuel - <http://www.graphicsfuel.com>")
    print()
    print("\\\Testers")
    print()
    print("Currently we do not have any testers, unless Travis-CI counts.")
    print()
    print("\\\ These sites helped")
    print()
    print("QuestionFor - <http://python.questionfor.info/q_python_60818.html>")
    print()
    print("\\\Special Thanks")
    print()
    print("GitHub - Thanks for your great hosting both repo and site. <http://github.com>")
    print("Travis-CI - Excellent build slaves continuously testing the code. <http://travis-ci.org>")
    print("All the people credited in the 'I-wantz-doges' project, you guys helped a lot <http://bit.ly/I-wantz-doges>")
    print()
    commandline()
def license():
    print()
    print(app_license_description)
    print()
    print("All information regarding the NO WARRANTY disclamier and the redistribution disclaimer can be found in the license file online.")
    print()
    print("Your copy of this license can be obtained here: " + app_license_url + " .")
    print()
    commandline()
def licenses():
    print()
    print("Below are the links to the licenses for all the things used in " + app_name + ":")
    print()
    print("To view " + app_name + "'s license type 'show c'.")
    print()
    print("Python Programming Language - <http://docs.python.org/3/license.html> (PSF LICENSE AGREEMENT)")
    print("20 Flat Icons - <http://www.graphicsfuel.com> (Free for commercial use)")
    print()
    commandline()
def changelog():
    'Must still put stuff here'
    print()
def help():
    print()
    print("Here are a list of commands that can be used in " + app_name_short + ".")
    print()
    print("about         Displays about info")
    print("about_gui     Displays about info in GUI mode")
    print("changelog     Displays info on how to get the changelog")
    print("credits       Displays credits")
    print("exit          Terminates the program")
    print("gui           Starts OpenProfile in GUI mode")
    print("help          Displays list of commands")
    print("license       Displays the " + app_name + " license")
    print("licenses      Displays all licenses")
    print("q             Universally used for quitting")
    print("restart       Restarts " + app_name)
    print("show c        Displays the " + app_name + " license")
    print("show w        Displays the " + app_name + " license")
    print("start         Starts OpenProfile opperation")
    print()
    commandline()
def finish_biography():
    print()
    print("Below is your biography that " + app_name + " just generated:")
    print()
def finish_autobiography():
    print()
    print("Below is your autobiography that " + app_name + " just generated:")
    print()
def begin():
    print()
    print("Please fill in the following, hit enter to confirm:")
    print()
    print("--- Personal details ---")
    print()
    str = input("Enter your first name: ")
    user_names_firstname = str
    str = input("Enter your middle name: ")
    user_names_middlename = str
    str = input("Enter your last name: ")
    user_names_lastname = str
    str = input("Enter your maiden name: ")
    user_names_maidenname = str    
    str = input("Enter your nickname: ")
    user_names_nickname = str
    str = input("Enter your age: ")
    user_time_age = str
    str = input("Enter the day of your birth (No. format): ")
    user_time_dateofbirth_day = str
    str = input("Enter the month of your birth (ABC format): ")
    user_time_dateofbirth_month = str
    str = input("Enter the year of your birth (No. format): ")
    user_time_dateofbirth_year = str
    print()
    print("--- Location details ---")
    print()
    str = input("Enter city of birth: ")
    user_location_cityofbirth = str
    str = input("Enter country of birth: ")
    user_location_countryofbirth = str
    str = input("Enter current postal code: ")
    user_location_cityofbirth = str
    str = input("Enter current city: ")
    user_location_city = str
    str = input("Enter current state/province: ")
    user_location_state = str
    str = input("Enter current country: ")
    user_location_country = str
    print()
    print("--- Interests & hobbies ---")
    print()
    str = input("List your interests (Comma format): ")
    user_interests_list = str
    'Not finished with all the Inputs and Outputs yet hay :P :D'
    print()
    print("Which one of the following would you like to generate?")
    print()
    print("1. Autobiography")
    print("2. Biography")
    if str == "1":
       finish_autobiography()
    if str == "2":
       finish_biography() 
def about_gui():
    print()
    print("Setting up the GUI...")
    print("Setting window name...")
    about = tkinter.Tk()
    print("Setting window names... [Done]")
    print("Setting window properties...")
    print("Setting window size...")
    about.geometry(app_gui_window_about_size)
    print("Setting window title...")
    about.title(app_gui_window_about_title)
    print("Setting window title... [Done]")
    print("Setting window properties... [Done]")
    print("Setting up the GUI... [Done]")
    print("Creating the window...")
    about.mainloop()
    print("Creating the window... [Done - Loop ended]")
    print()
    commandline()
    'This above module is not correct I think yet, IDK how I want it be.'
def gui():
    print()
    print("Setting up the GUI...")
    print("Setting window name...")
    main = tkinter.Tk()
    print("Setting window names... [Done]")
    print("Setting window properties...")
    print("Setting window size...")
    main.geometry(app_gui_window_main_size)
    print("Setting window title...")
    main.title(app_gui_window_main_title)
    print("Setting window title... [Done]")
    print("Setting window properties... [Done]")
    print("Setting up widgets...")
    'must finish this stuff here'
    label1_app_name = tkinter.Label(text=app_name)
    label2_app_version = tkinter.Label(text=app_version_complete)
    
    print("Setting up widgets... [Done]")
    print("Packing the widgets...")
    'image must be created and then packed here'
    label1_app_name.pack()
    label2_app_version.pack()
    print("Packing the widgets... [Done]")
    print("Setting up the GUI... [Done]")
    print("Creating the window...")
    main.mainloop()
    print("Creating the window... [Done - Loop ended]")
    print()
    commandline()
    'This above module is not correct I think yet, IDK how I want it be.'
def commandline():
    str = input(">>>")
    if str == "start":
        'Jump to the "begin" definition'
        begin()
    if str == "help":
        help()
    if str == "exit":
        exit()
    if str == "q":
        exit()
    if str == "about":
        about()
    if str == "about_gui":
        about_gui()
    if str == "credits":
        credits()
    if str == "show w":
        license()
    if str == "show c":
        license()
    if str == "license":
        license()
    if str == "licenses":
        licenses()
    if str == "restart":
        app_start()
    if str == "gui":
        gui()
    if str == "":
        commandline()
def app_start():
    print("-------------------------------------------------------")
    print(app_name + " v" + app_version_complete + " " + app_environment_build_machine_type)
    print(app_ui_console_welcomemsg)
    print("-------------------------------------------------------")
    print()
    print(app_license_startupmsg_line1)
    print(app_license_startupmsg_line2)
    print(app_license_startupmsg_line3)
    print(app_license_startupmsg_line4)
    print()
    print("Type 'start' to begin or 'help' for a list of commands.")
    print()
    commandline()
'This is continueing from "setting up strings" code, we are now going to jump into the definition called "app_start"'
app_start()
