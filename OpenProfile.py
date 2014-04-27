'OpenProfile is a free and open-source easy to use autobiography and biography creator written in Python. Copyright (C) 2014 DeavmiOSS'
'Below we start setting up strings'
print("Please wait, the application is starting...")
print("Setting application strings...")
class AppInfo:
    name = "OpenProfile"
    name_short = "OP"
    version_number = "1.4.2.0"
    version_phase = "pre-beta"
    version_all = version_number + " " + version_phase
    orginization = "DeavmiOSS"
    orginization_message = "This is free, gratis and open-source software from " + orginization + "."
    description = name + " is a free, gratis and open-source easy to use autobiography and biography creator written in Python."
    description_part1 = name + " is a free, gratis and open-source easy to use "
    description_part2 = "autobiography and biography creator written in Python."
    'Licensing stuff here'
    license_url = "http://gnu.org/licenses/gpl.txt"
    license = "GPL v3"
    license_description = name + " is registered under " + license + "."
    license_year = "2014"
    license_startupmsg_line1 = name + " Copyright (C) " + license_year + " " + orginization
    license_startupmsg_line2 = "This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'."
    license_startupmsg_line3 = "This is free software, and you are welcome to redistribute it"
    license_startupmsg_line4 = "under certain conditions; type `show c' for details."
    'End licensing stuff'
    'Changelog stuff'
    changelog = "https://deavmi.github.io/OpenProfile/changelog.txt"
    'End of changelog stuff'
    site = "http://bit.ly/getopenprofile"
    repository = "https://github.com/deavmi/OpenProfile"
    feedback = "mailto:tristankildaire@gmail.com"
    wiki = "https://github.com/deavmi/OpenProfile/wiki"
class BuildConfig:
    '##### User build preferences to be changed according to your preference #####'
    build_type = "OpenProfile"
    'Below is for compatibility, because older version of Python want the user to use a captital "T" when importing tkinter.'
    build_tkinter_import_mode = "modern"
    'Change this to "true" to make OpenProfile start in GUI mode.'
    build_auto_gui = "false"
    '##### Do not chnage the below #####'
    build_machine_type = ""
    gui_enabled = ""
class Misc:
    generation_option = ""
    generation_complete = ""
class Person:
    'Thanks redditors and learnpython.org!'
print("Setting application strings... [Done]")
print("Creating objects...")
app = AppInfo()
buildconfig = BuildConfig()
misc = Misc()
person = Person()
print("Creating object... [Done]")
'######### Configure your build of OpenProfile #########'
'######'
print(app.name + " build system is running...")
print(app.name + " build type is being set...")
print(app.name + " build type set to: " + buildconfig.build_type)
'######'
print("Checking for the selected build type's environment...")
'Below are the different build types, their code is seperated by these "#"'
'###### OpenProfile-system ######'
if buildconfig.build_type == "OpenProfile":
    print("Checking for the selected build type's environment... [Done]")
    print("Setting up the environment for the selected build type...")
    buildconfig.build_machine_type = "[Windows/Mac OSX/GNU-Linux]"
    buildconfig.gui_enabled = "true"
    print("Setting up the environment for the selected build type... [Done]")
'#################################'

'###### OpenProfile-lite-system ######'
if buildconfig.build_type == "OpenProfile-lite":
    print("Checking for the selected build type's environment... [Done]")
    print("Setting up the environment for the selected build type...")
    buildconfig.build_machine_type = "[Windows/Mac OSX/GNU-Linux (lite)]"
    buildconfig._gui_enabled = "false"
    print("Setting up the environment for the selected build type... [Done]")
'#################################'

'###### OpenProfile-for-iOS-system ######'
if buildconfig.build_type == "OpenProfile-for-iOS":
    print("Checking for the selected build type's environment... [Done]")
    print("Setting up the environment for the selected build type...")
    buildconfig.build_machine_type = "[iOS]"
    buildconfig.gui_enabled = "false"
    print("Setting up the environment for the selected build type... [Done]")
'#################################'

'End of awesome stuff'
'Next stage of awesome stuff'
print("Checking if the GUI needs to be enabled...")
if  buildconfig.gui_enabled == "true":
    'Sets up dat string'
    app_environment_gui_datword = "enabled"
    'Imports the "tkinter" library"'
    print("Checking if the GUI needs to be enabled... Yes")
    print("Checking the library import mode...")
    if  buildconfig.build_tkinter_import_mode == "modern":
        print("Library import mode has been set to: modern")
        print("Importing GUI library...")
        import tkinter
        print("Importing GUI library... [Done]")
    if  buildconfig.build_tkinter_import_mode == "old":
        print("Library import mode has been set to: old")
        print("Importing GUI library...")
        import Tkinter
        print("Importing GUI library... [Done]")
print(app.name + " build system is running... [Done]")
'######### End of next stage awesome stuff #########'
'Getting everything referenced so that we can, "refer"-lol, to them when we need to a.k.a go to them-(the definitions)'
def exit():
    print()
    print("Thank you for using " + app.name + ".")
    exit
def about():
    print()
    print("-------------------------------------------------------")
    print("                      " + app.name)
    print("                   v" + app.version_all)
    print()
    print(app.description_part1)
    print(app.description_part2)
    print()
    print(app.license_description)
    print()
    print(app.orginization_message)
    print()
    print("Below are some helpful links:")
    print()
    print("License: " + app.license_url)
    print("Project site: " + app.site)
    print("Wiki: " + app.wiki)
    print("Source code: " + app.repository)
    print("Feedback: " + app.feedback)
    print()
    commandline()
def credits():
    print()
    print("Credits of " + app.name + " v" + app.version_number + " .")
    print()
    print()
    'I wanted three back slashes but apprently you always have to add +1 to the amount of slashes any way two slahes is enough'
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
    print(app.license_description)
    print()
    print("All information regarding the NO WARRANTY disclamier and the redistribution disclaimer can be found in the license file online.")
    print()
    print("Your copy of this license can be obtained here: " + app.license_url + " .")
    print()
    commandline()
def licenses():
    print()
    print("Below are the links to the licenses for all the things used in " + app.name + ":")
    print()
    print("To view " + app.name + "'s license type 'show c'.")
    print()
    print("Python Programming Language - <http://docs.python.org/3/license.html> (PSF LICENSE AGREEMENT)")
    print("20 Flat Icons - <http://www.graphicsfuel.com> (Free for commercial use)")
    print()
    commandline()
def changelog():
    print()
    print("View the changelog here: " + app.changelog)
    print()
def help():
    if  buildconfig.gui_enabled == "true":
        app_strings_about_gui_help_string = "about_gui     Displays about info in GUI mode"
        app_strings_gui_help_string = "gui           Starts OpenProfile in GUI mode"
    if  buildconfig.gui_enabled == "false":
        app_strings_about_gui_help_string = "about_gui     Displays about info in GUI mode (Not available in this build type)"
        app_strings_gui_help_string = "gui           Starts OpenProfile in GUI mode (Not available in this build type)"
    print()
    print("Here are a list of commands that can be used in " + app.name_short + ".")
    print()
    print("about         Displays about info")
    print(app_strings_about_gui_help_string)
    print("changelog     Displays info on how to get the changelog")
    print("credits       Displays credits")
    print("exit          Terminates the program")
    print(app_strings_gui_help_string)
    print("help          Displays list of commands")
    print("license       Displays the " + app.name + " license")
    print("licenses      Displays all licenses")
    print("q             Universally used for quitting")
    print("restart       Restarts " + app.name)
    print("show c        Displays the " + app.name + " license")
    print("show w        Displays the " + app.name + " license")
    print("start         Starts OpenProfile operation")
    print()
    commandline()
def begin():
    print()
    print("Please fill in the following, hit enter to confirm:")
    print()
    print("--- Personal details ---")
    print()
    person.names_firstname = input("Enter your first name: ")
    person.names_middlename = input("Enter your middle name: ")
    person.names_lastname = input("Enter your last name: ")
    person.names_maidenname = input("Enter your maiden name: ")
    person.names_nickname = input("Enter your nickname: ")
    person.time_age = input("Enter your age: ")
    person.time_dateofbirth_day = input("Enter the day of your birth (No. format): ")
    person.time_dateofbirth_month = input("Enter the month of your birth (ABC format): ")
    person.time_dateofbirth_year = input("Enter the year of your birth (No. format): ")
    print()
    print("--- Location details ---")
    print()
    person.location_cityofbirth = input("Enter city of birth: ")
    person.location_countryofbirth = input("Enter country of birth: ")
    person.location_postalcode = input("Enter current postal code: ")
    person.location_city = input("Enter current city: ")
    person.locationr = input("Enter current state/province: ")
    person.location_countryr = input("Enter current country: ")
    print()
    print("--- Work ---")
    person.work_currentjob = input("What is your current job: ")
    person.work_previousjobs_list = input("List your previous jobs (Comma format): ")
    print("--- Interests & hobbies ---")
    print()
    person.interests_list = input("List your interests (Comma format): ")
    'If the person is below the age of 13, he is considered a kid/child (thanks mom ;P)'
    if person.time_age < "13":
        person.time_age_type = "kid"
    'For all the ages below consider the person a teenager (thanks mom ;P, again)'
    if person.time_age == "13":
        person.time_age_type = "teenager"
    if person.time_age == "14":
        person.time_age_type = "teenager"
    if person.time_age == "15":
        person.time_age_type = "teenager"
    if person.time_age == "16":
        person.time_age_type = "teenager"
    if person.time_age == "17":
        person.time_age_type = "teenager"
    if person.time_age == "18":
        person.time_age_type = "teenager"
    if person.time_age == "19":
        person.time_age_type = "teenager"
    'For all the ages above 19, the person is considered an adult (thanks mom, ;P, lol, again) P.S I know, grandparents/people are not included'
    if person.time_age > "19":
        person.time_age_type = "adult"
    misc.generation_complete == "true"
    'Jump to the mode selection definition'
    mode()
def mode():
    print()
    print("1. Autobiography")
    print("2. Biography")
    print("3. Both of the above")
    misc.generation_option = input("Which would you like to generate (Mode selection): ")
    if misc.generation_option == "1":
        autobiography()
    if misc.generation_option == "2":
        biography()
    if misc.generation_option == "3":
        autobiography()
    commandline()
def autobiography():
    print()
    print("-------------------------------------------------------")
    print()
    print("Below is your autobiography that " + app.name + " just generated:")
    print()
    'Put stuff here'
    if misc.generation_option == "3":
        biography()
def biography():
    print()
    print("-------------------------------------------------------")
    print()
    print("Below is your biography that " + app.name + " just generated:")
    print()
    'Put stuff here'
    commandline()
def about_gui():
   if app_environment_gui_enabled == "true":
       print("-------------------------------------------------------")
       print("The gui has been " + app_environment_gui_datword + " for your build type.")
       print("Build type: " + buildconfig.build_type)
       print("Tkinter import mode: " + app_environment_build_tkinter_import_mode)
       print("-------------------------------------------------------")
       print()
       print("Setting up the GUI...")
       print("Setting window name...")
       about = tkinter.Tk()
       print("Setting window names... [Done]")
       print("Setting window properties...")
       print("Setting window size...")
       about.geometry("300x300")
       print("Setting window size... [Done]")
       print("Setting window title...")
       about.title("About " + app.name)
       print("Setting window title... [Done]")
       print("Setting window properties... [Done]")
       print("Setting up the GUI... [Done]")
       print("Creating the window...")
       about.mainloop()
       print("Creating the window... [Done - Loop ended]")
   if app_environment_gui_enabled == "false":
       print("-------------------------------------------------------")
       print("The gui has been " + app_environment_gui_datword + " for your build type.")
       print("Build type: " + buildconfig.build_type)
       print("Tkinter import mode: " + app_environment_build_tkinter_import_mode)
       print("-------------------------------------------------------")
   print()
   commandline()
def gui():
    if app_environment_gui_enabled == "true":
       print("-------------------------------------------------------")
       print("The gui has been " + app_environment_gui_datword + " for your build type.")
       print("Build type: " + buildconfig.build_type)
       print("Tkinter import mode: " + app_environment_build_tkinter_import_mode)
       print("-------------------------------------------------------")
       print()
       print("Setting up the GUI...")
       print("Setting window name...")
       main = tkinter.Tk()
       print("Setting window names... [Done]")
       print("Setting window properties...")
       print("Setting window size...")
       main.geometry("300x300")
       print("Setting window size... [Done]")
       print("Setting window title...")
       main.title(app.name)
       print("Setting window title... [Done]")
       print("Setting window properties... [Done]")
       print("Setting up widgets...")
       'must finish this stuff here'
       label1_app_name = tkinter.Label(text=app.name)
       label2_app_version = tkinter.Label(text=app.version_all)
       button1_get_started = tkinter.Button(text="Get Started", command=begin)
       button2_about = tkinter.Button(text="About " + app.name, command=about_gui)
       button3_quit = tkinter.Button(text="Quit " + app.name, command=exit)
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
       print("Build type: " + buildconfig.build_type)
       print("Tkinter import mode: " + app_environment_build_tkinter_import_mode)
       print("-------------------------------------------------------")  
    print()
    commandline()
def commandline():
    user_input = input(">>>")
    if user_input == "start":
        'Jump to the "begin" definition'
        begin()
    if user_input == "help":
        help()
    if user_input == "exit":
        exit()
    if user_input == "q":
        exit()
    if user_input == "about":
        about()
    if user_input == "about_gui":
        about_gui()
    if user_input == "credits":
        credits()
    if user_input == "show w":
        license()
    if user_input == "show c":
        license()
    if user_input == "license":
        license()
    if user_input == "licenses":
        licenses()
    if user_input == "restart":
        app_start()
    if user_input == "gui":
        gui()
    if user_input == "":
        commandline()
    if user_input == "generate":
        if misc.generation_complete = "true":
            mode()
        if misc.generation_complete = "false":
            print("No data collected. Cannot generate.")
def app_start():
    print("-------------------------------------------------------")
    print(app.name + " v" + app.version_all + " " +  buildconfig.build_machine_type)
    print("Welcome to " + app.name)
    print("-------------------------------------------------------")
    print()
    print(app.license_startupmsg_line1)
    print(app.license_startupmsg_line2)
    print(app.license_startupmsg_line3)
    print(app.license_startupmsg_line4)
    print()
    print("Type 'start' to begin or 'help' for a list of commands.")
    print()
    if buildconfig.build_auto_gui == "true":
        print("Autostart GUI is enabled, starting the GUI...")
        gui()
    commandline()
'This is continuing from "setting up strings" code, we are now going to jump into the definition called "app_start"'
app_start()