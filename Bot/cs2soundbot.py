from flask import Flask, request, jsonify
import os
from google import genai
import pyttsx3
import time
import winsound
import random
import tkinter as tk
import ctypes
from multiprocessing import Process, freeze_support
import threading
killdif = int()
deathdif = int()
playername = None
steamid = None

cwdpath = os.getcwd()
imgpath = os.path.join(cwdpath, "flashes")
imgfiles = os.listdir(imgpath)

print(imgpath, imgfiles)

def playsound(file):
    winsound.PlaySound(file, winsound.SND_FILENAME)

def threadsound(sound):
    threading.Thread(target=playsound, args=(sound,), daemon=True).start()

def fade(step=0):
         if step > STEPS:
            root.destroy()
            return

def flashimagine():
    STEPS = 50
    FADE_DURATION = 1000
    START_ALPHA = 1.0
    END_ALPHA = 0.0
    alpha_step = (START_ALPHA - END_ALPHA) / STEPS
    step_delay = FADE_DURATION // STEPS

    
    flashes = random.choice(imgfiles)
    useflashimage = os.path.join(imgpath, flashes)

    root = tk.Tk()
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.attributes("-alpha", START_ALPHA)
    root.attributes("-transparentcolor", "black")
    root.update_idletasks() 

    img = tk.PhotoImage(file=useflashimage)
    label = tk.Label(root, image=img, bg="black")
    label.image = img
    label.pack(fill="both", expand=True)

    screenwidth = root.winfo_screenwidth()
    screenheight = root.winfo_screenheight()
    imgwidth = img.width()
    imghieght = img.height()
    centrewidth = (screenwidth - imgwidth) // 2
    centrehight = (screenheight - imghieght) // 2

    root.geometry(f"{imgwidth}x{imghieght}+{centrewidth}+{centrehight}")

    
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    GWL_EXSTYLE = -20
    WS_EX_LAYERED = 0x00080000
    WS_EX_TRANSPARENT = 0x00000020
    WS_EX_NOACTIVATE = 0x08000000

    style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_EXSTYLE)
    ctypes.windll.user32.SetWindowLongW(
        hwnd,
        GWL_EXSTYLE,
        style | WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_NOACTIVATE
    )

    
    
    new_alpha = START_ALPHA - step * alpha_step
    root.attributes("-alpha", max(new_alpha, 0))
    root.after(step_delay, fade, step + 1)

    root.after(100, fade)
    root.mainloop()


if __name__ == "__main__":
    freeze_support()

    p = Process(target=flashimagine)
    #p.start()

    ai = int(input("Type 1 for AI features: "))
    valorantmode = int(input("Type 1 for Valorant Mode: "))
    grenadewarningmode = int(input("Type 1 for Grenade Warnings: "))
    flashmode = int(input("Type 1 for Flashing Mode: "))


    prompt = ("")
    cwd = os.getcwd()
    path = cwd
    dir_list = os.listdir(path)
    if "Api_Key.txt" in dir_list:
        file = open('Api_Key.txt', 'r') 
        content = file.read()
        GEMINI_API_KEY = content
    else:
        if ai == 1:
            print("No API key found, create Api_Key.txt in this folder and put your api key in there")
            pyttsx3.speak("No API key, create Api_Key.txt")
            raise("No Api Key")
        GEMINI_API_KEY = "none"
        

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
        global playername
        global steamid


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
            f"Name: {player.get('name')} "
            f"SteamID: {player.get('steamid')} "
            f"Activity: {player.get('activity')} "
        )
        
        


        steamid = player.get('steamid') if steamid is None else steamid
        playername = player.get('name') if playername is None else playername

        print(playername, steamid)

        if steamid == player.get('steamid'):
            killss = match.get('kills')
            deathss = match.get('deaths')
            assistss = match.get('assists')

            killss = 0 if killss is None else killss
            deathss = 0 if deathss is None else deathss
            assistss = 0 if assistss is None else assistss
            killdif = 0 if killss == 0 else killdif
            deathdif = 0 if deathss == 0 else deathdif
            burning = 0 if burning is None else burning
            smoked = 0 if smoked is None else smoked
            flashed = 0 if flashed is None else flashed
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
            if killdif != killss:
                killdif = killss
                if valorantmode == 1:
                    threadsound("valomode.wav")
                    print("UwU :3")
                if flashmode == 1:
                    flashimagine()
                
            if deathdif != deathss and valorantmode == 1:
                #pyttsx3.speak(random.choice(roasts))
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




