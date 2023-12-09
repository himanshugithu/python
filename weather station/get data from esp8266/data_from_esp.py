import requests
import time
target_ip = "192.168.0.102"


# Make an HTTP GET request to the specified IP address and endpoint
url = f"http://{target_ip}"
while True:
    try:
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            data = response.text
            print(f"Received data: {data}")
        else:
            print(f"Error in HTTP GET request. Status code: {response.status_code}")

    except requests.ConnectionError:
        print(f"Failed to connect to {url}")
    time.sleep(1)    
