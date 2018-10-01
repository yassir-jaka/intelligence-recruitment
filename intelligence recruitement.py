import requests
import time
import threading
import msvcrt
def check():
    time.sleep(2)
    if text != None:
        return
    print("temps fini")

point=0
barre=30
domaine=["computer","technology","software","engineering"]

requis =["ingenieur","developpement web"]

print(" BONJOUR ,Presentez vous")
text=input()
text=text.replace(" ","%20")
r = requests.get('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text='+text+'.&features=sentiment,keywords', auth=('f5d6aceb-2a29-48a4-a658-892fa480926d', '4IhrKw27mXoI'))
dict=r.json()
usage=dict.get("usage","none")
number=usage.get("text_characters")
doc=dict.get("sentiment","none").get("document","none")
sentiment=doc.get("label","none")
score=doc.get("score","none")

#voir les sentiments 
if(sentiment=="positive"):
    point+=10*score
if(sentiment=="negative"):
    point-=5
if(number>200):
    point+=5



r = requests.get('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text='+text+'.&features=categories', auth=('f5d6aceb-2a29-48a4-a658-892fa480926d', '4IhrKw27mXoI'))
a=r.json()

#voir la correspandance avec les domaines
categories=a.get("categories","none")
nom=[]
scoring=[]
for i in categories:
    nom.append(i.get("label","none"))
    scoring.append(i.get("score","none"))
for i,str in enumerate(nom):
    for j in domaine:
        if j in str:
            point+=10*scoring[i]

print(point)
            
#-2 eme question
timeout = 5 # number of seconds your want for timeout
text= None
prompt=""
def direct_input():
    global text
    text=input()

class KeyboardThread(threading.Thread):
    def run(self):
        direct_input()
    def stop(self):
        self.stopped=True 
        
def raw_input_with_timeout(prompt, timeout=30.0):    
    global text
    print(prompt)
    finishat = time.time() + timeout
    it=KeyboardThread()
    it.start() 
    while True:
        if time.time() > finishat:
            it.stop()
            return text         
   

text=raw_input_with_timeout("quelles sont vos experiences et vos diplomes 120 sec",120)
print("temps termine")
if text!= None:
    text=text.replace(" ","%20")
    r = requests.get('https://gateway.watsonplatform.net/natural-language-understanding/api/v1/analyze?version=2017-02-27&text='+text+'.&features=keywords&keywords.limit=2&keywords.sentiment=true', auth=('f5d6aceb-2a29-48a4-a658-892fa480926d', '4IhrKw27mXoI'))
    a=r.json()
    keyword=a.get("keywords","none")
    competences=[]
    for i in keyword:
        competences.append(i.get("text","none"))
    
    for str in competences:
        for j in requis:
            if j in str:
                point+=5
        

print(point)