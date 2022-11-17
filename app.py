from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")

def helloWorld():
    return render_template("home.html")

@app.route('/test', methods=['GET', 'POST'])
def formDemo():
    name = None
    if request.method == 'POST':
        name=request.form['name']
    return render_template('otherPage.html', name=name)