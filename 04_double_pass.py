# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info


# Function definitions for your events go here.
def btn_check_pass():
    if pass_1.value == pass_2.value:
        info("Password Checker","Great - your passwords match")
    else:
        info("Password Checker", "Oops - they don't match")


# *** Main Routine goes here ***
app = App()

# Your GUI widgets go here
lbl_pass_1 = Text(app, text="Please enter your password")
pass_1 = TextBox(app)
lbl_pass_2 = Text(app, text="Please enter your password again")
pass_2 = TextBox(app)

btn_go = PushButton(app, command=btn_check_pass, text="Check")


# Show the GUI on the screen
app.display()
