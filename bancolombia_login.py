import pyautogui as py
import webbrowser
import time

# Chrome browser path
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

# Images directory to use pyAutoGui
img_dir = './images/bancolombia/'

# URL to open
URL = "https://sucursalpersonas.transaccionesbancolombia.com/"

###############
# CREDENTIALS #
###############

username = "username"
code = "0000"

code_list = [*code]
images_list = code_list
images_list = [img_dir + x + '.png' for x in images_list]
buttons = []

#############
# FUNCTIONS #
#############

# Function to locate image
def find_img(img, conf=0.9):
    print(img)
    img = img_dir + img
    location = None
    while location is None:
        try:
            if conf == 1:
                location = py.locateCenterOnScreen(img)
            else:
                location = py.locateCenterOnScreen(img, confidence=conf)
        except Exception as e:
            print(e)
    return location

# Function to click image
def find_and_click(png, conf=0.9):
    location = find_img(png, conf)
    py.click(location)
    return location

##############
# AUTOMATION #
##############

# Open URL in Chrome browser
webbrowser.get(chrome_path).open(URL)

print("Buscando ingresar usuario...")
location = find_img('icon-user.png')
py.click(location[0] + 20, location[1])
py.write(username)
py.press('enter')

print("Ingresando usuario...")
print("Buscando numeros...")

# Locate keypad numbers
for i in range(len(code)):
    location = None
    while (location == None):
        try:
            location = py.locateCenterOnScreen(images_list[i])
            coord = (location.x, location.y)
            buttons.append(coord)
        except Exception as e:
            print(e)

# Click keypad password
print("Ingresando password...")
for i in range(len(buttons)):
    py.click(buttons[i])
    time.sleep(1)

print("click ingresar...")
find_and_click('ingresar.png')