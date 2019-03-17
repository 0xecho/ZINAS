from flask import Flask,jsonify,request
from analyse_wav import analyse_from_file
import binascii

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'
@app.route('/upload_wav/',methods=["GET","POST","PUT"])
def process():
    for i in request.form:
        print(i.encode('utf-8'))
    if request.method == 'GET':
        # if request.form['key'] == "KwErtY":
        # f = request.files['file']
        # print(f.filename)
        # filePath = "/home/joeking/Desktop/HACK_A_TOWN/audio/app/ZINAS/"+f.filename
        # f.save(filePath)

        return jsonify({"desc":"success uploading "+str(f.filename),
                        "data":analyse_from_file(f.filename)})
    return "hello"
# @app.route('/test_for_fun/')
# def fun():
#     if request.method == "POST":
#         return ""
#     return """
#         <form method="post" enctype="multipart/form-data">
#   <input type="file" name="audio" accept="audio/*" capture>
#   <input type="submit" value="Upload">
# </form>
#     """
if __name__ == "__main__":
    app.run(host="0.0.0.0")
