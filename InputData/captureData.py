#def add_questions():
#    Dict={}
#    optionList=[]   
#    ques=input('Enter Your Question:')
#    for i in range(3):
#       option=input('Enter Your option:')
#        optionList.append(option)
#   print(optionList)
#   ans=input('Please enter correct answer:')
#   Dict['a']=ques
#   Dict['b']=optionList
#   Dict['c']=ans
#   return Dict

def add_questions():
    Dict={}
    optionList=[]   
    ques=input('Enter Your Question:')
    for i in range(3):
        option=input('Enter Your option:')
        optionList.append(option)
    print(optionList)
    ans=input('Please enter correct answer:')
    Dict.update({'Question':ques})
    Dict.update({'Options':optionList})
    Dict.update({'Answer':ans})
    return Dict