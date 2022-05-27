from re import L
from flask import Flask
app=Flask(__name__)

@app.route('/')
def grad_des():
    return 'api1'

def grad_desc1():
    return 'api2'

if __name__=="__main__":
    app.run(debug=True)