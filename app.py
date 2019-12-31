from flask import Flask, redirect, url_for, request, abort,Response,json
import chrsma as ch

app = Flask(__name__)

male_personality = ch.loadData("male")
female_personality = ch.loadData("female")

@app.route('/')
def server_check():
   return "SERVER CHECK OK"


def errorResponse(message):
        return json.dumps({
                "success":False,
                "data":None,
                "message":message
            })

@app.route('/api/getchrsma')
def chrsma():
    name = str(request.args.get('name'))
    gender = str(request.args.get('gender'))
    age = str(request.args.get('age'))
    if name == 'None' or name.strip() == "":
        return errorResponse("invalid name")
    if gender == 'None' or gender.strip() == "" or not (gender.strip() == "male" or gender.strip() == "female"):
        return errorResponse("invalid gender")
    if age == 'None' or age.strip() == "" or (not age.isnumeric()) or (int(age) < 5 or int(age) > 100):
        return errorResponse("invalid age")
    #all test passed
    reponseStr = ch.generatePersonality(name,gender,age,personalities=male_personality if gender=="male" else female_personality)
    return json.dumps({
            "success":True,
            "data":reponseStr,
        })
        



if __name__ == '__main__':
    app.run()



