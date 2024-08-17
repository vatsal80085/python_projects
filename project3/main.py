print("Welcome to Treasure Planet! ")
print('''     ____...------------...____
               _.-"` /o/__ ____ __ __  __ \o\_`"-._
             .'     / /                    \ \     '.
             |=====/o/======================\o\=====|
             |____/_/________..____..________\_\____|
             /   _/ \_     <_o#\__/#o_>     _/ \_   /
             \_________\####/_________/
              |===\!/========================\!/===|
              |   |=|          .---.         |=|   |
              |===|o|=========/     \========|o|===|
              |   | |         \() ()/        | |   |
              |===|o|======{'-.) A (.-'}=====|o|===|
              | __/ \__     '-.\___/.-'    __/ \__ |
              |==== .'.'^'.'.====|
          jgs |  _\o/   __  {.' __  '.} _   _\o/  _|
              `""""-""""""""""""""""""""""""""-""""`''')
first_choice = input("Where would you like to go? (type left or right)\n")
if first_choice == "left" or "LEFT" or "Left":
    second_choice = input("take the jet propeller with bare hands or wait ?(type propeller or wait)\n")
    if second_choice == "wait" or "Wait" or "WAIT":
        third_choice = input("Which Gateway? (RED, GREEN, BLUE)\n")
        if third_choice == "RED" or "red" or "Red":
            print("Realm Of hell IS summoned, Game Over\n")
        if third_choice == "GREEN" or "green" or "Green":
            print("You Win! Infinite Wealth Lies In front of YOU! Just have the Perspective!\n")
            print('''  _--~~~~~~~~~~~~~~~~~~--_
                    ./   ASCII MUSTANG ..      \
                  ./                            \
                (-.`., ~~~-----------------~~~-.,.-)
                 / \  - _ ,  {________} _. - - /  \
                /\  . ____\_           _/_____ .  /\
                |\_/|____|_\~_-_(@)_-_~/_|____|\__/|
                [  _____   /#         #\  _____    ]
                /.{ }...,,] \ -- - -- / [,,.. { }. \
                \--_((____)(___- - -___)(_____))_--/
    BLGM        |>>>>|        {83,50}         |<<<<|
        ___   ` \<<<>>>/'__''')
        else:
            print("You've reached to the Land of nothingness! Game Over!\n")
    else:
        print("Propeller Killed you! , Game Over\n")
else:
    print("You fell RIGHT into the trap!, Game Over!\n")
