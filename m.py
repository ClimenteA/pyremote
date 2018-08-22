from pynput.mouse import Button, Controller

mouse = Controller()

# Read pointer position

def mpos():
    value = mouse.position
    #print(value)
    return value

def setmpos(mpos_tuple, set_tuple):
    new_mpos = (mpos_tuple[0] + set_tuple[0], mpos_tuple[1] + set_tuple[1])
    mouse.position = new_mpos

def click():
    mouse.press(Button.left)
    mouse.release(Button.left)

def doubleClick():
    mouse.click(Button.left, 2)
    

def rightClick():
    mouse.press(Button.right)
    mouse.release(Button.right)

def scrollUp():
    mouse.scroll(10, 0)

def scrollDown():
    mouse.scroll(0, 10)

