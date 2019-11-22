from flask import Flask, render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello_www():
    # return '<h1>Hello World</h1>'
    return render_template('index.html')


app.run()
