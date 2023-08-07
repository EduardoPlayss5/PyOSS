import atexit
import os
import time
import colorama
from colorama import Fore, Back, Style

# Importante! Chame a função init do colorama para habilitar a formatação ANSI
colorama.init()

# Restaurar as configurações de estilo ao fechar o programa
def reset_style_on_exit():
    print(Style.RESET_ALL)

atexit.register(reset_style_on_exit)

# Limpa a tela do terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


# importing the kernel files
import commands.kernel.process as processF
import commands.kernel.run as runF
import commands.kernel.runApp as runAppF
import commands.kernel.cat as catF

# (others) kernel bsod file
import commands.kernel.bsod as bsodF

# importing the apps
import commands.apps.ping as pingF
import commands.apps.emual as emualF

def RunProcess():
    print('Type process code. Type "Stop" to finsh program code and run.')
    code_lines = []
    while True:
        line = input()
        if line.strip() == 'Stop':
            break
        code_lines.append(line)

        process_code = '\n'.join(code_lines)
        processF.execute_process(process=process_code)

def RunCmd():
    print('Type anything to run (can be: commands or apps): ')
    cmd = input()
    runF.start(code=cmd)

def RunAppFromFile():
    print('Enter the app path: ')
    app_pth = input('>>> ')
    runAppF.run_app(app_filename=app_pth)

# startup codes
def show_home_screen():
    clear_screen()
    print(Fore.LIGHTGREEN_EX + Back.BLACK)
    print("#########################################")
    print("#                                       #")
    print("#    Welcome to PyOSS v1.7 System!      #")
    print("#                                       #")
    print("#########################################")
    print(Style.RESET_ALL)

def main():
    show_home_screen()
    print("PyOSS v1.7 - beta")
    print()
    
    while True:
        command = input("user@pyoss1:~$ ").strip()

        if command == 'RunProcess':
           RunProcess()
        elif command == 'Run':
             RunCmd()
        elif 'echo' in command:
            full = command.replace('echo ', '')
            print(full)
        elif command == 'RunApp':
             RunAppFromFile()
        elif command == 'cls':
            clear_screen()
        elif 'cat' in command:
            print('Enter the file path: ')
            fn = input(">>> ")
            catF.catFile(fn)
        elif command == 'bserr':
            print('Enter the blue screen error: ')
            txt = input()
            bsodF.display(error=txt)
            clear_screen()
            main()
        elif command == 'start':
            print('Enter the file path to start: ')
            fn = input()
            os.startfile(fn)
        elif 'ping' in command:
            print('Site or host to ping: ')
            hip = input(">>> ")
            pingF.start(address=hip)
        elif command == 'emual':
            osid = input('Operating system id (1-BashOS,2-cancel): ')
            vn = f'{osid}'
            emualF.vm(id=vn)
        elif command == 'help':
            print('PyOSS v1.7 help')
            print()
            print('cls, clear screen')
            print('RunApp, run a app')
            print('Run, run a command')
            print('RunProcess, run a process, more than 1 line but runs only on specifc format.')
            print('shutdown <arg>, close or restart system.')
            print('cat, show the content of an file')
            print('echo <say>, print something')
            print('bserr, get a bsod (blue screen of death)')
            print('start, start an app')
            print('emual, emulate a operating system in python')
        elif 'shutdown' in command:
             full_args = command.replace('shutdown ', '')
             if full_args == '-r':
                clear_screen()
                main()
             elif full_args == '-s':
                print('Shutting down PyOSS!')
                time.sleep(4)
                break
             else:
               print('Usage: shutdown <arg>')
               print()
               print('Args: ')
               print('<arg> -r, restart')
               print('<arg> -s, close')
               print()
        else:
            print(Fore.LIGHTRED_EX + Back.BLACK + "Bad command or argument")
            print(Style.RESET_ALL)

    print(Style.RESET_ALL)
if __name__ == "__main__":
    main()