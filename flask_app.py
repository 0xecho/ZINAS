

from flask import Flask,jsonify,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
@app.route('/upload_wav',methods=["GET","POST"])
def process():
    if request.method == 'POST':
        if request.form['key'] == "KwErtY":
            f = request.files['file']
            filePath = "/home/joeking/"+f.filename
            f.save(filePath)
            return "success"
    return "hello"

if __name__ == "__main__":
    app.run()
