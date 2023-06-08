
from flask import Flask,render_template,request, redirect, url_for, jsonify
import json
import requests
import mysql.connector
import time
import json
import urllib, base64
import threading

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    print("pagina inicial iniciada")
    return render_template("index.html")

@app.route("/config_email", methods=["POST"])
def config_email():
    fullnam = request.form["fullname"]
    email = request.form['email_address']
    mbnumber = request.form['mobile_number']
    subject = request.form['email_subject']
    message = request.form['your_message']

    conn = mysql.connector.connect(
    host='srv952.hstgr.io',
    database='u663647989_zeus',
    user='u663647989_matheus',
    password='#Luis454049'
    )
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO emails (full_name, email_address, mobile_number, email_subject, your_message)VALUES ('"+fullnam+"', '"+email+"', '"+mbnumber+"', '"+subject+"', '"+message+"');")
    conn.commit()
    cursor.close()
    return redirect('/')
    
    
app.run(debug=True)