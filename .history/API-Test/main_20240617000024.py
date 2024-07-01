from flask import Flask, request , jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home"
    
if__name__ == "__main__":
    app.run(debug = True)

@app.route('/api', methods=['POST'])