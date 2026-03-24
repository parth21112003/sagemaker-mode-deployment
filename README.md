STEP 1: CREATE S3 BUCKET & UPLOAD DATA
Go to AWS S3
Click Create bucket
Give name (e.g., parth-model)
Keep region same (e.g., ap-south-1)
Create bucket

👉 Open bucket
👉 Click Upload
👉 Upload:

data.csv
later: model.tar.gz
🔐 STEP 2: CREATE IAM ROLE FOR SAGEMAKER
Go to IAM → Roles → Create Role
Select:
AWS Service → SageMaker
Attach policies:
AmazonSageMakerFullAccess
AmazonS3FullAccess
Name:
SageMakerExecutionRole
Create role
🧠 STEP 3: CREATE SAGEMAKER NOTEBOOK
Go to SageMaker
Open Studio / Notebook Instances
Create new notebook
Attach:
SageMakerExecutionRole

👉 Inside notebook:

Load data from S3
Train model
Save model
Upload model (model.tar.gz) to S3
🚀 STEP 4: DEPLOY MODEL (SAGEMAKER ENDPOINT)

Inside SageMaker:

Create model using:
S3 model path
inference script
Deploy model:
Instance type: ml.t2.medium
Wait until:
Status = InService

👉 Now model is live internally

🔐 STEP 5: CREATE IAM ROLE FOR LAMBDA
Go to IAM → Roles → Create Role
Select:
Lambda
Attach:
AmazonSageMakerFullAccess
AWSLambdaBasicExecutionRole
Name:
LambdaSageMakerRole
⚙️ STEP 6: CREATE LAMBDA FUNCTION
Go to AWS Lambda
Click Create function
Choose:
Author from scratch
Runtime:
Python 3.x
Attach role:
LambdaSageMakerRole

👉 Add code to:

Receive request
Call SageMaker endpoint
Return prediction

👉 Click Deploy

🧪 STEP 7: TEST LAMBDA
Click Test
Create test event
Send input data

👉 Check:

Response works
No errors
🌐 STEP 8: CREATE API GATEWAY
Go to API Gateway
Click Create API
Choose:
HTTP API
Add integration:
Select your Lambda function
Add route:
POST /predict
Create API
🚀 STEP 9: STAGE CONFIGURATION
Keep:
$default stage
Auto-deploy ON

👉 No changes required

🔗 STEP 10: GET API URL

You’ll get:

https://xxxxx.execute-api.ap-south-1.amazonaws.com

👉 Final endpoint:

https://xxxxx.execute-api.ap-south-1.amazonaws.com/predict
🧪 STEP 11: TEST API

Use:

ReqBin / Postman / frontend

Send:

POST request
JSON input

👉 Get prediction output
