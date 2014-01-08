'Doing the imports'
import tkinter
'Below we start setting up strings'
app_name = "OpenProfile"
app_name_short = "OP"
app_version_number = "1.0.2.5"
app_version_stableness = "pre-beta"
app_version_complete = app_version_number + " " + app_version_stableness
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
app_license_url = "http://gnu.org/licenses/gpl.txt"
app_license = "GPLv3"
app_license_description = app_name + " is registered under " + app_license + "."
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
    print("\\\Special Thanks")
    print()
    print("GitHub - Thanks for your great hosting both repo and site. <http://github.com>")
    print("Travis-CI - Excellent build slaves continuously testing the code. <http://travis-ci.org>")
    print("All the people credited in the 'I-wantz-doges' project, you guys helped a lot <http://bit.ly/I-wantz-doges>")
    print()
    commandline()
def licenses():
    print()
    print(app_license_description)
    print()
    commandline()
def help():
    print()
    print("Here are a list of commands that can be used in " + app_name_short + ".")
    print()
    print("about         Displays about info")
    print("credits       Displays credits")
    print("exit          Terminates the program")
    print("gui           Starts OpenProfile in GUI mode")
    print("help          Displays list of commands")
    print("licenses      Displays licenses")
    print("q             Universally used for quitting")
    print("restart       Restarts " + app_name)
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
    str = input("Enter your nickname: ")
    user_names_nickname = str
    str = input("Enter your age: ")
    user_time_age = str
    str = input("Enter your date of birth (DD/MM/YYYY): ")
    user_time_dateofbirth = str
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
    print("Setting up the GUI... [Done]")
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
    if str == "credits":
        credits()
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
    print(app_name + " v" + app_version_complete)
    print(app_ui_console_welcomemsg)
    print("-------------------------------------------------------")
    print()
    print("Type 'start' to begin or 'help' for a list of commands.")
    print()
    commandline()
'This is continueing from "setting up strings" code, we are now going to jump into the definition called "app_start"'
app_start()
