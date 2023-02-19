from flask import Flask, render_template, request
import pickle

app=Flask(__name__)
model=pickle.load(open("BA_Model.pkl","rb"))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods=["POST"])
def predict():
    features=[x for x in request.form.values()]
    input=[]
    input.append(float(features[0]))
    input.append(float(features[1]))
    input.append((float(features[2])*float(features[3]))/float(features[4]))
    input.append(float(features[2])/float(features[5]))
    input_array=[]
    input_array.append(input)
    result=model.predict(input_array)
    return render_template("index.html",Result="Next Year,{}".format(result[0]))

    

if __name__=="__main__":
    app.run(debug=True)