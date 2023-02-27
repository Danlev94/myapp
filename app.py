from flask import Flask,Response,jsonify, render_template ,logging,request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

#run server
if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)),host='0.0.0.0',debug=True)