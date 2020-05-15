from chait import captureData
from flask import Flask,render_template,request
app = Flask(__name__)

#d1={}
#res=int(input('Enter choice:'))
#for i in range (res):
#d1=captureData.add_questions()

#d2={}
#d2=captureData.add_questions()

holdList=[]
answerList=[]

def capture_answerlist_holdlist():
    d={}
    for i in range(2):
        #d = captureData.add_questions()
        classobject = captureData.Capture()
        d = classobject.add_questions()
        answerList.append(d['Answer'])
        holdList.append(d)

@app.route('/')
def hello():
    return render_template('Login.html')

@app.route('/pass',methods=['POST'])
def getvalue():
    name=request.form['Name']   
    return render_template('pass.html',n=name)

@app.route('/quiz')
def getquiz():
    #return render_template('quiz.html',DictQuestion1=d1['Question'],DictOptions1=d1['Options'],DictQuestion2=d2['Question'],DictOptions2=d2['Options'])
    return render_template('quiz.html',containerList=holdList)

@app.route('/result',methods=['POST'])
def getinput():
    counter=0
    first=request.form['0']
    second=request.form['1']
    if answerList[0]==first:
        counter=counter+1
    if answerList[1]==second:
        counter=counter+1
    return render_template('result.html',s=counter)




if __name__ == "__main__":
    capture_answerlist_holdlist()
    app.run()
