import os
import sys
import time

def summarymethod(name, versionvar, packformat, packdescription):
    return f""" ------------------------------------
    Thanks for using Autoz Texture pack creator:
    Here's a summary of your experience :)
    1. Name of your pack: {name}
    2. Native Pack version: {versionvar}
    3. Pack format version: {packformat}
    4. Pack description: {packdescription}"""

def getcwd(name):
    return f"""
Where your texture pack template is located:
{os.getcwd()}\\{name}"""

def clear_console():
    os.system('cls')

def helpsc():
    helpscreen = """Color Codes:
    &0 = Black
    &1 = Dark_Blue
    &2 = Dark_Green
    &3 = Dark_Aqua
    &4 = Dark_Red
    &5 = Dark_Purple
    &6 = Gold
    &7 = Grey
    &8 = Dark_Grey
    &9 = Blue
    &a = Green
    &b = Teal
    &c = Red
    &d = Light_Purple
    &e = Yellow
    &f = White
    Obfuscated = &k
    Bold = &l
    Strikethrough = &m
    Underline = &n
    Italic = &o
    Reset = &r"""
    return helpscreen

def loadinganimation():
    animation = ["⢿", "⣻", "⣽", "⣾", "⣷", "⣟", "⡿"]

    # Loop that creates animation
    for i in range(len(animation)):
        time.sleep(0.15)
        sys.stdout.write("\r" + "[!] Loading... " + animation[i % len(animation)])
        sys.stdout.flush()

    # Finsished text
    sys.stdout.write("\n" + "[✔] Finished!")

def endingmessage(name):
    print(f"""
If you had any trouble with this tool please DM me on discord :) IGN: Autozoneyt
Please be aware this is my first tool! Good luck with {name}""")


