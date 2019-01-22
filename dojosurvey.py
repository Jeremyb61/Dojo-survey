from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def dojo():
    return render_template('dojosur.html')

@app.route("/result", methods=['POST'])
def create():
    print(request.form)
    print('Name', request.form['name'])
    print('Email', request.form['email'])
    return render_template('created.html')

@app.route("/danger")
def danger():
    print("A user tried to visit /danger.  We have redirected the user to /")
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)