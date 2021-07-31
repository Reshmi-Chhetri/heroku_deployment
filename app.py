# import a library

from flask import Flask, render_template, request
import joblib

# instance of an app
app = Flask(__name__)

model = joblib.load('diabetes.pkl')

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/blog', methods= ['POST'])
def contact():
    a = request.form.get('preg')
    b = request.form.get('plas')
    c = request.form.get('pres')
    d = request.form.get('skin')
    e = request.form.get('test')
    f = request.form.get('mass')
    g = request.form.get('pedi')
    h = request.form.get('age')
   

    pred = model.predict([[int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)]])

    if pred[0] == 1:
         output = 'diabetic'
    else:
         output = 'not diabetic'

    return render_template('blogs.html', predicted_text = f'The person is {output}')
    


# run the app
if __name__ == '__main__':
    app.run(debug= True)