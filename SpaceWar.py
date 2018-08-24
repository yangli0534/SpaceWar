import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from random import randint

curses.initscr()
win = curses.newwin(20, 60, 0, 0)
win.keypad(1)
curses.noecho()
curses.curs_set(0)
win.border(0)
win.nodelay(1)

key = KEY_RIGHT
score = 0
flag = True # True for right, Falsefor left
airship = [[14,10], [14, 9], [14,8],[13,9]]
bullets =[]
target =[10, 20]
win.addch(target[0], target[1], '*')

while key!= 27:
    win.border(0)
    win.addstr(0, 2, 'Score: ' + str(score)+' ')
    win.addstr(0,27, 'TEST')
    win.timeout(150 - (len(airship)/5 + len(airship)/10)%120)          # Increases the speed of Snake as its length increases
    
    prevKey = key
    key = win.getch()
    # Previous key pressed
    #event = win.getch()
    #key = key if event == -1 else event
    if key == ord(' '):                                            # If SPACE BAR is pressed, wait for another
        key = -1                                                   # one (Pause/Resume)
        while key != ord(' '):
            key = win.getch()
        #key = prevKey
        continue

    #if key not in [KEY_LEFT, KEY_RIGHT, KEY_UP, KEY_DOWN, 27]:     # If an invalid key is pressed
    #    key = prevKey
    #if key != prevKey and  (not key not in [KEY_LEFT, KEY_RIGHT]):
       # airship.reverse()
        #flag = key == KEY_RIGHT
    # Calculates the new coordinates of the head of the airship. NOTE: len(airship) increases.
    # This is taken care of later at [1].
    #airship.insert(0, [airship[0][0] + (key == KEY_DOWN and 1) + (key == KEY_UP and -1), airship[0][1] + (key == KEY_LEFT and -1) + (key == KEY_RIGHT and 1)])
    
    # If airship crosses the boundaries, make it enter from the other side
    #if airship[0][0] == 0: airship[0][0] = 18
    if airship[0][1] == 0 or airship[0][1]==59:
        airship.reverse()
        flag = not flag
    # if airship[0][0] == 19: airship[0][0] = 1
    #if airship[0][1] == 59: airship[0][1] = 1
    if flag:
        airship.insert(0,[airship[0][0], airship[0][1]+1])
    else:
        airship.insert(0,[airship[0][0], airship[0][1]-1])
    # Exit if airship crosses the boundaries (Uncomment to enable)
    #if airship[0][0] == 0 or airship[0][0] == 19 or airship[0][1] == 0 or airship[0][1] == 59: break

    # If airship runs over itself
    #if airship[0] in airship[1:]: break

    # fire a bullet
    if key != prevKey and key == KEY_UP:
        bullets.append([13,airship[1][1]])
        curses.beep()
    # bullet on fire    
    length = len(bullets)
    exploded = []
    if (length > 0):    
        for i in range(length):
            #win.addch(bullets[i][0], bullets[i][1], ' ')
            bullets[i][0]-=1
            if bullets[i][0] <= 0:
                win.addch(bullets[i][0]+1, bullets[i][1], ' ')
                #bullets.pop(i)
                exploded.append(i)
        for i in exploded:
            bullets.pop(i)
            # else:
            #    win.addch(bullets[i][0], bullets[i][1], '#')
        for i in range(len(bullets)):
            win.addch(bullets[i][0]+1, bullets[i][1],' ')
            win.addch(bullets[i][0], bullets[i][1],'#')

    if target in bullets:# When airship eats the bullet
        #win.beep()
        target = []
        score += 1
        while target == []:
            target = [randint(1, 10), randint(1, 58)]                 # Calculating next bullet's coordinates
            if target in airship and target in bullets : bullet = []
        win.addch(target[0], target[1], '*')
    #else:
        
    last = airship.pop()                                          # [1] If it does not eat the bullet, length decreases
    win.addch(last[0], last[1], ' ')
    win.addch(airship[0][0], airship[0][1], '#')
curses.endwin()
print('game over')
