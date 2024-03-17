# password manager

master_pswd = input('Please enter your master password: ')

def view():
    with open('password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, paswd = data.split(' | ')
            print('Username: ' + user + ' | Password: ' + paswd)


def add():
    name = input('enter your username: ')
    pswd = input('enter your password: ')
    with open('password.txt', 'a') as f:
        f.write(name + ' | ' + pswd + '\n')


while True:
    action = input('Would you like to view or add a new password(view/add/q): ').lower()
    if action == 'q':
        break
    elif action == 'view':
        view()
    elif action == 'add':
        add()
    else:
        print('invalid argument bruh :/')
        continue