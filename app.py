from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

st=''

class inputform(FlaskForm):
      #c1n=StringField("Compound 1 Nature")
      c1a=StringField("Compound 1 amount (in gm or ml)")
      c1m=StringField("Compound 1 MW")
      c1d=StringField("Compound 1 Density (in gm/ml)")
      #c2n=StringField("Compound 2 Nature")
      c2m=StringField("Compound 2 MW")
      c2d=StringField("Compound 2 Density (in gm/ml)")
      c2r=StringField("'Compound 1 : Compound 2 = 1:'")
      submit=SubmitField("Submit")

def convert(c1n,c1a,c1m,c1d,c2m,c2r,c2n,c2d):
    if  c1n=='Solid1':
        m1=c1a/c1m
    elif c1n=='Liquid1':
        a=(c1a*c1d)
        m1=a/c1m
    if  c2n=='Solid2':
        req=m1*c2m*c2r
        #print('Required amount of Compound 2: '+ str(c2a)+' in gm')
    elif c2n=='Liquid2':
        req=(m1*c2m*c2r)/c2d
        #print('Required amount of Compound 2: '+ str(c2a)+' in ml')
    return req

#convert(c1n,c1a,c1m,c1d,c2m,c2r,c2n,c2d)
@app.route("/", methods=["GET","POST"])
def index():
    input=inputform()
    strn=''
    c1a,c1m,c1d,c2m,c2d,c2r='','','','','',''
    if request.method == 'POST':
       if request.form['c1n']=='Solid':
          c1n='Solid1'
       elif request.form['c1n']=='Liquid':
          c1n='Liquid1'

       if request.form['c2n']=='Solid':
          c2n='Solid2'
       elif request.form['c2n']=='Liquid':
          c2n='Liquid2'
       #if input.validate_on_submit():
       strn=strn+str(convert(str(request.form["c1n"]),float(request.form["c1a"]),float(request.form["c1m"]),float(request.form["c1d"]),
       float(request.form["c2m"]),float(request.form["c2r"]),str(request.form["c2n"]),float(request.form["c2d"])))
       print(request.form["c2m"])
       print(request.form["c2r"])
       print(request.form["c2n"])
       print(request.form["c2d"])
       #print(strn)
    return render_template('index.html', template_form=input, template_list=strn)


if __name__=="__main__":
   app.run(debug=True)
