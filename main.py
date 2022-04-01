# WebSafer is designed and coded by Isaiah Stanke
# it is used to block websites for any reason from
# opening on one's computer. Note: This tool does
# not block the website for every vister, nor
# everyone on the network. Only for the single
# user the program is ran on!!! It will loopback
# to 127.0.0.1 automatically

from lib2to3.pytree import convert
from colorama import Fore, Style, init
import shutil
import os
import ctypes
import time
import os.path
from os.path import exists
from pathlib import Path
from icmplib import ping, multiping

# this script doesn't work on Linux/Mac, so if we detect it's being ran on one of those then tell them and exit the script!
if os.name in ('Linux', 'linux', 'linux2', 'Darwin', 'darwin'):
    print(f"{Fore.GREEN} THIS SCRIPT DOES NOT WORK ON LINUX/MAC!!! EXITING NOW")
    time.sleep(5)
    exit()


# detect what OS their using and depending on what then use the right command to clear the console
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)

# the script only works in elevated CMD's so this is to check if the user is running it in one
def isAdmin():
    try:
        is_admin = (os.getuid() == 0)
    except:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    return is_admin

if isAdmin():
    print(f"{Fore.GREEN} This script only works in an elevated CMD, please run this script again in an elevated CMD. Exiting now...")
    time.sleep(5)
    exit()

clearConsole()

# have to call this for colorama *ugh*
init(convert=True)


# ALRIGHT LOOK - I just needed it to be recursive
def maywork():
    # just clearing the terminal to provide better aesthetics and not be so confusing
    clearConsole()

    # made it into a function in order to have cleaner code, didn't want to write all of it out every single time
    def logo():
        print(" ")
        print(
            f"{Fore.RED}///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}// {Fore.GREEN}| {Fore.RED}//////////////////// {Fore.GREEN}| {Fore.RED}//// {Fore.GREEN}|=============== {Fore.RED}//// {Fore.GREEN}|==============|{Fore.RED} ////////{Fore.GREEN} |=============== {Fore.RED}/////////////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}// {Fore.GREEN}| {Fore.RED}//////////////////// {Fore.GREEN}| {Fore.RED}//// {Fore.GREEN}|{Fore.RED} /////////////////// {Fore.GREEN}|{Fore.RED} ////////////{Fore.GREEN} |{Fore.RED} ////////{Fore.GREEN} | {Fore.RED}////////////////////////////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}// {Fore.GREEN}| {Fore.RED}//////////////////// {Fore.GREEN}| {Fore.RED}//// {Fore.GREEN}| {Fore.RED}/////////////////// {Fore.GREEN}|==============|{Fore.RED} ////////{Fore.GREEN} |=============== {Fore.RED}/////////////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}// {Fore.GREEN}| {Fore.RED}//////////////////// {Fore.GREEN}| {Fore.RED}//// {Fore.GREEN}|=============== {Fore.RED}//// {Fore.GREEN}|{Fore.RED} //////////////////////////////////////{Fore.GREEN} | {Fore.RED}/////////////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}// {Fore.GREEN}| {Fore.RED}////////{Fore.GREEN} | {Fore.RED}/////////{Fore.GREEN} | {Fore.RED}//// {Fore.GREEN}| {Fore.RED}///////////////////{Fore.GREEN} |==============|{Fore.RED} ////////{Fore.GREEN} |=============== {Fore.RED}///{Fore.GREEN}.....{Fore.RED}/////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}/// {Fore.GREEN}\{Fore.RED}  /////{Fore.GREEN}  | {Fore.RED}///////{Fore.GREEN}  / {Fore.RED}/////{Fore.GREEN} | {Fore.RED}/////////////////// {Fore.GREEN}| {Fore.RED}////////////{Fore.GREEN} | {Fore.RED}////////{Fore.GREEN} | {Fore.RED}//////////////////{Fore.GREEN}.....{Fore.RED}/////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}//// {Fore.GREEN}\________|_________/ {Fore.RED}////// {Fore.GREEN}|=============== {Fore.RED}//// {Fore.GREEN}|==============| {Fore.RED}////////{Fore.GREEN} |=============== {Fore.RED}///{Fore.GREEN}.....{Fore.RED}/////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////{Style.RESET_ALL}")
        print(
            f"{Fore.RED}///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////{Style.RESET_ALL}\n")

        print("WebSafer is designed and coded by Isaiah Stanke. " +
              "It is used to block websites for any reason from\n" +
              "opening on one's computer. Note: This tool does " +
              "not block the website for every vister, nor\n" +
              "everyone on the network. Only for the single " +
              "user the program is ran on!!! It will loopback\n" +
              "to 127.0.0.1 automatically and throws in variations like www, .com, .edu, etc. Please report\nbugs on " +
              f"the repo! We are not responsible for damage to any system files\n")

    logo()
    # giving main menu option and made it global
    global choice
    choice = input("1) Block website 2) Restore original host file 3) Exit ")

    # this is a huge if statment, depending on what was chosen then it brances into sub menu's and etc.
    if choice == "1":

        print("\nYou chose to block a website\n")

        # WE LOVE BEING DYNAMIC!
        var = os.path.dirname(os.path.abspath(__file__))
        target1 = os.path.join(var, "hosts")
        file_exists = exists(target1)
        print("Checking if you've ran this program already and made a copy to avoid overwrite...\n")

        # if the hosts file copy already exists in this directory then skip it to avoid overwrite
        if file_exists:

            input("Copy of original hosts file already exists, press Enter to continue...")
            clearConsole()

        # if a copy doesn't exist then make a copy
        else:

            print("No copy found...making a copy\n")
            global original5
            # location of hosts file and naming it original
            original5 = r"%s\System32\drivers\etc\hosts" % (os.environ['windir'],)

            # this is to be dynamic, it get's the path of the current file being ran to store the copy in since every user is different
            var2 = os.path.dirname(os.path.abspath(__file__))
            # use is to copy the hosts file as a backup, shutil.copy(*path of file*, *target location of copy file*)
            shutil.copy(original5, var2)

            time.sleep(3)

            input("Copy made, press Enter to continue...")

            clearConsole()

        logo()

        # taking input of what website to be blocked
        val2 = input("Input website to block (e.g. facebook *do not add any .com, etc. it will be added later*): ")

        # I put this in a try except statement as a fail safe, if the try fails then it's a permissions error
        try:

            # making them global

            global str1
            global str2
            global str3
            global str4
            global str5
            global str6

            # defining most commonly used suffix's and prefixes
            www = "www."
            net = ".net"
            org = ".org"
            com = ".com"
            xyz = ".xyz"
            edu = ".edu"
            gov = ".gov"
            inn = ".in"

            # combining original input and variations
            str1 = www + val2 + com
            str2 = val2 + net
            str3 = val2 + org
            str4 = val2 + xyz
            str5 = val2 + edu
            str6 = val2 + gov
            str7 = val2 + inn

            hostnames = [str1, str2, str3, str4, str5, str6, str7]

            # open the hosts file
            f2 = open(original5, 'a')

            def host_up(hostname: str):
                host = ping(hostname, count=5, interval=0.2)
                return host.packets_sent == host.packets_received

            print("\n")
            for host in hostnames:
                try:
                    if host_up(host):
                        print(f"Writing {host} as it is up!\n")
                        f2.write(f" 127.0.0.1 {host}")
                except:
                    print(f"{host} is not up so not writing it to the file!\n")

            # closing file
            f2.close()
        except:
            # look at top of try block to understand this
            print(
                "\nThere was an error writing to the hosts file, most likely permissions. Make sure to run the CMD as admin with the right permissions")
            time.sleep(8)
            maywork()

        choiccc = input("1) Move forward 2) Add customized domain ")
        if choiccc == "1":
            print("\nGoing forward...")
        elif choiccc == "2":
            clearConsole()
            logo()
            print("\nYou chose to add a customized website\n")

            def customized():
                f3 = open(original5, 'a')
                custo = input("\nPlease enter the customized domain name: ")
                f3.write(f" 127.0.0.1 {custo}")
                print(f"\nWrote {custo} to file")
                repeat = input("\n1) Add another customized domain 2) Continue on ")
                if repeat == "1":
                    customized()
                else:
                    print("\nGoing on...")
                    time.sleep(5)

            customized()
        clearConsole()

        logo()

        # after all is said and done then show these to user, made it a function to call it in the bottom else statment
        def vals():

            clearConsole()
            logo()
            global val3
            val3 = input("1) Return to main menu 2) Exit this program ")
            clearConsole()

            if val3 == "1":
                # if chosen to return to main menu call it's own function
                maywork()
            elif val3 == "2":

                logo()
                # this just exiting, it doesn't do any cleaning. lol
                print("Cleaning and exiting...")
                time.sleep(5)
                exit()
            else:
                # if user inputted invalid choice then show them that and call it's own function
                logo()
                print("\nChoice not valid. Please try again")
                time.sleep(5)
                vals()

        # calling above function..found to be very important
        vals()

    elif choice == "2":

        print("\nYou chose to restore the original host file\n")
        time.sleep(2)

        # checking if file exists in order to make copy
        var5 = os.path.dirname(os.path.abspath(__file__))
        var6 = os.path.join(var5, "hosts")
        file_exists = exists(var6)

        # if it does then run this code...
        if file_exists:

            print("Copy found! Replacing now...\n")

            # location of now editied hosts file
            location = r"%s\System32\drivers\etc\hosts" % (os.environ['windir'],)

            # getting homepath to be dynamic
            var7 = os.path.dirname(os.path.abspath(__file__))
            var8 = os.path.join(var7, "hosts")
            shutil.copy(var8, location)

            time.sleep(5)

            print("File has been restored!\n")

            val4 = input("1) Return to main menu 2) Exit this program ")

            if val4 == "1":
                maywork()
                clearConsole()
            else:

                clearConsole()
                logo()

                print("Cleaning and exiting...")
                time.sleep(5)
                exit()

        else:

            print("Copy/File not found! Have you ran this program before? Defaulting back to main menu...")
            time.sleep(5)
            clearConsole()
            maywork()

    elif choice == "3":
        clearConsole()
        logo()
        print("Cleaning and exiting...")
        time.sleep(5)
        exit()
    else:
        clearConsole()
        logo()
        print("Input not valid, please try again")
        time.sleep(5)
        maywork()


maywork()
