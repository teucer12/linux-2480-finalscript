import subprocess, sys

def maker(filename):
    subprocess.call(["touch",filename])
    print("Created" + filename)
    return
def remover(filename):
    yesno = input("Are you sure you want to delete "+filename+"? ")
    if yesno != "y":
        exit()
    else:
        subprocess.call(["rm",filename])
    return

if len(sys.argv) > 1:
    if str(sys.argv[1]) == "maker":
        newfile = input("What filename would you like to make?")
        maker(newfile)
    elif str(sys.argv[1]) == "remover":
        oldfile = input ("What filename would you like to remove?")
        remover(oldfile)
else:
    print("Try running this script with <maker> or <remover> as an argument")