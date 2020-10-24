from flask import Flask,render_template,request

app=Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    Email = request.args.get('mail')
    return render_template('index.html')

@app.route("/auth")
def auth():
    with open('auth.txt', 'w') as f:
        f.write('True')
    return 'Authontication Done!'

@app.route("/auth_checking")
def auth_checking():
    with open('auth.txt', 'r') as f:
        content = f.read()
    return content

@app.route("/data")
def auth_done():
    return 'Welcome to your Account!'

@app.route("/logout")
def logout():
    with open('auth.txt', 'w') as f:
        f.write('False')
    return 'logout Done!'

if __name__ == "__main__":
    app.run(debug=True)