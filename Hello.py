from chait import captureData
from flask import Flask,render_template,request
app = Flask(__name__)

#holdList will hold all captured data
holdList=[] 
#answerList will hold list of correct answers
answerList=[]

def capture_answerlist_holdlist():
    d={}
    #for i in range(2):
    #    classobject = captureData.Capture()
    #    d = classobject.add_questions()
    #    answerList.append(d['Answer'])
    #    holdList.append(d)
    add_more_ques=input('would you like to add more questions:')
    if add_more_ques=='N':
        d ={'Question':'Emerson innovation center located in:','Options':['Mumbai','Pune','Chennai'],'Answer':'Pune'}
        answerList.append(d['Answer'])
        holdList.append(d)
    else:    
        number_of_ques=int(input('Enter total number of questions:'))
        for i in range (number_of_ques):
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
    #responselist is list of captured responses from user
    responselist=[]
    #first=request.form['0']
    #second=request.form['1']
    #if answerList[0]==first:
    #    counter=counter+1
    #if answerList[1]==second:
     #   counter=counter+1
    #return render_template('result.html',s=counter)
    for i in range(len(answerList)):
        response=request.form[str(i)]
        responselist.append(response)
    for i in range(len(responselist)):
        if answerList[i]==responselist[i]:
            counter=counter+1
    return render_template('result.html',s=counter)

if __name__ == "__main__":
    capture_answerlist_holdlist()
    app.run()
