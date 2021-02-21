# Import the GUI widgets that you'll be using, and create the 'app' for your program.
from guizero import App, TextBox, PushButton, Text, info


# Function definitions for your events go here.
def btn_go_clicked():
    info("Greetings","Hello, {} - I hope you're having a nice "
                     "day.  You like {}"
         .format(txt_name.value, txt_animal.value))

def btn_come_clicked():
    info("Brave!", "You tried the second button")


# *** Main Routine goes here ***
app = App()

# Your GUI widgets go here
lbl_name = Text(app, text="Hello. What's your name?")
txt_name = TextBox(app)
lbl_animal = Text(app, text="What is your favourite animal?")
txt_animal = TextBox(app)
btn_go = PushButton(app, command=btn_go_clicked, text="Done")
btn_come = PushButton(app, command=btn_come_clicked, text="Try Me")

# Show the GUI on the screen
app.display()
