from flask import Flask, request
app = Flask(__name__)

@app.route("/upload", methods=["get", "post"])
def hello():
    return str(request.form) + str(request.files)

if __name__ == "__main__":
    app.run()