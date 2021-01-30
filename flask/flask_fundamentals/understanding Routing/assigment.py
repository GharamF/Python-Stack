from flask import Flask 
app = Flask(__name__) 
@app.route('/') 
def Hello():
    return ("Hello World !")

@app.route('/dojo')
def dojo():
    return("Dojo!")


@app.route("/say/<name>")
def pattren(name):
    return (f"Hi {name} ! ")

@app.route("/repeat/<number>/<word>")
def repeat(word,number):
    return word*int(number)



if __name__=="__main__":    
    app.run(debug=True) 