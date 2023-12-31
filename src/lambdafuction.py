import json
import subprocess

def lambda_handler(event, context):

    records = event['Records'][0]['s3']
    bucket_name = records['bucket']['name']
    file_name = records['object']['key']
    process_data = 's3://' + bucket_name + '/' + file_name
    print("Current processing data " + process_data)
    endpoint = 'http://<your_EC2_external_ip>:8080/api/experimental/dags/emr_job_flow_manual_steps_dag/dag_runs'
    data = json.dumps({'conf': {'s3_location': process_data}})

    subprocess.run(['curl', '-X', 'POST', endpoint, '--insecure', '--data', data])
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')

    }