from guizero import App, TextBox, Text, PushButton, info, \
    ButtonGroup, Combo


# Functions go here
def btn_make_name():
    generated ="You are a {} {} {}".format(txt_name.value,
                                  txt_color.value,
                                  txt_animal.value)
    lbl_generated_name.value = generated


# main routine goes here
app = App(title="Name Generator")

lbl_name = Text(app, text="Choose an adjective", size=14)
txt_name = ButtonGroup(app, options=["Great", "Amazing", "Marvelous"])

lbl_color = Text(app, text="Enter a colour", size=14)
txt_color = TextBox(app)

lbl_animal = Text(app, text="Pick an Animal", size=14)
txt_animal = Combo(app, options=["Sheep", "Goat", "Gold Fish"])

btn_generate = PushButton(app, command=btn_make_name, text="Generate")

lbl_generated_name = Text(app, text="")

app.display()
