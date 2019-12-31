import hashlib

def loadData(gender):
    personalities = []
    filename = "male_personality.data" if gender == "male" else "female_personality.data"
    with open(filename,"r") as f:
        data = f.read()
        data = data.splitlines()
        sets = int(len(data)/5)
        for i in range(5):
            personalities.append(data[0:sets])
            data = data[sets:]
        return personalities


def generatePersonality(name,gender,age,personalities):
    lower_name = str(name).lower()
    superkey = f"{lower_name}-{gender}-{age}" #sanjay-male-20
    hashstr = hashlib.sha1(str.encode(str(superkey))).hexdigest() 
    hashstrarr = [x for x in hashstr] 
    hashkeys = list(filter(lambda x:x.isnumeric(),hashstr)) 
    hashkeys = hashkeys[:5] #33277
    if len(hashkeys) < 5: #may never be called... probability : 1/1000000... just handling errors here
        left = (5-len(hashkeys))
        for i in range(left):
            hashkeys.append(0)
    hashkeys = [int(x) - 1 for x in hashkeys] #22166
    personalityStr = ""
    for i,e in enumerate(hashkeys):
        personalityStr += personalities[i][e]
        if not i == len(hashkeys)-1:
            personalityStr = personalityStr.replace(".",", ")
    replacement = {"him":name,"He":name,"her":name,"She":name}
    for k,v in replacement.items():
        personalityStr = personalityStr.replace(k,v)
    return personalityStr