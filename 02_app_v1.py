from guizero import App, Text

app = App(title="this is my first GUI")

# first message, blue and big
message = Text(app, text="guis are cool!",
               size=40, color="blue")

# second message, black
message_2 = Text(app, text="another message")

# displays GUI
app.display()
