from operator import eq

import keyboard
import time

print ('press "ctrl + e" to exit. ')

def printSavedKey():
    print ("print savesd")

def key_pressed(key):
    global pressedKey
    global DELAY_TIME
    global mode
    global savedKey
    global lastSpace
    if eq(key, "space") and lastSpace == 0:
        if savedMod[0] == 0 and savedMod[1] == 0:
            keyboard.press_and_release('backspace')
        elif savedMod[0] == 1 and savedMod[1] == 1:
            keyboard.press_and_release('backspace')
            keyboard.press_and_release('backspace')
            keyboard.press_and_release('backspace')

        else:
            if pressedKey >= 3:
                keyboard.press_and_release('backspace')
                keyboard.press_and_release('backspace')
            else:
                keyboard.press_and_release('backspace')
            keyboard.press_and_release('backspace')

            for i in range(0, pressedKey):
                keyboard.press_and_release(savedKey[i])
        keyboard.press_and_release("space")
        keyboard.press_and_release('backspace')
        pressedKey = 0

    if eq(key, "space"):
        not lastSpace
    elif eq(key, "backspace"):
        if pressedKey is not 0:
            pressedKey -= 1
        savedMod[1] = savedMod[0]
        savedMod[0] != savedMod[0]
    elif eq(key, "cKey"):
        not not key
    else:
        savedMod[0] = savedMod[1]
        savedMod[1] = mode
        savedKey[pressedKey] = key
        pressedKey += 1
        if eq(savedKey[0],savedKey[1])and not eq(savedKey[0],"")and not eq(savedKey[0],""):
            keyboard.press_and_release("backspace")
            keyboard.press_and_release("backspace")
            keyboard.press_and_release("backspace")
            savedKey[pressedKey-2] = "shift+"+str(savedKey[pressedKey-2])
            pressedKey = 1
            keyboard.press_and_release(savedKey[0])


    if lastSpace == 1 and eq(key,"space"):
        print ("???")

    lastSpace = 0
    if eq(key,"space"):
        lastSpace = 1

    time.sleep(DELAY_TIME)
    #print ("mode : "+str(mode)+"    key : "+key+"    pressedKey : "+str(pressedKey)+"   savedKey : "+str(savedKey)+"    modesave : "+str(savedMod))


while 1:
    DELAY_TIME = 0.2
    mode = 0  # 0 = ja // 1 = mo imput
    savedKey = ['', '', '', '', '', '']
    savedMod = [0, 0]
    pressedKey = 0
    lastSpace = 0
    cKey = "g"

    shiftMod = 0
    ctrlMod = 0

    keyboard.release("ctrl")
    keyboard.release("shift")

    print ("start")
    while 1:
        if keyboard.is_pressed('ctrl+e'):  # exit
            exit(1)
        if keyboard.is_pressed('ctrl+q'):  #reset
            break

        if keyboard.is_pressed('j'):
            if mode is 0:
                keyboard.press_and_release('backspace+a')
                mode = 1
                key_pressed('a')
            elif mode is 1:
                mode = 0
                key_pressed('j')

        if keyboard.is_pressed('k'):
            if mode is 0:
                keyboard.press_and_release('backspace+s')
                mode = 1
                key_pressed('s')
            elif mode is 1:
                mode = 0
                key_pressed('k')

        if keyboard.is_pressed('l'):
            if mode is 0:
                keyboard.press_and_release('backspace+d')
                mode = 1
                key_pressed('d')
            elif mode is 1:
                mode = 0
                key_pressed('l')

        if keyboard.is_pressed(';'):
            keyboard.press_and_release('backspace+f')
            mode = 1
            key_pressed('f')

        if keyboard.is_pressed("'"):
            if mode is 0:
                keyboard.press_and_release('backspace+g')
                mode = 1
                key_pressed('g')
            elif mode is 1:
                mode = 0
                key_pressed("'")

        if keyboard.is_pressed("u"):
            if mode is 0:
                keyboard.press_and_release('backspace+q')
                mode = 1
                key_pressed('q')
            elif mode is 1:
                mode = 0
                key_pressed('u')

        if keyboard.is_pressed("i"):
            if mode is 0:
                keyboard.press_and_release('backspace+w')
                mode = 1
                key_pressed('w')
            elif mode is 1:
                mode = 0
                key_pressed('i')

        if keyboard.is_pressed("o"):
            if mode is 0:
                keyboard.press_and_release('backspace+e')
                mode = 1
                key_pressed('e')
            elif mode is 1:
                mode = 0
                key_pressed('o')

        if keyboard.is_pressed("p"):
            if mode is 0:
                keyboard.press_and_release('backspace+r')
                mode = 1
                key_pressed('r')
            elif mode is 1:
                mode = 0
                key_pressed('p')

        if keyboard.is_pressed("["):
            keyboard.press_and_release('backspace+t')
            mode = 1
            key_pressed('t')

        if keyboard.is_pressed("m"):
            if mode is 0:
                keyboard.press_and_release('backspace+z')
                mode = 1
                key_pressed('z')
            elif mode is 1:
                mode = 0
                key_pressed('m')

        if keyboard.is_pressed(","):
            keyboard.press_and_release('backspace+x')
            mode = 1
            key_pressed('x')

        if keyboard.is_pressed("."):
            keyboard.press_and_release('backspace+c')
            mode = 1
            key_pressed('c')

        if keyboard.is_pressed("/"):
            keyboard.press_and_release('backspace+v')
            mode = 1
            key_pressed('v')

        if keyboard.is_pressed('y'):
            mode = 0
            key_pressed('y')

        if keyboard.is_pressed('h'):
            mode = 0
            key_pressed('h')

        if keyboard.is_pressed('n'):
            mode = 0
            key_pressed('n')

        if keyboard.is_pressed('b'):
            mode = 0
            key_pressed('b')

        if keyboard.is_pressed(cKey):
            if mode == 0:
                mode = 1
            else:
                mode = 0
            key_pressed(cKey)

        if keyboard.is_pressed('backspace'):
            if mode == 0:
                mode = 1
            else:
                mode = 0
            key_pressed('backspace')

        if keyboard.is_pressed('space'):
            keyboard.press_and_release('space')
            keyboard.press_and_release("backspace")
            mode = 0
            key_pressed('space')

        if keyboard.is_pressed("t"):
            if shiftMod == 1:
                keyboard.press("shift")
                shiftMod = 0
            else:
                keyboard.release("shift")
                shiftMod = 1


        if keyboard.is_pressed("v"):
            if shiftMod == 1:
                keyboard.press("ctrl")
                shiftMod = 0
            else:
                keyboard.release("ctrl")
                shiftMod = 1

        if keyboard.is_pressed("c"):
            keyboard.press_and_release("ctrl+c")

        if keyboard.is_pressed("z"):
            keyboard.press_and_release("ctrl+z")


