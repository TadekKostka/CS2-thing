from flask import Flask, request
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def gsi():
    data = request.json

    print("====================================")
    print("NOWY GAMESTATE… O NIE… 67…")
    print(json.dumps(data, indent=2, ensure_ascii=False))
    print("====================================")

    return "ok"

app.run(port=3000)
