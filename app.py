from flask import Flask, render_template

app = Flask(__name__)


def get_current_temp():
    return 70


@app.route("/")
def hello():
    temp = get_current_temp()
    return render_template("index.html", temp=temp)

if __name__ == "__main__":
    app.run()
