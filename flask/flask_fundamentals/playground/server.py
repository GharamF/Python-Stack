from flask import Flask  ,render_template  
app = Flask(__name__) 
@app.route('/') 


@app.route('/play')
def play():
    return render_template("play.html")


@app.route('/play/<num>')
def play_more(num):
    return render_template("play.html", number = int(num))

@app.route('/play/<num>/<color>')
def play_more_color(num,color):
    print(color)
    return render_template("play.html",number = int(num) , color=color )



if __name__=="__main__":
    app.run(debug=True) 