from flask import Flask, render_template as RenderTemplate      

app = Flask(__name__)     


@app.route('/')  
@app.route('/home')              
def index():                    
    return "Hello World!"

@app.route('/home/<string:name>/id/<int:id>')                 
def parametes(name, id):                    
    return f'Hello, {name}: id = {id}!'     

@app.route('/getonly', methods=['POST'])
def get_only():
    return 'This is a GET request only!'


if __name__ == '__main__':      
    app.run(debug=True)         
