#def add_questions():
#    Dict={}
#    optionList=[]   
#    ques=input('Enter Your Question:')
#    for i in range(3):
#        option=input('Enter Your option:')
#        optionList.append(option)
#    ans=input('Please enter correct answer:')
#    Dict.update({'Question':ques})
#   Dict.update({'Options':optionList})
#    Dict.update({'Answer':ans})
#   return Dict

class Capture():
    @staticmethod
    def add_questions():
        Dict={}
        optionList=[]   
        ques=input('Enter Your Question:')
        for i in range(3):
            option=input('Enter Your option:')
            optionList.append(option)
        ans=input('Please enter correct answer:')
        Dict.update({'Question':ques})
        Dict.update({'Options':optionList})
        Dict.update({'Answer':ans})
        return Dict