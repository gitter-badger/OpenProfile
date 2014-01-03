'Doing the imports'
import tkinter
'Below we start setting up strings'
app_name = "OpenProfile"
app_name_short = "OP"
app_version_number = "1.0.0.5"
app_version_stableness = "pre-beta"
app_version_complete = app_version_number + " " + app_version_stableness
app_company = "DeavmiOSS"
app_description = app_name + " is a free and open-source easy to use autobiography and biography creator written in Python."
app_description_part1 = app_name + " is a free and open-source easy to use "
app_description_part2 = "autobiography and biography creator written in Python."
app_license_url = "http://gnu.org/licenses/gpl.txt"
app_license = app_name + " is registered under GPLv3"
app_info_online_site_url = "http://bit.ly/getopenprofile"
app_info_online_repository_url = "https://github.com/deavmi/OpenProfile"
app_info_online_feedback_url = "https//deavmi.github.io/OpenProfile/feedback"
app_ui_console_welcomemsg = "Welcome to " + app_name + "!"
'Getting everything referenced so that we can, "refer"-lol, to them when we need to a.k.a go to them-(the definitions)'
def exit():
    print()
    print("Thank you for using " + app_name + ".")
    exit
def about():
    print()
    print("---------------------------------------------------")
    print("                    " + app_name)
    print("                 v" + app_version_complete)
    print()
    print(app_description_part1)
    print(app_description_part2)
    print()
    print(app_license)
    print()
    print("Below are some helpful links:")
    print()
    print("License: " + app_license_url)
    print("Project site: " + app_info_online_site_url)
    print("Source code: " + app_info_online_repository_url)
    print("Feedback: " + app_info_online_feedback_url)
def help():
    print()
    print("Here are a list of commands that can be used in " + app_name_short + ".")
    print()
    print("about         Displays about info")
    print("credits       Displays credits")
    print("exit          Terminates the program")
    print("help          Displays list of commands")
    print("licenses      Displays licenses")
    print("start         Starts OpenProfile opperation")
    print("q             Universally used for quitting")
    print("(return)      Also universally used for quitting")
    print()
    str = input()
    if str == "":
        app_start()
    if str == "q":
        app_start()
def finish_biography():
    print()
    print("")
def finish_autobiography():
    print()
    print("")
def begin():
    print()
    print("")
def app_start():
    print("---------------------------------------------------")
    print(app_name + " v" + app_version_complete)
    print(app_ui_console_welcomemsg)
    print("---------------------------------------------------")
    print()
    print("Type 'start' to begin or 'help' for help.")
    print()
    str = input(">>>")
    if str == "start":
        'Jump to the "begin" definition'
        begin()
    if str == "help":
        help()
    if str == "exit":
        exit()
    if str == "about":
        about()
'This is continueing from "setting up strings" code, we are now going to jump into the definition called "app_start"'
app_start()
