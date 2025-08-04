import requests

# Replace this with your actual IAM Bearer token
mltoken = "your_IBM_cloud_token"

# Example input payload (replace with your actual fields and test values)
payload_scoring = {
    "input_data": [
        {
            "fields": ["voltage", "current", "phasor"],
            "values": [[230.0, 5.2, 0.98]]
        }
    ]
}

# Public endpoint from IBM Watson deployment
url = "https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/844683d5-2809-4351-84fb-1fb51ebd430c/predictions?version=2021-05-01"

# API call to get prediction
response = requests.post(
    url,
    json=payload_scoring,
    headers={"Authorization": "Bearer " + mltoken}
)

# Print the result
print("Scoring response:")
print(response.json())
