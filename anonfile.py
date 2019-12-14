import requests

def upload_file(file):
    file = {
        'file': (file, open(file, 'rb')),
    }
    req = requests.post('https://api.anonfile.com/upload', files=file)
    try:
        req = req.json()
        return req
    except:
        return False

def get_file_info(id):
    req = requests.get('https://api.anonfile.com/v2/file/{}/info'.format(id))
    try:
        req = req.json()
        return req
    except:
        return False