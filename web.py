import PicoBorgRev3 as PicoBorgRev

voltageIn = 12.0
voltageOut = 6.0

if voltageOut > voltageIn:
    maxPower = 1.0
else:
    maxPower = voltageOut / float(voltageIn)
PicoBorgRev.ScanForPicoBorgReverse()
PBR = PicoBorgRev.PicoBorgRev()
PBR.Init()
PBR.ResetEpo()
PBR.MotorsOff()
# Reading parameters (after Init)
print (PBR.busNumber)                   # Shows which I²C bus the board is connected on
print (PBR.foundChip)                  # See if the board is found / not found


# website  
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    PBR.Init()
    PBR.ResetEpo()
    PBR.MotorsOff()
    return render_template('index.html')
@app.route("/for")
def forward():
    PBR.SetMotor1(+maxPower)
    PBR.SetMotor2(+maxPower)
    return render_template("for.html")
@app.route("/back")
def backward():
    PBR.SetMotor1(-maxPower)
    PBR.SetMotor2(-maxPower)
    return render_template("back.html")
@app.route("/clock")
def clock():
    PBR.SetMotor1(+maxPower)
    PBR.SetMotor2(-maxPower)
    return render_template("clock.html")
@app.route("/anticlock")
def anti():
    PBR.SetMotor1(-maxPower)
    PBR.SetMotor2(+maxPower)
    return render_template("anti.html")
@app.route("/stop")
def stop():
    PBR.MotorsOff()
    return render_template("stop.html")
#redirect(url_for("home"))
if __name__ == "__main__":
    app.run(host='0.0.0.0' , port='80' , debug = True)