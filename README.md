CS2 Roast Bot

This is a brutal roast bot for Counter-Strike 2, made in Python 3.13.9.
It insults players, reads the roast aloud, and even plays a beep… chaos incarnate, uhh…

Installation

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

python roast_bot.py


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
Readme was written by chat gpt
