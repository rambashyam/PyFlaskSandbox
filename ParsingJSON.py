# this is a test file for Parsing JSON request from an endpoint

import urllib
import json

import urllib.request
import json


def getresponse(url):
    # first get the content
    oper_url = urllib.request.urlopen(url)

    # if the url exists i.e. HTTP return code is 200
    if oper_url.getcode() == 200:
        # data will be the JSON file
        data = oper_url.read()
        # load the JSON file into a dict called json_data
        json_data = json.loads(data)
    else:
        print("Error receiving data", oper_url.getcode())
    return json_data


def main():
    urldata = "http://vocab.nic.in/rest.php/states/json"
    json_data = getresponse(urldata)
    # print the state id and state name corresponding
    for i in json_data["states"]:
        print(f'State Name:  {i["state"]["state_name"]} , State ID : {i["state"]["state_id"]}')


if __name__ == '__main__':
    main()
