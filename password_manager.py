# password manager
from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        
write_key()
'''


def load_key():
    file = open("password_manager\key.key", "rb")
    key = file.read()
    file.close()
    return key


# master_pswd = input('Please enter your master password: ')
key = load_key() # + master_pswd.encode()
fer = Fernet(key)


def view():
    with open('password_manager\password.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, pswd = data.split(' | ')
            print('Username: ' + user + ' | Password: ' + str(fer.decrypt(pswd.encode()).decode()))


def add():
    name = input('enter your username: ')
    pswd = input('enter your password: ')
    with open('password.txt', 'a') as f:
        f.write(name + ' | ' + fer.encrypt(pswd.encode()).decode() + '\n')


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
