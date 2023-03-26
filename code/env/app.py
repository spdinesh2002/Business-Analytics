from flask import Flask, render_template, request
import pickle

app=Flask(__name__)
model=pickle.load(open("BA_Model.pkl","rb"))

@app.route('/')
def index():
    return render_template('index.html')
 

@app.route('/form')
def form():
    return render_template('form.html')

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
    if result[0]=="Revenue will decrease,offer sale promotions to boost the volume of sales":
        output_message="Focus on your customers, increase your marketing and sales efforts, review your pricing strategies, and expand your market to increase revenue for your company."
        return render_template("form.html",Result="{}".format(output_message))
    elif result[0]=="Revenue will increase":
        output_message="The revenue will rise. Develop new product or service lines, sell more to current clients, and run sales campaigns to increase volume of sales."
        return render_template("form.html",Result="{}".format(output_message))
    elif result[0]=="Sales price will decrease,concentrate on right taget":
        output_message="Sales prices will fall as the number of customers grows. Increase the size of the average transaction. Boost the number of transactions per customer. Increase your prices."
        return render_template("form.html",Result="{}".format(output_message))
    else:
        output_message="loss of income. in order to earn more Establish a budget, Pay attention to your profit margins, Review the profitability of your company. benchmark the performance of your business, evaluate the success of cost-management initiatives, Assess business productivity. Create fresh business strategies."
        return render_template("form.html",Result="{}".format(output_message))

    

if __name__=="__main__":
    app.run(debug=True)