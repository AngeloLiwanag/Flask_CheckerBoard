from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def checkerboard():
    return render_template('index.html', num1=8, num2=8)

@app.route('/<x>')
def checkerboard2(x):
    return render_template('index.html', num1=8, num2=int(x))

@app.route('/<x>/<y>')
def checkerboard3(x,y):
    return render_template('index.html', num1=int(y), num2=int(x))

if __name__ == "__main__":
    app.run(debug = True)