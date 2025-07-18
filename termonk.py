import subprocess
import platform
from colorama import init, Fore, Style
import toolList as ts

init()

class Termonk:
    def listCategory(catList):
        print(f"{Fore.RED}\n[+] .... Categories .... [+]{Style.RESET_ALL}")
        num = 0
        for i in catList:
            print(f"{Fore.CYAN}\n[{num}] {i}{Style.RESET_ALL}")
            num += 1
        catNum = input(f"{Fore.RED}\n[+] Select Category: {Style.RESET_ALL}")

        Termonk.selectCategory(catNum)

    def listTools(lists):
        if platform.system() == "Windows":
            subprocess.run(["cls"], shell=True)
        else:  # For Linux, macOS, and other Unix-like systems
            subprocess.run(["clear"], shell=True)
        banner()
        tool = []
        print(f"{Fore.RED}\n[+] .... Tools .... [+]{Style.RESET_ALL}")
        num = 1
        for i in lists:
            print(f"{Fore.CYAN}\n[{num}] {i}{Style.RESET_ALL}")
            num += 1

        try:    
            toolNum = int(input(f"{Fore.RED}\n[+] Select Tool: {Style.RESET_ALL}"))
            tool.append(toolNum)
        except:
            print(f"{Fore.RED}\n[-] Select One Tool [-]{Style.RESET_ALL}")
            subprocess.run("exit", shell=True)

        try:
            ind = toolNum - 1
            tool.append(lists[ind])
        except:
            print(f"{Fore.RED}\n[-] Invalid Choice [-]{Style.RESET_ALL}")
            subprocess.run("exit", shell=True)
        if ind <= len(lists):
            Termonk.installTool(tool)



    def installTool(tool):
        try:
            subprocess.run(["apt", "install", tool[1], "-y"], check=True, capture_output=True, text=True)
            print(f"{Fore.GREEN}\n[+] .... {tool[1]} installed successfully .... [+]{Style.RESET_ALL}")
            print(f"{Fore.GREEN}\n Run the tool: {Fore.LIGHTGREEN_EX} {tool[1]} -h {Style.RESET_ALL}")
        except subprocess.CalledProcessError as e:
            print(f"{Fore.RED}\n{tool[1]} installation failed: {e.stderr}{Style.RESET_ALL}")

    def selectCategory(catNum):
        if catNum == '0':
            subprocess.run("exit", shell=True)
            print(f"{Fore.RED}\n[-] .... END .... [-]{Style.RESET_ALL}")

        elif catNum == '1':
            return Termonk.listTools(ts.essential)
        elif catNum == '2':
            return Termonk.listTools(ts.networking)
        elif catNum == '3':
            return Termonk.listTools(ts.programming)
        elif catNum == '4':
            return Termonk.listTools(ts.development)
        elif catNum == '5':
            return Termonk.listTools(ts.text)
        elif catNum == '6':
            return Termonk.listTools(ts.compression)
        elif catNum == '7':
            return Termonk.listTools(ts.security)
        elif catNum == '8':
            return Termonk.listTools(ts.database)
        elif catNum == '9':
            return Termonk.listTools(ts.remote)
        elif catNum == '10':
            return Termonk.listTools(ts.file)
        elif catNum == '11':
            return Termonk.listTools(ts.terminal)
        elif catNum == '12':
            return Termonk.listTools(ts.vcs)
        elif catNum == '13':
            return Termonk.listTools(ts.system)
        elif catNum == '14':
            return Termonk.listTools(ts.misc)
        elif catNum == '15':
            return Termonk.listTools(ts.pypackage)
        elif catNum == '16':
            return Termonk.listTools(ts.media)
        elif catNum == '17':
            return Termonk.listTools(ts.gui)
        elif catNum == '18':
            return Termonk.listTools(ts.games)
        elif catNum == '19':
            return Termonk.listTools(ts.nethack)
        else:
            print(f"{Fore.RED}\n[-] Invalid Choice [-]{Style.RESET_ALL}")
            subprocess.run("exit", shell=True)


def banner():
    banner = r"""
 _____  _____ ____  _      ____  _      _  __
/__ __\/  __//  __\/ \__/|/  _ \/ \  /|/ |/ /
  / \  |  \  |  \/|| |\/||| / \|| |\ |||   / 
  | |  |  /_ |    /| |  ||| \_/|| | \|||   \ 
  \_/  \____\\_/\_\\_/  \|\____/\_/  \|\_|\_\
    """
    print()
    print()
    print(f"{Fore.LIGHTRED_EX}{banner}{Style.RESET_ALL}")
    print()
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT} [+]  GitHub     :  PavinDas{Style.RESET_ALL}")
    print(f"{Fore.LIGHTRED_EX}{Style.BRIGHT} [+]  Instagram  :  pavin__das{Style.RESET_ALL}")
    print()

if __name__ == "__main__":
    banner()

    # ! Catergory List
    catList = open("catList.txt","r")

    if platform.system() == "Windows":
        subprocess.run(["cls"], shell=True)
    else:  # For Linux, macOS, and other Unix-like systems
        subprocess.run(["clear"], shell=True)
    Termonk.listCategory(catList)
