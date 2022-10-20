#!/bin/python3
def process():
    ## Your text here
    text="""em iu anh<3
iu anh rat nhieu<3"""
    ## Main process
    shell = win32com.client.Dispatch("WScript.Shell")
    for line in text.splitlines():
        for character in [char for char in line]:
            shell.SendKeys(character)
            sleep(0.1)
        shell.SendKeys("{ENTER}")
        sleep(0.7)
    return 0
def clear():
    if (name=='nt'):
        system('cls')
    else:
        system('clear')
if (__name__=='__main__'):
    timeout=5
    from os import system,name
    from time import sleep
    from sys import stdout,exit
    try:
        import win32com.client
        from pyperclip import copy,paste
    except:
        if (name=='nt'):
            system("python -m pip install pyperclip pypiwin32")
        else:
            system("python3 -m pip install pyperclip pypiwin32")
        from pyperclip import copy,paste
        import win32com.client
    try:
        clear()
        print("\nVừa ấn vô đây đúng hong=))")
        sleep(1.5)
        print("\nQuay trở lại đoạn chat với anh rồi đợi {0}s có điều bất ngờ đó em=))\n".format(str(timeout)))
        sleep(1)
        for i in range(int(timeout),-1,-1):
            sleep(1)
            print("{0}... ".format(str(i)),end="")
            stdout.flush()
        print()
        process()
        exit()
    except KeyboardInterrupt:
        print("\n\nĐừng ấn [Ctrl + C] nữa, đang thoát nè:<")
        exit()