'OpenProfile is a free and open-source easy to use autobiography and biography creator written in Python. Copyright (C) 2014 DeavmiOSS'
import subprocess
import tkinter
'Below we start setting up strings'
print("[Startup] Please wait, the application is starting...")
class AppInfo:
    version_number = "1.0.0.0"
    orginisation = "DeavmiOSS"
    orginisation_message = "This is free, gratis and open-source software from " + orginisation + "."
    description = "OpenProfile" + " is a free, gratis and open-source easy to use autobiography and biography creator written in Python."
    description_part1 = "OpenProfile" + " is a free, gratis and open-source easy to use "
    description_part2 = "autobiography and biography creator written in Python."
    'Licensing stuff here'
    license_url = "https://gnu.org/licenses/gpl.txt"
    license = "GPL v3 or above."
    license_description = "OpenProfile" + " is licensed under " + license + "."
    license_startupmsg_line2 = "This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'."
    license_startupmsg_line3 = "This is free software, and you are welcome to redistribute it"
    license_startupmsg_line4 = "under certain conditions; type `show c' for details."
    'End licensing stuff'
    'Changelog stuff'
    changelog = "https://deavmi.github.io/OpenProfile/changelog.txt"
    'End of changelog stuff'
    site = "http://bit.ly/getopenprofile"
    repository = "https://github.com/deavmi/OpenProfile"
    feedback = "https://github.com/deavmi/OpenProfile/issues/new"
    wiki = "https://github.com/deavmi/OpenProfile/wiki"
class Misc:
    generation_option = ""
    generation_complete = ""
    cli_line = "-------------------------------------------------------"
class Person:
    'Thanks to redditors and people at learnpython.org!'
app = AppInfo()
misc = Misc()
person = Person()
'Getting everything referenced so that we can, "refer"-lol, to them when we need to a.k.a go to them-(the definitions)'
def exit():
    print()
    print("Thank you for using " + "OpenProfile" + ".")
def about():
    print()
    print(misc.cli_line)
    print("                      " + "OpenProfile")
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
    print("Credits of " + "OpenProfile" + " v" + app.version_number + " .")
    print()
    print()
    'I wanted three back slashes but apprently you always have to add +1 to the amount of slashes any way two slashes is enough'
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
    print("Below are the links to the licenses for all the things used in " + "OpenProfile" + ":")
    print()
    print("To view " + "OpenProfile" + "'s license type 'show c'.")
    print()
    print("Python Programming Language - <http://docs.python.org/3/license.html> (PSF LICENSE AGREEMENT)")
    print("20 Flat Icons - <http://www.graphicsfuel.com> (Free for commercial use)")
    print()
    commandline()
def changelog():
    print()
    print("View the changelog here: " + app.changelog + " .")
    print()
def help():
    if  buildconfig.gui_enabled == "true":
        misc.gui_about_string = "about_gui     Displays about info in GUI mode"
        misc.gui_help_string = "gui           Starts OpenProfile in GUI mode"
    else:
        misc.gui_about_string = "about_gui     Displays about info in GUI mode (Not available in this build type)"
        misc.gui_help_string = "gui           Starts OpenProfile in GUI mode (Not available in this build type)"
    print()
    print("Here are a list of commands that can be used in " + "OpenProfile"_short + ".")
    print()
    print("about         Displays about info")
    print(misc.gui_about_string)
    print("changelog     Displays info on how to get the changelog")
    print("credits       Displays credits")
    print("exit          Terminates the program")
    print(misc.gui_help_string)
    print("help          Displays list of commands")
    print("license       Displays the " + "OpenProfile" + " license")
    print("licenses      Displays all licenses")
    print("q             Universally used for quitting")
    print("restart       Restarts " + "OpenProfile")
    print("show c        Displays the " + "OpenProfile" + " license")
    print("show w        Displays the " + "OpenProfile" + " license")
    print("start         Starts OpenProfile operation")
    print()
    print("For more information visit online 'https://github.com/deavmi/OpenProfile/wiki/Commands'")
    print()
    commandline()
def begin():
    print()
    print("Please fill in the following, hit enter to confirm:")
    print()
    print("--- Personal details ---")
    print()
    person."OpenProfile"s_first"OpenProfile" = input("Enter your first "OpenProfile": ")
    person."OpenProfile"s_middle"OpenProfile" = input("Enter your middle "OpenProfile": ")
    person."OpenProfile"s_last"OpenProfile" = input("Enter your last "OpenProfile": ")
    person."OpenProfile"s_maiden"OpenProfile" = input("Enter your maiden "OpenProfile": ")
    person."OpenProfile"s_nick"OpenProfile" = input("Enter your nick"OpenProfile": ")
    person.time_age = input("Enter your age: ")
    person.time_dateofbirth_day = input("Enter the day of your birth (No. format): ")
    person.time_dateofbirth_month = input("Enter the month of your birth (ABC format): ")
    person.time_dateofbirth_year = input("Enter the year of your birth (No. format): ")
    print()
    print("--- Location details ---")
    print()
    person.location_cityofbirth = input("Enter city of birth: ")
    person.location_stateofbirth = input("Enter state/province of birth: ")
    person.location_countryofbirth = input("Enter country of birth: ")
    person.location_postalcode = input("Enter current postal code: ")
    person.location_city = input("Enter current city: ")
    person.location_state = input("Enter current state/province: ")
    person.location_country = input("Enter current country: ")
    print()
    print("--- Work ---")
    person.work_currentjob = input("What is your current job: ")
    person.work_previousjobs_list = input("List your previous jobs (Comma format): ")
    print("--- Interests & hobbies ---")
    print()
    person.interests_list = input("List your interests (Comma format): ")
    'If the person is below the age of 13, he is considered a kid/child (thanks mom ;P)'
    if person.time_age < "13": person.time_age_type = "kid"
    'For all the ages below consider the person a teenager (thanks mom ;P, again)'
    elif person.time_age == "13": person.time_age_type = "teenager"
    elif person.time_age == "14": person.time_age_type = "teenager"
    elif person.time_age == "15": person.time_age_type = "teenager"
    elif person.time_age == "16": person.time_age_type = "teenager"
    elif person.time_age == "17": person.time_age_type = "teenager"
    elif person.time_age == "18": person.time_age_type = "teenager"
    elif person.time_age == "19": person.time_age_type = "teenager"
    'For all the ages above 19, the person is considered an adult (thanks mom, ;P, lol, again) P.S I know, grandparents/people are not included'
    elif person.time_age > "19": person.time_age_type = "adult"
    misc.generation_complete == "true"
    'Jump to the mode selection definition'
    mode()
def mode():
    print()
    print("1. Autobiography")
    print("2. Biography")
    print("3. Basic info")
    print("4. Contact info")
    print("5. All of the above")
    print()
    print("For more information visit online 'https://github.com/deavmi/OpenProfile/wiki/Generation-modes'")
    print()
    misc.generation_complete == "true"
    misc.generation_option = input("Which would you like to generate (Mode selection): ")
    if misc.generation_option == "1": autobiography()
    elif misc.generation_option == "2": biography()
    elif misc.generation_option == "3":  basicinfo()
    elif misc.generation_option == "4": contactinfo()
    elif misc.generation_option == "5": autobiography()
    else:
        print("Invalid generation option selected!")
        mode()
    commandline()
def autobiography():
    print()
    print(misc.cli_line)
    print()
    print("Below is your autobiography that " + "OpenProfile" + " just generated:")
    print()
    print("My "OpenProfile" is " + person."OpenProfile"s_first"OpenProfile" + person."OpenProfile"s_middle"OpenProfile" + person."OpenProfile"s_maiden"OpenProfile" + person."OpenProfile"s_last"OpenProfile")
    print("but most people call me " + person."OpenProfile"s_nick"OpenProfile" + ". I am a " + person.time_age + " year old " + person.time_age_type)
    print("that was born in " + person.location_cityofbirth + ", " + person.location_stateofbirth + ", " + person.location_countryofbirth + " in " +  person.time_dateofbirth_day + "/" +  person.time_dateofbirth_month + "/" +  person.time_dateofbirth_year + ".")
    print("I currently live in " + person.location_city + ", " + person.location_state + ", " + person.location_country + ".")
    'Put stuff here'
    if misc.generation_option == "4": biography()
    commandline()
def biography():
    print()
    print(misc.cli_line)
    print()
    print("Below is your biography that " + "OpenProfile" + " just generated:")
    print()
    'Put stuff here'
    if misc.generation_option == "4": basicinfo()
    commandline()
def basicinfo():
    print()
    print(misc.cli_line)
    print()
    print("Below is your basic info that " + "OpenProfile" + " just generated:")
    print()
    print("Basic Info")
    print()
    print("First"OpenProfile": " + person."OpenProfile"s_first"OpenProfile")
    print("Middle"OpenProfile": " + person."OpenProfile"s_middle"OpenProfile")
    print("Maiden"OpenProfile": " + person."OpenProfile"s_maiden"OpenProfile")
    print("Last"OpenProfile": " + person."OpenProfile"s_last"OpenProfile")
    print("Nick"OpenProfile": " + person."OpenProfile"s_nick"OpenProfile")
    print("Age: " + person.time_age)
    print("Date of birth: " +  person.time_dateofbirth_day + "/" +  person.time_dateofbirth_month + "/" +  person.time_dateofbirth_year)
    print("Current location: " + person.location_city + ", " + person.location_state + ", " + person.location_country)
    'Put stuff here'
    if misc.generation_option == "4": contactinfo()
    commandline()
def contactinfo():
    print()
    print(misc.cli_line)
    print()
    print("Below is your conatct info that " + "OpenProfile" + " just generated:")
    print()
    print("Conatct info:")
    'Put stuff here'
    commandline()
def export_to_text():
    'Work in progress...'
    export_file"OpenProfile" = input("Enter the file"OpenProfile" to export as: ")
    print("Exporting to '" + export_file"OpenProfile" + "' ...")
    subprocess.Popen("echo " + person.rendered + " > " + export_file"OpenProfile")
    print("Exported successfully!")
def about_gui():
   if buildconfig.gui_enabled == "true":
       print(misc.cli_line)
       print("The gui has been " + buildconfig.gui_datword + " for your build type.")
       print("Build type: " + buildconfig.build_type)
       print("Tkinter import mode: " + buildconfig.build_tkinter_import_mode)
       print(misc.cli_line)
       print()
       print("Setting up the GUI...")
       about = tkinter.Tk()
       about.geometry("300x300")
       about.title("About " + "OpenProfile")
       print("Setting up the GUI... [Done]")
       print("Creating the window...")
       about.mainloop()
       print("Creating the window... [Done - Loop ended]")
   else:
       print(misc.cli_line)
       print("The gui has been " + buildconfig.gui_datword + " for your build type.")
       print("Build type: " + buildconfig.build_type)
       print("Tkinter import mode: " + buildconfig.build_tkinter_import_mode)
       print(misc.cli_line)
   print()
   commandline()
def gui():
    if buildconfig.gui_enabled == "true":
       print(misc.cli_line)
       print("The gui has been " + buildconfig.gui_datword + " for your build type.")
       print("Build type: " + buildconfig.build_type)
       print("Tkinter import mode: " + buildconfig.build_tkinter_import_mode)
       print(misc.cli_line)
       print()
       print("Setting up the GUI...")
       main = tkinter.Tk()
       main.geometry("300x300")
       main.title("OpenProfile")
       'must finish this stuff here'
       label1_app_OpenProfile = tkinter.Label(text="OpenProfile")
       label2_app_version = tkinter.Label(text=app.version_all)
       button1_get_started = tkinter.Button(text="Get Started", command=begin)
       button2_about = tkinter.Button(text="About " + "OpenProfile", command=about_gui)
       button3_quit = tkinter.Button(text="Quit " + "OpenProfile", command=exit)
       'image must be created and then packed here'
       label1_app_OpenProfile.pack()
       label2_app_version.pack()
       button1_get_started.pack()
       button2_about.pack()
       button3_quit.pack()
       print("Setting up the GUI... [Done]")
       print("Creating the window...")
       main.mainloop()
       print("Creating the window... [Done - Loop ended]")
    else:
       print(misc.cli_line)
       print("The gui has been " + buildconfig.gui_datword + " for your build type.")
       print("Build type: " + buildconfig.build_type)
       print("Tkinter import mode: " + buildconfig.build_tkinter_import_mode)
       print(misc.cli_line)
    print()
    commandline()
def commandline():
    user_input = input(">>>")
    if user_input == "start": begin()
    elif user_input == "help": help()
    elif user_input == "exit" or user_input == "q": exit()
    elif user_input == "about": about()
    elif user_input == "about_gui": about_gui()
    elif user_input == "credits": credits()
    elif user_input == "show w" or user_input == "show c" or unser_input == "license": license()
    elif user_input == "licenses": licenses()
    elif user_input == "restart": app_start()
    elif user_input == "gui": gui()
    elif user_input == "": commandline()
    elif user_input == "generate_info":
        if misc.generation_complete == "true": mode()
        else: print("No data collected. Cannot generate.")
    else:
        print("Unknown command '" + user_input + "'")
        commandline()
def app_start():
    print(misc.cli_line)
    print("OpenProfile" + " v" + app.version_all + " " +  buildconfig.build_machine_type)
    print("Welcome to OpenProfile!")
    print(misc.cli_line)
    print()
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