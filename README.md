# Greet on startup

Simple script that greets you once a day.

# Installation and setup

I assume that you have already created virtual environment and installed necessary dependencies.

Now you have to create a shortcut for python interpreter ```.exe``` file from your venv and pass a location of the ```main.py``` as an argument (object section in Options of a shortcut should look like this: path_to_interpreter path_to_main. Example: D:\Projects\greet_on_startup\\.venv\Scripts\python.exe D:\Projects\greet_on_startup\main.py).

Then you put this shortcut inside folder which is located here: ```C:\Users\{your_username}\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup```.

And that's it.