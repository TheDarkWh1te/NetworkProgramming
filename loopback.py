

def chosefunc();
    print('ChooseFunc')
def HostName():
    print('HOSTNAME')
    
def ShowRun():
    print('SHOWRUN')

def ConfigPrints():
    print('CONFIGPRINTS')

def CompFile():
    print('COMPFILE')

def CompPrint():
    print('COMPPRINT')

def NewInt():
    print('NewINTERFACE')

def NewProto():
    print('PROTOCOL')




def main():
    #choose fun is in a closed loop as the user will need to either choose Telnet or SSH at program launch and that wont change unless the user quits out of the connection type
    chosefunc()
    while True:
        print('----CONNECTION ESTABLISHED .......')
        print('    Please select an option    ')
        print('-------------------------------')
        print('1. Change hostname')
        print('2. Show running config')
        print('3. Compare Start & running config')
        print('4. Configure new interface')
        print('5. Configre new protocol \n')
        print('enter q or Q to exit')
        OP = input('Option: ')
        if OP == 1:   #Hostname OP
            HostName()
        elif OP == 2: #Show Run OP
            ShowRun()
        elif OP == 3: #Comp Start Run OP
            ConfigPrints()
            CompFile()
            CompPrint()

        elif OP == 4: #Conf New Int OP
            NewInt()
        elif OP == 5: #Conf New Proto OP
            NewProto()
        elif OP == q or OP == Q: #Quit
            print('Exiting program')
            session.sendline('exit')
            exit()
        else: 
            print('Incorrect input please try again ')
        
        
        


    
    
main()
