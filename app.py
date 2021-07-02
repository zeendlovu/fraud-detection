from flask import Flask, render_template, request
import model
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def func():
    if request.method == 'POST':
        V1 = request.form['V1']
        V2 = request.form['V2']
        V3 = request.form['V3']
        V4 = request.form['V4']
        V5 = request.form['V5']
        V6 = request.form['V6']
        V7 = request.form['V7']
        V8 = request.form['V8']
        V9 = request.form['V9']
        V10 = request.form['V10']
        V11 = request.form['V11']
        V12 = request.form['V12']
        V13 = request.form['V13']
        V14 = request.form['V14']
        V15 = request.form['V15']
        V16 = request.form['V16']
        V17 = request.form['V17']
        V18 = request.form['V18']
        V19 = request.form['V19']
        V20 = request.form['V20']
        V21 = request.form['V21']
        V22 = request.form['V22']
        V23 = request.form['V23']
        V24 = request.form['V24']
        V25 = request.form['V25']
        V26 = request.form['V26']
        V27 = request.form['V27']
        V28 = request.form['V28']
        amount = request.form['amount']
        
        array = [V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,amount]
        array = pd.to_numeric(array)
        result = model.dtc.predict([array])
        print(result)
        
        return render_template(output=result)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
