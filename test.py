import keyboard  # using module keyboard
from time import sleep
while True:  # making a loop
  var = None
  var = keyboard.get_hotkey_name().strip()
  if var:
   keyboard.wait('backspace')
   print(var)
  sleep(0.4)
