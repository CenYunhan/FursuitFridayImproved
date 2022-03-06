import os


def downloadProvider(status=True):
    if status:
        if os.name == "nt" and os.path.exists("wget.exe"):
            if input("Found wget.Download?(y/n)") == "y":
                os.system("wget -P images -i URLs.txt")
            else:
                pass
        if os.name == "posix":
            code = os.system("wget -V")
            if code != 0:
                print("It seems you don't install wget.")
            elif input("Found wget.Download?(y/n)") == "y":
                os.system("wget -P images -i URLs.txt")

