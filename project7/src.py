
#step1
import curses  # pip install windows-curses ##this module is built-in in mac0s and linux
from curses import wrapper # initializes this module and basically takes over the terminal
import time #for wpm
import random

#step2
def start_screen(stdscr):
    stdscr.clear()  # clears junk that would otherwise overlay on screen
    stdscr.addstr("Typing test WPM\n")
    stdscr.addstr("Press any key to continue! \n")
    # stdscr.addstr("Orewa Monkey D Luffy", curses.color_pair(2))
    stdscr.refresh()
    stdscr.getkey()

#step4
#To overlay typed text on target text
def display_text(stdscr, target, current, wpm=0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM: {wpm}") #displays the word per minute to the user

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)

        if char != correct_char:
            color = curses.color_pair(2)

        stdscr.addstr(0, i, char, color)

#step5 
# File Handling
def load_text():
    with open("text.txt", "r") as f:
        lines= f.readlines()
        return random.choice(lines).strip() #Return a copy of the string with leading and trailing whitespace removed. If chars is given and not None, remove characters in chars instead


#primary step
def wpm_test(stdscr):
    target_text = load_text()
    current_text = []

    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        #step5
        time_elapsed = max(time.time() - start_time, 1)
        wpm = round((len(current_text) / (time_elapsed / 60)) / 5)    # eqn for calculating wpm when we assume that average word contains 5 characters

        #step3
        stdscr.clear()  # clears junk that would otherwise overlay on screen
        display_text(stdscr, target_text, current_text, wpm)
        stdscr.refresh()

        if "".join(current_text) == target_text:
            stdscr.nodelay(False)
            break
        
        try:    # makes sure this line doesnt crash on us #Exception handling
            key = stdscr.getkey()
        except:
            continue 

        if (ord(key) == 27):  # ord/ordinal value of the key is its ASCII/numeric value on the keyboard ##here 27->ESC button on keyboard
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f",):  ##this is just the different ways different os represent backspace key
            if len(current_text) > 0:
                current_text.pop()  # removes last character of the list here
        elif len(current_text) < len(target_text):
            current_text.append(key)


#combining all steps here and calling all functions here for execution
# stdscr stands for standard screen
def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # (pair_number: int, fg: int, bg: int, /) -> None
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)  # (pair_number: int, fg: int, bg: int, /) -> None
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)  # (pair_number: int, fg: int, bg: int, /) -> None

    start_screen(stdscr)
    while True:
        wpm_test(stdscr)

        stdscr.addstr(2, 0, "You Completed The Text! Press any key to continue..And ESC To exit ")
        key = stdscr.getkey()
        if ord(key) == 27:
            break


wrapper(main)
