# I - Endpoint Checker

### Overview
This Python script checks the availability of a given list of endpoints (URLs) and gracefully handles exceptions to prevent crashes. It provides detailed status messages for each request, making it useful for monitoring web services and APIs.

#### Features

  - **Checks endpoint availability** using HTTP requests
  - **Handles exceptions gracefully**,including timeouts, connection errors, and HTTP errors

#### Installation
##### Prerequisites
Ensure to  have Python installed and also needs the **requests** library:

```
pip install requests

```

# II - QR Code Generator
This is a simple Python script that generates QR codes from a given message or URL and saves the output as an image file. The script utilizes the argparse module to handle command-line arguments for input.

## Features

 - Generates QR codes from text or URLs.

 - Saves QR codes as image files.

 - Simple command-line interface using argparse.

##### Prerequisites
Ensure you have Python installed (Python 3 recommended) and  also need the **qrcode** module, which can be installed using pip:

```
pip install qrcode

```
#### Usage
Run the script using the command line with the required arguments:

```
python script.py "<message_or_url>" "<output_filename.png>"

```

##### Example: 

```
python script.py "https://linux.com" "qrcode.png"

```
This will generate a QR code for ****https://example.com** and save it as **qrcode.png**.