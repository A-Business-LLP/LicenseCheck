from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from crud import get_robot_status


app = Flask(__name__)
api = Api(app)


class CheckLicense(Resource):
    def post(self):
        data = request.get_json()
        robot_id = data.get('id')

        if robot_id is None:
            return jsonify({"error": "No ID provided"}), 400

        status = get_robot_status(robot_id)
        
        if status is None:
            return jsonify({"error": "Robot not found"}), 404

        return jsonify({"status": status})


api.add_resource(CheckLicense, '/robot_status')


if __name__ == '__main__':
    app.run(debug=True)
