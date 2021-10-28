from flask import *
import json, boto3

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home_page():
    json_dump = json.dumps({'message': 'Flugel assessment home page'})

    return json_dump


@app.route('/tags', methods=['GET'])
def tags():
    ec2_instance = boto3.client("ec2")
    json_dump = json.dumps({'instance': ec2_instance.decribe_instances()})

    return json_dump


if __name__ == '__assessment__':
    app.run(port=7777)