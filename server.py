from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninja')
def blue():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def ninjacolor(color):
    return render_template(color+".html")

app.run(debug = True)