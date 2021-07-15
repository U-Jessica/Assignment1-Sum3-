import json
from flask import Flask, render_template, request, jsonify   

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("InputOutput.html")    
    

@app.route("/submitJSON", methods=["POST"])
def processJSON(): 
    jsonStr = request.get_json()
    jsonObj = json.loads(jsonStr) 
    
    response = ""
    a=int(jsonObj['a'])
    b=int(jsonObj['b'])
    c=int(jsonObj['c'])
    d=[a,b,c]
    d.sort
    r=(d[1]+d[2])/1.4
    if (r>90):
        response+="<b> Grade:Ex</b><br>"
    elif(r<90 and r>=80):
        response+="<b> Grade:A</b><br>"
    elif(r<80 and r>=70):
        response+="<b> Grade:B</b><br>" 
    elif(r<70 and r>=55):
        response+="<b> Grade:C</b><br>"  
    elif(r<55 and r>=40):
        response+="<b> Grade:Pass</b><br>" 
    else:
        response+="<b> Grade:Fail</b><br>" 	
    
      
    return response
    
    
if __name__ == "__main__":
    app.run(debug=True)
    
    
