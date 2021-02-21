from guizero import App, TextBox, Text, PushButton, info


# Functions go here
def btn_go_clicked():
    info("Greeting", "Hello {}".format(txt_name.value))


def highlight():
    txt_name.bg = "light blue"


def low_light():
    txt_name.bg = None


# main routine goes here
app = App()

lbl_name = Text(app, text="What is your name? ")
txt_name = TextBox(app)

# Highlight when mouse over button
txt_name.when_mouse_enters = highlight

# low light when mouse leaves button
txt_name.when_mouse_leaves = low_light

app.display()
