from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/rabbit')
def rabbit_info():
    return {
      "name": "Cream",
      "age": 2,
      "color": "White",
      "likes": "Lettuce"
    }

if __name__ == "__main__":
    app.run(debug=True)
