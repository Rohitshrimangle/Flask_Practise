## create a simple flask application

from flask import Flask,render_template,request,redirect,url_for

## create flask app

app=Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World<h1>'

@app.route('/welcome')
def welcome():
    return '<h1>Welcome to flask tutorial<h1>'

@app.route('/index')
def index():
    return render_template('index.html')
    #return redirect(url_for('index'))
    #return '<h1>Welcome to index page<h1>'

@app.route('/success/<int:score>')
def success(score):
    return "The person is passed and score is "+str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "The preson is failed and score is "+str(score)



@app.route('/calculate',methods=['POST','GET'])
def calculate():
    if request.method=="GET":
        return render_template('calculate.html')
    else:
        maths=float(request.form["maths"])
        science=float(request.form["science"])
        history=float(request.form["history"])

        average_marks=(maths+science+history)/3

        if average_marks>=50:
            result='success'
        else:
            result='fail'


        #return redirect(url_for(result,score=average_marks))

        return render_template('result.html',results=average_marks)




if __name__=='__main__':
    app.run(debug=True)