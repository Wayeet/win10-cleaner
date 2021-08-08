import os, time
import admin
import glob
import winshell
import shutil




#C:\Users\email\AppData\Local\Temp
#C:\$Recycle.Bin
#C:\Windows\SoftwareDistribution


print("The following folders will be cleared and permanently deleted:")
print("")
print("Bin")
print("Temp-Folder")
print("SoftwareDistrubition (Update-Files)")
print("")
print("Do you want continue? Y/N")

x = input()


if x == "N" or x == "n":
    print("Exiting with 0 errors")
    exit()
elif x == "Y" or x == "y":
    print("Starting...")
    try:
        winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)

    except:
        print("Bin is empty")

    print("--> Temp")
    path = "C:/Users/email/AppData/Local/Temp"
    t = os.listdir(path)
    for i in t:
        try:
            try:
                os.remove(path+"/"+i)
            except:
                shutil.rmtree(path+"/"+i)
        except:
            os.removedirs(path+"/"+i)

    print("Finsihed Temp Folder")

