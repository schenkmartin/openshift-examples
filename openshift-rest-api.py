#!/usr/bin/python3
import requests
import argparse

def send_request(url, method, bearer_token, file_path=None):
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Accept': 'application/yaml',
        'Content-Type': 'application/yaml',
    }
    
    # If a file is provided, open it and send it in the request body
    if file_path:
        with open(file_path, 'rb') as file:
            if method.upper() == 'PUT':
                response = requests.put(url, headers=headers, verify=False, data=file)
            elif method.upper() == 'POST':
                response = requests.post(url, headers=headers, verify=False, data=file)
            elif method.upper() == 'GET':
                response = requests.get(url, headers=headers, verify=False, data=file)
            else:
                print(f"Unsupported method: {method}")
                return
    else:
        # If no file is provided, just send an empty body with the request
        if method.upper() == 'PUT':
            response = requests.put(url, headers=headers)
        elif method.upper() == 'POST':
            response = requests.post(url, headers=headers)
        elif method.upper() == 'GET':
            response = requests.get(url, headers=headers)
        else:
            print(f"Unsupported method: {method}")
            return

    # Print response details
    if response.status_code == 200:
        print(f"Request successful! Response code: {response.status_code}\n{response.text}")
    else:
        print(f"Failed request. Response code: {response.status_code}, Error: {response.text}")

def main():
    # Set up argument parsing
    parser = argparse.ArgumentParser(description="Send HTTP request (PUT/POST/GET) with optional file upload")
    parser.add_argument("url", help="URL to send the request")
    parser.add_argument("bearer_token", help="Bearer token for authorization")
    parser.add_argument("method", choices=['PUT', 'POST','GET'], help="HTTP method (PUT or POST or GET)")
    parser.add_argument("--file", help="Path to the file to upload (optional)", default=None)
    
    args = parser.parse_args()

    # Call the function to send the request
    send_request(args.url, args.method, args.bearer_token, args.file)

if __name__ == "__main__":
    main()

