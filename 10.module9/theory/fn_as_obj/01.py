def show_me():
    print('Kari')
def show_other():
    print('New')
menu ={
    1:show_me,
    2:show_other    
}

while True:
    choice = int(input('Your choice>>>>'))
    menu[choice]()