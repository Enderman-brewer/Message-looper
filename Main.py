import pyautogui

MSG1 = input("Please enter message 1/3 ")
MSG2 = input("Please enter message 2/3 ")
MSG3 = input("Please enter message 3/3 ")

starttime = float("0.5")
pyautogui.sleep(starttime)
one = int("1")
while True:
    pyautogui.sleep(one)
    pyautogui.typewrite(MSG1)
    pyautogui.press('enter')
    pyautogui.keyDown('ctrl')
    pyautogui.press("a")
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')
    pyautogui.sleep(one)
    pyautogui.typewrite(MSG2)
    pyautogui.press('enter')
    pyautogui.keyDown('ctrl')
    pyautogui.press("a")
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')
    pyautogui.sleep(one)
    pyautogui.typewrite(MSG3)
    pyautogui.press('enter')
    pyautogui.keyDown('ctrl')
    pyautogui.press("a")
    pyautogui.keyUp('ctrl')
    pyautogui.press('backspace')
