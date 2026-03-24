# 🚀 ML Model Deployment on AWS (SageMaker + Lambda + API Gateway)

## 📌 Overview

This project demonstrates how to deploy a Machine Learning model on AWS and expose it as a public API.

### 🔁 Architecture

```
User → API Gateway → Lambda → SageMaker Endpoint → ML Model
```

---

## 📦 Step 1: Create S3 Bucket

1. Go to **AWS S3**
2. Click **Create Bucket**
3. Provide a unique name (e.g., `parth-model`)
4. Select region (e.g., `ap-south-1`)
5. Create bucket

### Upload Files:

* Upload dataset (`data.csv`)
* Upload trained model (`model.tar.gz`)

---

## 🔐 Step 2: Create IAM Role for SageMaker

1. Go to **IAM → Roles → Create Role**
2. Select **AWS Service → SageMaker**
3. Attach policies:

   * `AmazonSageMakerFullAccess`
   * `AmazonS3FullAccess`
4. Name the role:

   * `SageMakerExecutionRole`
5. Create role

---

## 🧠 Step 3: Create SageMaker Notebook

1. Open **SageMaker Studio / Notebook Instances**
2. Create a new notebook
3. Attach `SageMakerExecutionRole`

### Inside Notebook:

* Load dataset from S3
* Train ML model
* Save model as `.joblib`
* Convert to `model.tar.gz`
* Upload model to S3

---

## 🚀 Step 4: Deploy Model (SageMaker Endpoint)

1. Create model using:

   * Model file from S3
   * Inference script
2. Deploy model:

   * Instance type: `ml.t2.medium`
3. Wait until status becomes:

   ```
   InService
   ```

---

## 🔐 Step 5: Create IAM Role for Lambda

1. Go to **IAM → Roles → Create Role**
2. Select **Lambda**
3. Attach policies:

   * `AmazonSageMakerFullAccess`
   * `AWSLambdaBasicExecutionRole`
4. Name the role:

   * `LambdaSageMakerRole`

---

## ⚙️ Step 6: Create Lambda Function

1. Go to **AWS Lambda**
2. Click **Create Function**
3. Choose:

   * Author from scratch
4. Runtime:

   * Python 3.x
5. Attach role:

   * `LambdaSageMakerRole`

### Function Purpose:

* Accept request input
* Call SageMaker endpoint
* Return prediction response

---

## 🧪 Step 7: Test Lambda

1. Create test event
2. Send sample input
3. Verify response
4. Check logs if errors occur

---

## 🌐 Step 8: Create API Gateway

1. Go to **API Gateway**
2. Click **Create API**
3. Choose:

   * HTTP API
4. Add integration:

   * Select Lambda function
5. Add route:

   ```
   POST /predict
   ```
6. Create API

---

## 🚀 Step 9: Configure Stage

* Use default stage:

  ```
  $default
  ```
* Keep:

  ```
  Auto-deploy: ON
  ```

---

## 🔗 Step 10: Get API Endpoint

Example:

```
https://xxxxx.execute-api.ap-south-1.amazonaws.com/predict
```

---

## 🧪 Step 11: Test API

Use tools like:

* ReqBin
* Postman

### Request:

* Method: POST
* Content-Type: application/json
* Body:

```
{
  "input": [values]
}
```

### Response:

```
{
  "prediction": [result]
}
```

---

## ⚠️ Common Issues

* **403 Forbidden** → Check permissions / authorization
* **404 Not Found** → Route not created
* **405 Method Not Allowed** → Use POST instead of GET
* **500 Internal Server Error** → Input format or inference issue
* **Access Denied** → Missing IAM permissions

---

## 💰 Cleanup (Important)

To avoid AWS charges:

* Delete SageMaker endpoint
* Delete unused Lambda functions
* Delete API Gateway (if not needed)

---

## 🎯 Final Architecture

```
User → API Gateway → Lambda → SageMaker → Model → Response
```

---

## 📚 Key Services Used

* Amazon S3
* AWS SageMaker
* AWS Lambda
* API Gateway
* IAM

---

## ✅ Outcome

* ML model deployed successfully
* Public API created
* Predictions accessible via HTTP requests

---
