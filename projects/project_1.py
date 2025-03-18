import requests

def check_endpoint(url , timout=5):
    try:
        response = requests.get(url, timeout=timout)
        response.raise_for_status()
        return f"Endpoint {url} is reachable. \nStatus Code:{response.status_code}\n"
    except requests.exceptions.Timeout:
        return f"Timeout: The request to {url} took longer than {timout} seconds.\n"
    except requests.exceptions.ConnectionError:
        return f"Connection Error: could not connect to {url}. \nPlease check the network.\n"
    except requests.exceptions.HTTPError as e:
        return f"HTTP Error:{url} returned status code: {response.status_code}.\nError:{e}\n"
    except requests.exceptions.RequestException as e:
        return f"Unexpected Error: {e}\n"
    

# Endpoints
endpoints = [
    "https://www.oogle.com",
     "https://www.google.com"
]

for url in endpoints:
    print(check_endpoint(url))