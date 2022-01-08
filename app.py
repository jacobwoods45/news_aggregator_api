from flask import Flask, request
from flask_restful import Api
import database_handler
from flask_cors import CORS, cross_origin

app = Flask(__name__)
api = Api(app)

app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/get_current_news", methods =["GET"])
@cross_origin()
def insert_link():
    database_handler.insert_link(link, date, device)
    response = {
        "status": "success"
    }
    return response




if __name__ == '__main__':
    app.run(debug=True)