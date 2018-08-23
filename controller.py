# LFSR Simulator
# controller.py
# Created by Mauro J. Pappaterra on 23 of August 2018.

# MAIN PROGRAM METHOD / START SCREEN
def start(m,v):

    exit = False
    while (not exit):
        print (v.welcome)
        exit = main_menu(m,v)
    print(v.exit)

# MAIN MENU
def main_menu (m,v):
    print(v.menu)
    read = input().lower()

    while (read != 'g' and read != 'a' and read != 'q'):
        print(v.error_start)
        read = input().lower()

    if (read == 'g'):
        exit = generate(m, v)

    if (read == 'a'):
        exit = about(m, v)

    if (read == 'q'):
        exit = True  # quit


def generate (m,v):
    print("generate menu")

def about (m,v):
    print(v.about)

    read = input().lower()
    while (read != 'b' and read != 'q'):
        print(v.error_input)
        read = input().lower()

    if (read == 'b'):
        return main_menu(m, v)  # main menu
    elif (read == 'q'):
        return True  # quit









