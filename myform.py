import re
from bottle import post, request

@post('/home', method='post')

def my_form():
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    if((request.forms.get('ADRESS')=='')|(request.forms.get('QUEST')=='')):
        return "Please, put all information"
    else:
        if(re.match(r"^\w+@\w+(\.\w+)+$", mail)):
            mail = request.forms.get('ADRESS')
            return "Thanks, %s" % username+ "!The answer will be sent to the mail %s" % mail
        else:
            return "Please, put a correct email."