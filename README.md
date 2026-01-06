CS2 Roast Bot / Sound Bot / I dont fucking know what Bot

The script is held up by duct tape so it can break very easily

Plays sounds based on enabled things

AI features turn on Gemini generated roasts that are long af but better than valorant mode death ones, it activates when you have more deaths than kills

Valorant mode plays a sound when you get a kill or reads a mid at best roast when you die (use for authentic Valorant experince)

Grenade warning plays annoying sound when in a smoke, you get flashed, or burning

Flashing mode flashes a image from "flashes" folder after every kill

gsi.py just prints all the data cs2 sends, made for easier creation and customization

Installation

All files for the bot are located in "Bot" folder

Run this command to get all required Python packages:

pip install flask google-genai pyttsx3


winsound and random are built into Python, no installation required, hmm hmm…

Configuration

Place the file gamestate_integration_python.cfg in:

C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg


so the bot can receive game events.

Create a text file named Api_Key.txt in the bot folder and paste your Google GenAI API key in it.
The bot will automatically read it at startup. If missing, it will alert you via speech and raise an error.

How to Use

Start the bot with:

python cs2soundbot.py


Press the button in the web interface to get a random roast.

The roast will be spoken out loud via pyttsx3.

A beep will sound for dramatic effect using winsound.

Works alongside CS2 events if the config is correctly installed.

Notes

Roasts are savage… no mercy.

Make sure Python 3.13.9 or newer is installed.

For custom roasts, edit the roasts list in the Python script.


License

MIT license… but seriously, it’s a roast bot… feel free to chaos, hmm hmm

Im gonna play war thunder, if i see any issues reported i might fix them

Readme was kinda written by Chat GPT

(Chat GPT wrote the tutorial)


