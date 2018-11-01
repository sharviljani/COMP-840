from flask import Flask, render_template, Response, request, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/hello', methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
        return redirect(url_for('index'))

    return render_template('hello.html')

if __name__ == "__main__":
    app.run(debug = True)