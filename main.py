from flask import Flask
'''
Está é uma API simples produzida em python com o framework Flask. 
'''
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return 'Olá Gesto!'

@app.route('/name')
def name():
    """Return a friendly HTTP greeting."""
    return 'Olá, nome é Gabriel! e este é meu linkedin: <a href="https://www.linkedin.com/in/gabriel-heguedusch-389629184/">https://www.linkedin.com/in/gabriel-heguedusch-389629184/ </a>'


if __name__ == '__main__':    
    app.run(host='0.0.0.0', port=80, debug=False)

