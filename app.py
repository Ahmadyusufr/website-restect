from flask import Flask, render_template
app = Flask(__name__)

@app.route('/home')
def home():
    
   return render_template('home.html')

@app.route('/data')
def data():
    
   return render_template('data.html')

@app.route('/control')
def control():
    
   return render_template('control.html')

if __name__ == '__main__':
   app.run(debug=True)