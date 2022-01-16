import os
import pdftables_api
import functions_framework
import requests
import base64

url = "https://pdftables.com/api"

@functions_framework.http
def parsePDF(request):
    json_data = request.get_json()
    if request.args and 'pdf-data' in request.args:
        pdfdata = base64.b64decode(request.args.get('pdf-data'))
    elif json_data and 'pdf-data' in json_data:
        # Get the PDF data and deocde it
        pdfdata = base64.b64decode(json_data['pdf-data'])
    
    # secret key for api, and format we want the returned file in
    params = (
    ('key', 'API KEY'),
    ('format', 'csv'),
    )
    # our data we send the api
    files = {
    'f': (pdfdata),
    }
    
    # sending and recv the request & response
    response = requests.post('https://pdftables.com/api', params=params, files=files)

    
    # return the csv file
    # return response.content
    
    # parse the response
    codePrice = {}
    for s in response.text.split('\n'):
        if(',,' in s or "Code" in s or s == ''):
            continue
        t = s.split('$')
        if(len(list(t)) == 1):
            continue
        code = t[0][:5] # First 5 characters are the code
        price = t[1] # The price is what is left
        codePrice[code] = price
    # return response.text
    return str(codePrice) # return a string representation of the dictionary

