from flask import Flask , request , jsonify
from data import data
app = Flask(__name__)
@app.route("/")
def show_all_data():
    return jsonify({
        "data":data,
        "message":"SUCCESS"
    }),200
if __name__ == "__main__":
    app.run()