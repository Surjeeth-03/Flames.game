from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_flames(name1, name2):
    a = list(name1.lower().replace(" ", ""))
    b = list(name2.lower().replace(" ", ""))

    for ch in a[:]:
        if ch in b:
            a.remove(ch)
            b.remove(ch)

    c = len(a) + len(b)
    flames = ["F", "L", "A", "M", "E", "S"]
    i = 0

    while len(flames) > 1:
        i = (i + c - 1) % len(flames)
        flames.pop(i)

    return flames[0]

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
    app.run(debug=True)
if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))


