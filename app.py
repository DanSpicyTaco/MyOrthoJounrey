from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/doctorQuestionare', methods=["GET", "POST"])
def doctorQs():
    if(request.method == 'POST'):
        name = request.form['Pname']
        dob = request.form['birthdate']
        oLocation = request.form['Operationlocation']
        sDate = request.form['surgery_date']
        return render_template('confirm.html', name=name, dob=dob, oLocation=oLocation, sDate=sDate)

    return render_template('Doctor_Questionare.html')

@app.route('/physioQuestionares')
def physioQs():
    return render_template('Physio_Questionare.html')

@app.route('/patients', methods=["GET", "POST"])
def patients():
    if(request.method == 'POST'):
        PID = request.form['PID']
        return render_template('patient.html', patient=True, PID=PID)

    return render_template('patient.html', patient=False)

if __name__ == '__main__':
    app.run()
