# CS2 Sensory overload

A chaotic Counter-Strike 2 assistant that monitors your gameplay via Game State Integration (GSI) and reacts to game events in real-time. Warning: The code is currently held together by duct tape and sheer willpower. It might break easily!

## Features

* **Gemini AI Roasts:** When your deaths exceed your kills, the bot activates Google Gemini to generate long, brutal, and highly personalized roasts.
* **Valorant Mode:** Experience the authentic Valorant toxicity. Plays a sound on every kill and reads a "mid at best" roast every time you die.
* **Grenade Warnings:** Plays an incredibly annoying sound whenever you are stuck inside a smoke, blinded by a flashbang, or burning in a molotov.
* **Flashing Mode:** Flashes a random image from the "flashes" folder after every kill (supports 1920x1080 resolution).

---

##  Installation & Setup

All core files for the bot are located inside the "Bot" folder.

### 1. Prerequisites
Make sure you have Python 3.13.9 or newer installed.

### 2. Install Dependencies
Run the following command in your terminal to install all required packages:

pip install flask google-genai pyttsx3 pygame

### 3. CS2 Game State Integration (GSI) Configuration
To allow the bot to receive real-time events from Counter-Strike 2, copy the "gamestate_integration_python.cfg" file and paste it into your CS2 configuration directory:

C:\Program Files (x86)\Steam\steamapps\common\Counter-Strike Global Offensive\game\csgo\cfg

### 4. API Key Configuration
1. Create a plain text file named "Api_Key.txt" inside the "Bot" folder.
2. Paste your Google GenAI API Key into this file.
(If the key is missing, the bot will notify you via Text-to-Speech and throw an error at startup.)

---

## How to Use

1. Launch the bot by running:
   python cs2thing.py
2. Open the web interface.
3. Click the button in the web UI to trigger a random roast manually, or just play CS2 and let the bot roast your bad plays automatically via pyttsx3.

Note: If the visual effects look misaligned, run "screentest.py" to check your resolution. The overlay features are currently hardcoded for 1920x1080.

---

## Credits & License

* **License:** MIT License. It's a roast bot—do whatever chaos you want with it!
* **Acknowledgment:** Not gonna hide it—ChatGPT helped a lot with this, especially with gsi.py. 
* **Support:** I'm probably playing War Thunder right now. If you open an issue, I might look at it and fix it later... maybe.