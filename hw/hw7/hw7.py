from flask import Flask, request, render_template
app = Flask(__name__)
@app.route("/")
def hello():
return "Hello World!"
@app.route('/test')
def test_function():
return '<h1>Different more text </h1>'
@app.route('/test/<int:number>')
def test_number(number):
content = '<h1>Different more text for #{}<h1>'
content = content.format(number)
return content
@app.route =('/login', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
return 'This is a POST'
else:
return 'This is a GET'
@app.route/('hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html',name=name)
