from flask import Flask

app = Flask(__name__)     


@app.route('/')  
@app.route('/home')
def index():                    
    return "Hello World!"


@app.route('/hello/<string:name>/id/<int:id>')
def hello(name, id):
    return f"<H1>Hello, {name}!</H1><p>Your ID is: {id}</p>"

@app.route('/getonly', methods=['POST', 'GET'])
def getonly():                    
    return "Hello World!"



if __name__ == '__main__':      
    app.run(debug=True)         
