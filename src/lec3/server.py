from flask import Flask
from flask import render_template
from flask import request 

app = Flask(__name__)

names = []

@app.route("/")
def main():
  return render_template('index.html', names=list)

@app.route('/form', methods=['POST'])
def handle_form():
    name = request.form.get('name') 
    list.append(name)
    return "success"