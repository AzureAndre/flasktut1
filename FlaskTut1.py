from flask import Flask, render_template as RenderTemplate      

app = Flask(__name__)     


@app.route('/')                
def index():                    
    return RenderTemplate('index.html')

@app.route('/home/<string:name>/id/<int:id>')                 
def parametes(name, id):                    
    return f'Hello, {name}: id = {id}!'     

@app.route('/getonly', methods=['GET'])
def get_only():
    return 'This is a GET request only!'


if __name__ == '__main__':      
    app.run(debug=True)         
