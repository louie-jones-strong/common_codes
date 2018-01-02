import easygui

def file_picker(address = ""):
    if address == "":
        output = easygui.fileopenbox()
    else:
        output = easygui.fileopenbox(address)
    return output

def folder_picker(address = ""):
    if address == "":
        output = easygui.diropenbox()
    else:
        output = easygui.diropenbox(address)
    return output

def msgbox(msg="(Your message goes here)", title="popup", ok_button="OK"):
    easygui.msgbox( msg=msg , title=title , ok_button=ok_button )
    return