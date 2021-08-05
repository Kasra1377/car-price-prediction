from flask import Flask , render_template , request
import pickle

app =Flask(__name__ , template_folder="templates")

model = pickle.load(open("car-price-prediction-model.pkl", 'rb'))

@app.route("/home" , methods=["GET" , "POST"])
def home():
    output = 0
    if request.method == "POST":
        
        present_price = float(request.form["present_price"])
        kms_driven = float(request.form["kms_driven"])
        year = int(request.form["year"])
        fuel_type = request.form["fuel_type"]
        seller_type = request.form["seller_type"]

        if fuel_type == "Petrol":
            fuel_type = 171
        elif fuel_type == "Diesel":
            fuel_type = 33
        else:
            fuel_type = 1
        
        if seller_type == "Dealer":
            seller_type = 128
        else:
            seller_type = 77
        # print(present_price , kms_driven , year , fuel_type , seller_type)

        prediction = model.predict([[year , present_price , kms_driven , fuel_type , seller_type]])
        output = round(prediction[0] , 2)

    
    return render_template("templates.html" , output = output)    

if __name__=="__main__":
    app.run(debug=True)