from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_flames(name1, name2):
    a = list(name1.lower().replace(" ", ""))
    b = list(name2.lower().replace(" ", ""))

    for ch in a[:]:
        if ch in b:
            a.remove(ch)
            b.remove(ch)

    count = len(a) + len(b)

    flames = ["F", "L", "A", "M", "E", "S"]
    index = 0

    while len(flames) > 1:
        index = (index + count - 1) % len(flames)
        flames.pop(index)

    meanings = {
        "F": "Friend",
        "L": "Love",
        "A": "Affection",
        "M": "Marriage",
        "E": "Enemy",
        "S": "Sister"
    }

    return meanings[flames[0]]


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        name1 = request.form.get("name1")
        name2 = request.form.get("name2")
        if name1 and name2:
            result = calculate_flames(name1, name2)

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run()



