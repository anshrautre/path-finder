import os 
from flask import Flask,request,render_template
app=Flask(__name__)
@app.route('/',methods=["GET","POST"])
def a():
    if request.method == "POST":    
        name=request.form.get("data")
        print("processing....")
        b=f"{name}.txt"
        data=os.popen(r"where /r c:\ "+b).read()
        d1=data.split("\n")                
        if d1[0]==" ":
            print(f"Sorry there is no {name}.txt is in system")
            return f"Sorry there is no {name}.txt is in system"
        else:
            print(f"Your file path is \n{d1[0]}")
            return f"Your file path is \n{d1[0]}"
    return render_template("pathfinder.html")     
        
if __name__ == "__main__":
    app.run(host = "0.0.0.0", port = 5000, debug = True)