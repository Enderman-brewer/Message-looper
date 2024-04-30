import pyautogui

MSG1 = input("Please enter message 1/3 ")
MSG2 = input("Please enter message 2/3 ")
MSG3 = input("Please enter message 3/3 ")
responce = 'NULL'
def mainprint(input):
    global one
    global responce
    if responce == "N":
        pyautogui.keyDown('ctrl')
        pyautogui.press("a")
        pyautogui.keyUp('ctrl')
        pyautogui.press('backspace')
    pyautogui.typewrite(input)
    pyautogui.press('enter')
    pyautogui.sleep(one)

choice = 0
while choice != '0':
    responce = input("Skip clearing? (Y/N)")
    if responce.upper() == "Y":  # Check for "Y" (case-insensitive)
        choice = '0'  # Update choice only if skipping
    elif responce.upper() == "N":  # Check for "Y" (case-insensitive)
        choice = '0'  # Update choice only if skipping


starttime = float("0.5")
pyautogui.sleep(starttime)
one = int("1")
while True:
    mainprint(MSG1)
    mainprint(MSG2)
    mainprint(MSG3)
