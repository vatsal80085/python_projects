print("Welcome to Treasure Planet!")
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

first_choice = input("Where would you like to go? (type left or right)\n").lower()
if first_choice == "left":
    second_choice = input("Take the jet propeller with bare hands or wait? (type propeller or wait)\n").lower()
    if second_choice == "wait":
        third_choice = input("Which Gateway? (RED, GREEN, BLUE)\n").lower()
        if third_choice == "red":
            print("Realm Of hell IS summoned, Game Over!\n")
        elif third_choice == "green":
            print("You Win! Infinite Wealth Lies In front of YOU! Just have the Perspective!\n")
            print('''  _--~~~~~~~~~~~~~~~~~~--_
                    ./   ASCII MUSTANG ..
                  ./                            
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
            print("You've reached the Land of Nothingness! Game Over!\n")
    else:
        print("Propeller killed you! Game Over!\n")
else:
    print("You fell RIGHT into the trap! Game Over!\n")
