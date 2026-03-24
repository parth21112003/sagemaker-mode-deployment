import json
import boto3

runtime = boto3.client("sagemaker-runtime")

ENDPOINT_NAME = "sagemaker-scikit-learn-2026-03-24-06-51-15-415"

def lambda_handler(event, context):
    try:
        if "body" in event:
            body = json.loads(event["body"])
        else:
            body = event

        data = body.get("input")

        # ✅ FIX: convert to 2D array
        formatted_data = [data]

        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT_NAME,
            ContentType="application/json",
            Body=json.dumps(formatted_data)   # ✅ send [[...]]
        )

        result = json.loads(response["Body"].read().decode())

        return {
            "statusCode": 200,
            "body": json.dumps({"prediction": result})
        }

    except Exception as e:
        return {
            "statusCode": 500,
            "body": str(e)
        }
