from pynput import keyboard
import m

up = "Key.up"
down = "Key.down"
left = "Key.left"
right = "Key.right"


def on_press(key):
    try:
        global k
        k = key.char
        if k == '0':
            m.click()
        elif k == "1":
            m.doubleClick()
        elif k == '4':
            m.rightClick()
        elif k == "8":
            m.scrollUp()
        elif k == "2":
            m.scrollDown()

    except AttributeError:
        print(key)
        global mouse_position
        mouse_position = m.mpos()
        if str(key) == up:
            m.setmpos(mouse_position, (0, -5))
        elif str(key) == down:
            m.setmpos(mouse_position, (0, 5))
        elif str(key) == left:
            m.setmpos(mouse_position, (-5, 0))
        elif str(key) == right:
            m.setmpos(mouse_position, (5, 0))

     
def on_release(key):
    print(key)

    if str(key) == up:
        m.setmpos(mouse_position, (0, -5))
    elif str(key) == down:
        m.setmpos(mouse_position, (0, 5))
    elif str(key) == left:
        m.setmpos(mouse_position, (-5, 0))
    elif str(key) == right:
        m.setmpos(mouse_position, (5, 0))
    elif k == "8":
            m.scrollUp()
    elif k == "2":
            m.scrollDown()

    
    if key == keyboard.Key.esc:
        # Stop listener
        return False



# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
