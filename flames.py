from flask import Flask, render_template, request
import os

app = Flask(__name__)

def calculate_flames(name1, name2):
    # Convert names to lowercase & remove spaces
    a = list(name1.lower().replace(" ", ""))
    b = list(name2.lower().replace(" ", ""))

    # Remove common letters
    for ch in a[:]:
        if ch in b:
            a.remove(ch)
            b.remove(ch)

    # Count remaining letters
    o = len(a) + len(b)

    # FLAMES list
    z = list("flames")
    x = 0

    # Eliminate letters cyclically
    while len(z) > 1:
        x = (x + o - 1) % len(z)
        z.pop(x)

    # Map letter to full form
    h = {
        'f': "Friend",
        'l': "Love",
        'a': "Affection",
        'm': "Marriage",
        'e': "Enemy",
        's': "Sister"
    }

    return h[z[0]]


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        name1 = request.form.get("name1", "")
        name2 = request.form.get("name2", "")
        if name1 and name2:
            result = calculate_flames(name1, name2)

    return render_template("index.html", result=result)


# IMPORTANT FOR RENDER
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)










