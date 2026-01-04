from flask import Flask, request, jsonify
import os
from google import genai
import pyttsx3
import time
import winsound
killdif = int()


ai = int(input("Type 1 if you want AI features: "))
valorantmode = int(input("Type 1 if you want Valorant Mode: "))




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
    global killdif
    data = request.json

    if not data:
        return jsonify({"status": "no data"})

    player = data.get("player", {})
    state = player.get("state", {})
    match = player.get("match_stats", {})

   

    print(
        f"HP: {state.get('health')} | "
        f"Armor: {state.get('armor')} | "
        f"K: {match.get('kills')} "
        f"D: {match.get('deaths')} "
        f"A: {match.get('assists')}"
    )

    


    killss = match.get('kills')
    deathss = match.get('deaths')
    assistss = match.get('assists')

    killss = 0 if killss is None else killss
    deathss = 0 if deathss is None else deathss
    assistss = 0 if assistss is None else assistss
    killdif = 0 if killss == 0 else killdif


    if killss < deathss and ai == 1:
        prompt = (
        f"Roast me without mercy. I'm playing Counter Strike 2, "
        f"and my stats are {killss} kills, {deathss} deaths, "
        f"and {assistss} assists. Give me all you got, swear and all."
    )

        response = client.models.generate_content(
            model='models/gemini-2.0-flash-lite',
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





    return jsonify({"status": "ok"})  



if __name__ == "__main__":
    app.run(port=3000)




