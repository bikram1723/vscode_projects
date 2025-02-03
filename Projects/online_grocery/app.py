from flask import Flask, render_template # type: ignore

app = Flask(__name__)

#Routes to the home page
@app.route("/")
def home():
    return render_template('home.html')

#Routes to the products page
@app.route("/products")
def products():
    return render_template('products.html')

if __name__ == '__main__':
    app.run(debug=True)