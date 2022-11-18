from flask import Flask, render_template
# website 
app = Flask(__name__)

@app.route("/")
def home():
    print("PBR.Init()")
    print("PBR.ResetEpo()")
    print("PBR.MotorsOff()")
    return render_template('index.html')
@app.route("/for")
def forward():
    print("PBR.SetMotor1(+maxPower)")
    print("PBR.SetMotor2(+maxPower)")
    return render_template("for.html")
@app.route("/back")
def backward():
    print("PBR.SetMotor1(-maxPower)")
    print("PBR.SetMotor2(-maxPower)")
    return render_template("back.html")
@app.route("/clock")
def clock():
    print("PBR.SetMotor1(+maxPower)")
    print("PBR.SetMotor2(-maxPower)")
    return render_template("clock.html")
@app.route("/anticlock")
def anti():
    print("PBR.SetMotor1(-maxPower)")
    print("PBR.SetMotor2(+maxPower)")
    return render_template("anti.html")
@app.route("/stop")
def stop():
    print("PBR.MotorsOff()")
    return render_template("stop.html")
#redirect(url_for("home"))
#local variable can be change to 0.0.0.0 or localhost
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port='80' , debug = True)