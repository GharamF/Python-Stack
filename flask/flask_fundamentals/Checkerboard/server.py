from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/') 
def index():
    return render_template('index.html',colum= 4 ,row=4 )

@app.route('/<colum>')
def colum(colum,):
    return render_template('index.html', colum= int(colum) , row = 4)


@app.route('/<colum>/<row>')
def row(colum,row):
    return render_template('index.html', colum= int(colum) , row= int(row) )

@app.route('/<colum>/<row>/<color1>/<color2>')
def color1(colum,row ,color1,color2):
    return render_template('index.html', colum= int(colum) , row= int(row) , color1=color1,color2=color2)



if __name__=="__main__":
    app.run(debug=True) 