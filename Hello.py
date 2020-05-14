from InputData import captureData
from flask import Flask,render_template,request
app = Flask(__name__)

#d1={}
#res=int(input('Enter choice:'))
#for i in range (res):
#d1=captureData.add_questions()

#d2={}
#d2=captureData.add_questions()

d={}
holdList=[]
answerList=[]
for i in range(2):
    d = captureData.add_questions()
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
def getInput():
    counter=0
    first=request.form['0']
    second=request.form['1']
    print(first)
    print(answerList[0])
    if answerList[0]==first:
        counter=counter+1
    if answerList[1]==second:
        counter=counter+1
    return render_template('result.html',s=counter)




if __name__ == "__main__":
    app.run()
