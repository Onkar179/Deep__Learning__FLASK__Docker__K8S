from flask import Flask, render_template, request

app = Flask("lwapp")


from keras.models import load_model

model = load_model('/root/dl_model.h5')

@app.route("/")
def home():
    return render_template("form.html")



@app.route("/result" , methods=[ "GET" ])
def result():
        x1 = request.args.get("x1")
        x2 = request.args.get("x2")
        x3 = request.args.get("x3")
        x4 = request.args.get("x4")
        x5 = request.args.get("x5")
        x6 = request.args.get("x6")
        x7 = request.args.get("x7")
        x8 = request.args.get("x8")
        result = model.predict([[ x1 , x2 , x3 , x4 , x5 , x6 , x7 , x8 ]])
        if round(result[0][0]) == 0:
            return "You are safe"
        else:
            return "You are not safe"


app.run(port=1111, host='0.0.0.0')


