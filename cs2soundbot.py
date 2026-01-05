from flask import Flask, request, jsonify
import os
from google import genai
import pyttsx3
import time
import winsound
import random
killdif = int()
deathdif = int()

ai = int(input("Type 1 if you want AI features: "))
valorantmode = int(input("Type 1 if you want Valorant Mode: "))
grenadewarningmode = int(input("Type 1 if you want Grenade Warnings: "))



prompt = ("")
cwd = os.getcwd()
path = cwd
dir_list = os.listdir(path)
if "Api_Key.txt" in dir_list:
    file = open('Api_Key.txt', 'r') 
    content = file.read()
    GEMINI_API_KEY = content
else:
    print("No API key, go fuck yourself")
    pyttsx3.speak("No API key, go fuck yourself")
    

client = genai.Client(api_key=GEMINI_API_KEY)

app = Flask(__name__)

@app.route("/", methods=["POST"])
def gsi():
    roasts = [
        "Hey, even in hell nobody wanted you at the party, uhh...",
        "Congrats, now you can finally be useless enough that nobody sees you.",
        "Your life was like a rebooted movie… no one remembers it.",
        "Even ghosts throw up at the sight of you, hmm hmm...",
        "You sucked the last bit of meaning out of life just by existing.",
        "You know what? Even death is laughing at you.",
        "You died and… no one even noticed, hmm… maybe the neighbor's cat.",
        "Your legacy? Emptiness, uhh… pure emptiness.",
        "Congrats, even your shadow doesn’t want to remember you.",
        "In the afterlife they said: 'Relax, nobody asked about you.'"
    ]
    global killdif
    global deathdif


    data = request.json

    if not data:
        return jsonify({"status": "no data"})

    player = data.get("player", {})
    state = player.get("state", {})
    match = player.get("match_stats", {})
    activity = player.get("activity")
    flashed = state.get("flashed")
    smoked = state.get("smoked")
    burning = state.get("burning")

   

    print(
        f"State: {activity} "
        f"HP: {state.get('health')} | "
        f"Armor: {state.get('armor')} | "
        f"K: {match.get('kills')} "
        f"D: {match.get('deaths')} "
        f"A: {match.get('assists')} "
        f"Flashed; {flashed} "
        f"Smoked; {smoked} "
        f"Burning; {burning} "
    )

    


    killss = match.get('kills')
    deathss = match.get('deaths')
    assistss = match.get('assists')

    killss = 0 if killss is None else killss
    deathss = 0 if deathss is None else deathss
    assistss = 0 if assistss is None else assistss
    killdif = 0 if killss == 0 else killdif
    deathdif = 0 if deathss == 0 else deathdif


    if killss < deathss and ai == 1:
        prompt = (
        f"Roast me without mercy. I'm playing Counter Strike 2, "
        f"and my stats are {killss} kills, {deathss} deaths, "
        f"and {assistss} assists. Give me all you got, swear and all."
    )

        response = client.models.generate_content(
            model='gemini-2.5-flash-lite',
            contents={'text': prompt, },
            config={
                'temperature': 0,
                'top_p': 0.95,
                'top_k': 20,
            }
        )

        print(response.text)
        pyttsx3.speak(response.text)
        time.sleep(120)
    if killdif != killss and valorantmode == 1:
        winsound.PlaySound("valomode.wav", winsound.SND_FILENAME)
        killdif = killss
        print("UwU :3")
    if deathdif != deathss and valorantmode == 1:
        pyttsx3.speak(random.choice(roasts))
        print("U died dumbahh")
        deathdif = deathss
    if flashed > 0 and grenadewarningmode == 1:
        winsound.PlaySound("flash.wav", winsound.SND_FILENAME)
        print("Flashed")
    if burning > 0 and grenadewarningmode == 1:
        winsound.PlaySound("burning.wav", winsound.SND_FILENAME)
        print("Burning")
    if smoked > 0 and grenadewarningmode == 1:
        winsound.PlaySound("smoked.wav", winsound.SND_FILENAME)
        print("Smoked")









    return jsonify({"status": "ok"})  



if __name__ == "__main__":
    app.run(port=3000)




