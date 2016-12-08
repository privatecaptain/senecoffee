from flask import Flask,render_template,request,make_response,redirect,url_for,session


app = Flask(__name__) #,static_url_path="/static")
app.debug = True
