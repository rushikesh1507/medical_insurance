from flask import Flask, request, jsonify, render_template, redirect, url_for
from utils import MedicalInsurence
import config
import traceback

app = Flask(__name__)

@app.route('/')
def home1():
    
    return render_template('medical_insurence.html')

@app.route('/predict_charges', methods = ['POST'])
def predict_charges():
    try:
        if request.method == 'POST':
            print("*"*40)
            data = request.form.get
            print("Data :",data)
            age = int(data('age'))
            gender = data('gender')
            bmi = int(data('bmi'))
            children = int(data('children'))
            smoker = data('smoker')
            region = data('region')

            Obj = MedicalInsurence(age,gender,bmi,children,smoker,region)
            pred_price = Obj.get_predicted_price()
            
            
            return render_template('medical_insurence.html', prediction = pred_price)

    except:
        print(traceback.print_exc())
        return render_template('medical_insurence.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER,debug= False)
