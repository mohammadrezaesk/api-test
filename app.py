from flask import Flask

app = Flask(__name__ ,static_folder="./" ,static_url_path='/static/')

@app.route("/small" , methods=["GET","POST"])
def small():
    return app.send_static_file("small.json")

@app.route("/medium" , methods=["GET","POST"])
def medium():
    return app.send_static_file("medium.json")   

@app.route("/big" , methods=["GET","POST"])
def big():
    return app.send_static_file("big.json")

if __name__ == "__main__":
    app.run(debug=True)