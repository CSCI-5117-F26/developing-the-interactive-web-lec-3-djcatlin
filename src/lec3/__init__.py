from flask import Flask
from flask import render_template
from flask import request 

app = Flask(__name__)

names = []

@app.route("/")
def main():
  return render_template('index.html', names=names)

@app.route('/form', methods=['POST'])
def handle_form():
    name = request.form.get('name') 
    names.append(name)
    return render_template('index.html', names=names)

def main() -> None:
    app.run()