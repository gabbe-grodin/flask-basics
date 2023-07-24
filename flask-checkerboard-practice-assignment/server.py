from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_sq():
    return render_template("index.html", x=8, y=8)

@app.route('/<int:x>')
def four_row_eight_col( x ):
    return render_template("index.html", x=x, y=8)

@app.route('/<int:x>/<int:y>')
def row_times_col( x, y):
    return render_template("index.html", x=x, y=y )

if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)