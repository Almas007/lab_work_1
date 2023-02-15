import os

print('Welcome to Command Prompt created by Python')
command = 'The commands bellow available for you \n' \
          '- dir list of files/folders \n' \
          '- cd + folder_name: enter the file \n' \
          '- cd .. go back one folder \n' \
          '- create + folder_name: creates folder with specified name \n' \
          '- delete + folder_name: deletes folder with specified name \n' \
          '- rename + folder_name to new_folder_name: renames folder with specified name \n' \
          '- open + file_name: opens file with specified name \n' \
          '- close: close the cmd'
cmd = True
print(command)
path = 'C:/'
while cmd:
    cmd = str(input(f'Please enter the command bellow \n'
                    f'{path}>'))
    if cmd == 'dir':
        list = os.listdir(path)
        print('The current folder contains ...')
        for i in list:
            print(i)
    elif cmd.startswith('cd '):
        try:
            cd, folder = cmd.split()
        except:
            print('incorrect command')
            continue
        try:
            os.listdir(path + folder + '/')
            path = path + folder + '/'
        except:
            print('Folder does not exist')
            continue
    elif cmd.startswith('create '):
        try:
            cd, folder = cmd.split()
        except:
            print('incorrect command')
            continue
        os.mkdir(path+folder)
        print(f'New folder {folder} was created')
    elif cmd.startswith('delete '):
        try:
            cd, folder = cmd.split()
        except:
            print('incorrect command')
            continue
        try:
            os.rmdir(path + folder)
            print(f'folder {folder} was deleted')
        except:
            print('folder does not exist')
            continue
    elif cmd.startswith('rename '):
        try:
            cd, folder, to, newfolder = cmd.split()
        except:
            print('incorrect command')
            continue
        try:
            os.rename(path+folder, path+newfolder)
        except:
            print('The folder does not exist')
            continue
        print(f'The folder {folder} was renamed to {newfolder}')
    elif cmd.startswith('open '):
        try:
            cd, folder = cmd.split()
        except:
            print('incorrect command')
            continue
        try:
            folder = str(folder)
            f = open(path+folder, "r")
            for i in f:
                print(i)
            f.close()
        except:
            print('File does not exist')
    elif cmd == 'close':
        cmd = False
    else:
        print("Incorrect command")