from flask import Flask
app=Flask(__name__)

@app.route('/')
def grad_des():
    return 'api1'

if __name__=="__main__":
    app.run(debug=True)