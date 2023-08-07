import os
import time as wait
import datetime
import configparser

def runLUL():
    lf = configparser.ConfigParser()

    lf.read('user.inf')

    # get body
    body = lf['Account']

    # get user
    usr = body['Username']

    # get password
    passw = body['Password']

    # run
    dt = datetime.datetime.now().strftime('%H:%M:%S')
    run(user=usr, password=passw, time=dt)

def verifyLastLogin():
    if os.path.exists('user.inf'):
        runLUL()
    else:
        startup()

def run(user, password, time):
    print('Welcome ' + user + '!')
    time_day = str(time)
    user_save = str(user)
    pass_save = str(password)
    command = input('mbkb:~ ' + user + '$ ')
    if 'echo' in command:
        comando_6 = command.replace('echo ', '')
        print(comando_6)
        run(user=user, password=password, time=time)
    if 'ping' in command:
        comando_7 = command.replace('ping ', '')
        os.system('ping ' + comando_7)
        run(user, password, time)
    if command == 'time':
        print('Time: ' + time_day)
        print()
        run(user=user, password=password, time=time)
    if command == 'cmd':
        os.startfile('cmd')
        exit()
    if command == 'save':
        print('Saving your account...')
        lt = configparser.ConfigParser()

        lt.add_section('Account')
        lt.set('Account', 'Username', user_save)
        lt.set('Account', 'Password', pass_save)

        with open('user.inf', "w") as usersavel:
            lt.write(usersavel)
        print('Success!')
        run(user=user_save, password=pass_save, time=time_day)
    if command == 'sudo dtrace -w -n panic':
        password_request = input('Password: ')
        if password_request == password:
           os.system('cls')
           print()
           print('-----------------')
           print('[               ]')
           print('[       X       ]')
           print('[               ]')
           print('-----------------')
           print('Ú | _____________')
           print('-----------------')
           print('     iPC 99      ')
           print('-----------------')
           print()
           print('0xB74447, 0xC')
           print('0x9B6G22, 0x99BCA')
           print()
           print('To quit this screen please wait.')
           wait.sleep(3)
           os.system('cls')
           verifyLastLogin()
        if password_request != password:
            print('Invalid password.')
            print()
            run(user=user, password=password, time=time)
    if command == 'whoami':
       print('User: ' + user + ', Password: ' + password)
       print()
       print('If you do want to change your password type: passwd <password>')
       print('If you do want to change your username type: userwd <user>')
       print()
       run(user, password, time)
    if 'cat' in command:
        comando_9 = command.replace('cat ', '')

        with open(comando_9, 'r') as file:
            content = file.read()
            print(content)
            run(user, password, time)
    if 'passwd' in command:
       command_3 = command.replace('passwd ', '')
       password = command_3
       run(user, password, time)
    if 'userwd' in command:
        command_4 = command.replace('userwd ', '')
        user = command_4
        run(user, password, time)
    if command == 'help':
        print()
        print('EduardoBash, v3.0 help')
        print('--------------------------')
        print('Commands:                 ')
        print('help, this list.          ')
        print('userwd <user>, changes the username, change <user> to your name.')
        print('passwd <password>, changes your password, change <password> to your password.')
        print('whoami, prints the running user and password.')
        print('sudo, execute as root')
        print('clear, clears the screen.')
        print('time, prints the time.')
        print('start <app>, starts an aplication, change <app> for your full file location.')
        print('shutdown, close the app.')
        print('cat <file>, prints the content of any file. change <file> to your file path.')
        print('echo <say>, prints anything to user, chnage <say> to anything to print.')
        print('ping <site>, ping and return result to the user, change <site> to pinging ip or site.')
        print('cmd, open cmd')
        print('save, save your account in "user.inf" file. usage, after closed you can return to your user on open BashOS.')
        print()
        run(user=user, password=password, time=time)
    if command == 'clear':
         os.system('cls')
         run(user=user, password=password, time=time)
    if 'start' in command:
        app = command.replace('start ', '')
        os.startfile(app)
        run(user=user, password=password, time=time)
    if command == 'exit':
        exit()
    if command == 'sudo':
        print('Usage: sudo <command> [OPTION] <argument>')
        print()
        print('<command> dtrace, [OPTION] -w -n <argument> panic, desc: kernel panic')
        print()
        print('If any command have "none" into <argument> or [OPTION], not put nothing')
        run(user=user, password=password, time=time)

    else:
        print('Invalid command.')
        run(user=user, password=password, time=time)        
        
def startup():
    print('Welcome to Darwin!')
    print('If you do want help type: help, after login')
    print()
    print('Create your account:')
    user = input('Username: ')
    password = input('Password: ')
    print()
    print('Running at: /usr/' + user + '/env/')
    print()
    date = datetime.datetime.now().strftime('%H:%M:%S')
    run(user=user, password=password, time=date)

verifyLastLogin()