from website import app
from flask import render_template,redirect, url_for,request
from website.forms import DataForm
import tensorflow as tf
import pandas as pd


@app.route('/')
@app.route('/home', methods = ["GET","POST"])
def home_page():
    model = tf.keras.models.load_model("my_model.h5")
    result = -1
    if request.method == "POST":
        data_form = dict(request.form)
        for i in data_form.copy():
            data_form[i] = float(data_form[i])
        df = pd.DataFrame([data_form])
        result = model.predict(df)
        result = int(result[0][0])
        print (result)


    return render_template('index.html',result = result)

@app.route('/blog')
def blog_page():
    return render_template('here.html')
