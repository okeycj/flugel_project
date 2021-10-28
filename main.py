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
    instance = ec2_instance.describe_instances()['Reservations'][0]['Instances'][0]['Tags']

    json_dump = json.dumps(instance)

    return json_dump


@app.route('/shutdown', methods=['GET'])
def shutdown():
    ec2_instance = boto3.client("ec2")
    instance_id = ec2_instance.describe_instances()['Reservations'][0]["Instances"][0]['InstanceId']
    stopped_instance = ec2_instance.stop_instances(InstanceIds=[instance_id])

    return stopped_instance


if __name__ == '__main__':
    app.run(port=7777)