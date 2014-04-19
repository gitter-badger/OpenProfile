'OpenProfile is a free and open-source easy to use autobiography and biography creator written in Python. Copyright (C) 2014 DeavmiOSS'
'Below we start setting up strings'
print("Please wait, the application is starting...")
print("Setting application strings...")
app_name = "OpenProfile"
app_name_short = "OP"
app_version_number = "1.4.2.0"
app_version_stableness = "pre-beta"
app_version_complete = app_version_number + " " + app_version_stableness
print("Setting application strings... [Done]")
'######### Configure your build of OpenProfile #########'
'######'
print(app_name + " build system is running...")
print(app_name + " build type is being set...")
'!!!!!!!!!!!! These are the only settings (below), so obviously change them if you need to !!!!!!!!!!!!'
app_environment_build_type = "OpenProfile"
'Below is for compatibility, because older version of Python want the user to use a captital "T" when importing tkinter.'
app_environment_build_tkinter_import_mode = "modern"
'Change this to "true" to enable logs inside the OpenProfile console.'
app_environment_log2console_enabled = "true"
'Change this to "true" to make OpenProfile start in GUI mode.'
print(app_name + " build type set to: " + app_environment_build_type)
'######'
print("Checking for the selected build type's enviroment...")
'Below are the different build types, their code is seperated by these "#"'
'###### OpenProfile ######'
if app_environment_build_type == "OpenProfile":
    print("Checking for the selected build type's enviroment... [Done]")
    print("Setting up the environemnt for the selected build type...")
    app_environment_build_machine_type = "[Windows/Mac OSX/GNU-Linux]"
    app_environment_gui_enabled = "true"
    print("Setting up the environemnt for the selected build type... [Done]")
'#################################'

'###### OpenProfile-lite ######'
if app_environment_build_type == "OpenProfile-lite":
    print("Checking for the selected build type's enviroment... [Done]")
    print("Setting up the environemnt for the selected build type...")
    app_environment_build_machine_type = "[Windows/Mac OSX/GNU-Linux (lite)]"
    app_environment_gui_enabled = "false"
    print("Setting up the environemnt for the selected build type... [Done]")
'#################################'

'###### OpenProfile-for-iOS ######'
if app_environment_build_type == "OpenProfile-for-iOS":
    print("Checking for the selected build type's enviroment... [Done]")
    print("Setting up the environemnt for the selected build type...")
    app_environment_build_machine_type = "[iOS]"
    app_environment_gui_enabled = "false"
    print("Setting up the environemnt for the selected build type... [Done]")
'#################################'

'End of awesome stuff'
'Next stage of awesome stuff'
print("Checking if the GUI needs to be enabled...")
if app_environment_gui_enabled == "true":
    'Sets up dat string'
    app_environment_gui_datword = "enabled"
    'Imports the "tkinter" library"'
    print("Checking if the GUI needs to be enabled... Yes")
    print("Checking the library import mode...")
    if app_environment_build_tkinter_import_mode == "modern":
        print("Library import mode has been set to: modern")
        print("Importing GUI library...")
        import tkinter
        print("Importing GUI library... [Done]")
    if app_environment_build_tkinter_import_mode == "old":
        print("Library import mode has been set to: old")
        print("Importing GUI library...")
        import Tkinter
        print("Importing GUI library... [Done]")
print(app_name + " build system is running... [Done]")    
'######### End of next stage awesome stuff #########'    
'Some GUI stuff'
print("Continueing setting application strings...")
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
print("Continueing setting application strings... [Done]")
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
    print("Walkman - <http://walkman100/github.io/Walkman>")
    print()
    print("\\\Developers + These sites and people helped")
    print()
    print("QuestionFor - <http://python.questionfor.info/q_python_60818.html>")
    print("My mom - <no info>")
    print("Stackoverflow - <http://stackoverflow.com/questions/11767867/greater-than-less-than-python>")
    print("Open Book Project - <http://www.openbookproject.net/thinkcs/python/english2e/ch04.html>")
    print()
    print("\\\Special thanks")
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
    if app_environment_gui_enabled == "true":
        app_strings_about_gui_help_string = "about_gui     Displays about info in GUI mode"
        app_strings_gui_help_string = "gui           Starts OpenProfile in GUI mode"
    if app_environment_gui_enabled == "false":
        app_strings_about_gui_help_string = "about_gui     Displays about info in GUI mode (Not available in this build type)"
        app_strings_gui_help_string = "gui           Starts OpenProfile in GUI mode (Not available in this build type)"
    print()
    print("Here are a list of commands that can be used in " + app_name_short + ".")
    print()
    print("about         Displays about info")
    print(app_strings_about_gui_help_string)
    print("changelog     Displays info on how to get the changelog")
    print("credits       Displays credits")
    print("exit          Terminates the program")
    print(app_strings_gui_help_string)
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
def begin():
    print()
    print("Please fill in the following, hit enter to confirm:")
    print()
    print("--- Personal details ---")
    print()
    user_names_firstname = input("Enter your first name: ")
    user_names_middlename = input("Enter your middle name: ")
    user_names_lastname = input("Enter your last name: ")
    str = input("Enter your maiden name: ")
    user_names_maidenname = str    
    user_names_nickname = input("Enter your nickname: ")
    user_time_ager = input("Enter your age: ")
    user_time_dateofbirth_day = input("Enter the day of your birth (No. format): ")
    user_time_dateofbirth_monthr = input("Enter the month of your birth (ABC format): ")
    user_time_dateofbirth_yearr = input("Enter the year of your birth (No. format): ")
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
    print("--- Work ---")
    str = input("What is your current job: ")
    user_work_currentjob = str
    str = input("List your previous jobs (Comma format): ")
    user_work_previousjobs_list = str
    print("--- Interests & hobbies ---")
    print()
    str = input("List your interests (Comma format): ")
    user_interests_list = str
    print()
    print("Just completing some cool things...")
    'If the person is below the age of 13, he is considered a kid/child (thanks mom ;P)'
    if user_time_age < "13":
        user_time_age_type  = "kid"
    'For all the ages below consider the person a teenager (thanks mom ;P, again)'
    if user_time_age == "13":
        user_time_age_type = "teenager"
    if user_time_age == "14":
        user_time_age_type = "teenager"
    if user_time_age == "15":
        user_time_age_type = "teenager"
    if user_time_age == "16":
        user_time_age_type = "teenager"
    if user_time_age == "17":
        user_time_age_type = "teenager"
    if user_time_age == "18":
        user_time_age_type = "teenager"
    if user_time_age == "19":
        user_time_age_type = "teenager"
    'For all the ages above 19, the person is considered an adult (thanks mom, ;P, lol, again) P.S I know, grandparents/people are not included'
    if user_time_age > "19":
        user_time_age_type = "adult"
    'Not finished with all the Inputs and Outputs yet hay :P :D'
    print()
    print("Below is your autobiography that " + app_name + " just generated:")
    print()
    'Put stuff here'
    print()
    print("-------------------------------------------------------")
    print()
    print("Below is your autobiography that " + app_name + " just generated:")
    print()
    'Put stuff here'
    commandline()
def about_gui():
   if app_environment_gui_enabled == "true":
       print("-------------------------------------------------------")
       print("The gui has been " + app_environment_gui_datword + " for your build type.")
       print("Build type: " + app_environment_build_type)
       print("Tkinter import mode: " + app_environment_build_tkinter_import_mode)
       print("-------------------------------------------------------")
       print()
       print("Setting up the GUI...")
       print("Setting window name...")
       about = tkinter.Tk()
       print("Setting window names... [Done]")
       print("Setting window properties...")
       print("Setting window size...")
       about.geometry(app_gui_window_about_size)
       print("Setting window size... [Done]")
       print("Setting window title...")
       about.title(app_gui_window_about_title)
       print("Setting window title... [Done]")
       print("Setting window properties... [Done]")
       print("Setting up the GUI... [Done]")
       print("Creating the window...")
       about.mainloop()
       print("Creating the window... [Done - Loop ended]")
   if app_environment_gui_enabled == "false":
       print("-------------------------------------------------------")
       print("The gui has been " + app_environment_gui_datword + " for your build type.")
       print("Build type: " + app_environment_build_type)
       print("Tkinter import mode: " + app_environment_build_tkinter_import_mode)
       print("-------------------------------------------------------")
   print()
   commandline()
def gui():
    if app_environment_gui_enabled == "true":
       print("-------------------------------------------------------")
       print("The gui has been " + app_environment_gui_datword + " for your build type.")
       print("Build type: " + app_environment_build_type)
       print("Tkinter import mode: " + app_environment_build_tkinter_import_mode)
       print("-------------------------------------------------------")
       print()
       print("Setting up the GUI...")
       print("Setting window name...")
       main = tkinter.Tk()
       print("Setting window names... [Done]")
       print("Setting window properties...")
       print("Setting window size...")
       main.geometry(app_gui_window_main_size)
       print("Setting window size... [Done]")
       print("Setting window title...")
       main.title(app_gui_window_main_title)
       print("Setting window title... [Done]")
       print("Setting window properties... [Done]")
       print("Setting up widgets...")
       'must finish this stuff here'
       label1_app_name = tkinter.Label(text=app_name)
       label2_app_version = tkinter.Label(text=app_version_complete)
       button1_get_started = tkinter.Button(text="Get Started", command=begin)
       button2_about = tkinter.Button(text="About " + app_name, command=about_gui)
       button3_quit = tkinter.Button(text="Quit " + app_name, command=exit)
       print("Setting up widgets... [Done]")
       print("Packing the widgets...")
       'image must be created and then packed here'
       label1_app_name.pack()
       label2_app_version.pack()
       button1_get_started.pack()
       button2_about.pack()
       button3_quit.pack()
       print("Packing the widgets... [Done]")
       print("Setting up the GUI... [Done]")
       print("Creating the window...")
       main.mainloop()
       print("Creating the window... [Done - Loop ended]")
    if app_environment_gui_enabled == "false":
       print("-------------------------------------------------------")
       print("The gui has been " + app_environment_gui_datword + " for your build type.")
       print("Build type: " + app_environment_build_type)
       print("Tkinter import mode: " + app_environment_build_tkinter_import_mode)
       print("-------------------------------------------------------")  
    print()
    commandline()
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
