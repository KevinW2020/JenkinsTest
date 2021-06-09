# Code to get wells from OSDU
import requests
import json
import boto3

################### Global Variables for Using OSDU APIs ###################

client_id = "1qauvrgthe5epi2elco6sdjolb"
osdu_platform_url = "https://389u8yyazd.execute-api.us-east-1.amazonaws.com"
secret_name = "osdu/AT"

# Code to get OSDU credentials from the SecretsManager
session = boto3.session.Session()
client = session.client(service_name="secretsmanager", region_name="us-east-1")
secret = client.get_secret_value(SecretId=secret_name)["SecretString"]
osdu_credentials = json.loads(secret)
access_token = osdu_credentials["OSDU_AT"]
print(access_token)
osdu_search_url = osdu_platform_url + "/api/search/v2/query/"
headers = {
    "Authorization": "Bearer " + access_token,
    "Content-Type": "application/json",
    "data-partition-id": "opendes",
}


def lambda_handler(event, context):
    print(event)
    cityList = {
        "London": {"longitude": -0.118092, "latitude": 51.509865,},
        "Amsterdam": {"longitude": 4.897070, "latitude": 52.377956},
        "Rotterdam":{"longitude":4.4777,'latitude':51.9244},
        "The Hague":{"longitude":4.3007, 'latitude':52.0705}
    }
    city = event["City"]
    print(city)
    long = cityList[city]["longitude"]
    lat = cityList[city]["latitude"]
    query = {
        "kind": "opendes:osdu:well-master:0.2.1",
        "spatialFilter": {
            "field": "data.GeoLocation",
            "byDistance": {
                "point": {"longitude": long, "latitude": lat},
                "distance": 150000,  # 50 km radius
            },
        },
        "limit": 1,
    }
    print("no issues with query structure")
    try:
        result = requests.post(osdu_search_url, headers=headers, json=query)
        print(result.json())
        print(result.json()["totalCount"])
        answer = str(result.json()["totalCount"])
    except:
        answer = "Unknown"
        print("Error: ", answer)
    response = {"statusCode": 200, "body": json.dumps(answer)}
    return response

