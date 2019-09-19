import requests
import json
import argparse
import random
from random import randint
import time

sheetId = None
token = None
url = None
headers = {}
cList = []
rList = []


def setHeaderCreateSheet():

    token = "3c8f4c59e19041a5b14a9890514ed527"


def createSheet(url, rowNumber):
    global sheetId
    global cList
    global rList
    global headers

    url = url

    sheetname = "Test Sheet"
    payload = {
        'name': sheetname,
        "columns": [{'title': 'Primary Column', 'primary': 'true', 'type': 'TEXT_NUMBER'}]
    }

    r = requests.post(url + '/sheets', data=json.dumps(payload), headers=headers)

    data = json.loads(r.text)

    if (r.status_code == 200):
        sheetId = data['result']['id']
        primaryCol = data['result']['columns'][0]['id']
        cList.append(primaryCol)

        # inserting a row depending on number
        for j in range(rowNumber):
            rowPayload = {
                'toBottom': 'true', 'cells': [{'columnId': str(cList[0]), 'value': 'Test Data ' + str(rowNumber)}]
            }

            r = requests.post(url + '/sheets/' + str(sheetId) + '/rows?exclude=nonexistentCells',
                              data=json.dumps(rowPayload)
                              , headers=headers)
            rowData = json.loads(r.text)

            if (r.status_code == 200):
                rowId = rowData['result']['id']

                for k in range(len(cList)):
                    updatePayload = {
                        'cells': [
                            {'columnId': str(cList[k]),
                             'value': "test",
                             'strict': False
                             }]
                    }

                    r = requests.put(url + '/sheets/' + str(sheetId) + '/rows/' + str(rowId),
                                     data=json.dumps(updatePayload),
                                     headers=headers)

                    updateData = json.loads(r.text)

                    if (r.status_code == 200):
                        print("Sucess Row: " + str(rowId))

                        data = open('./TEST_copy_2.png', 'rb').read()

                        r = requests.post(url + '/sheets/' + str(sheetId) + '/rows/' + str(rowId) + 'proofs', data=data,
                                          headers=setHeaderCreateProof())

                        updateData = json.loads(r.text)

                    if (r.status_code == 200):
                        print("Sucess Proof: " + str(rowId))
                    else:
                        print(updateData)
                        break
            else:
                print(rowData)
                break


    else:
        print(data)

def createProof(url, rowNumber):
    global sheetId
    global rList
    global headers

    url = url

    data = open('./TEST copy 2.png', 'rb').read()

    r = requests.post(url + '/sheets/({{SHEETID}}/rows/', data=data, headers=headers)
    #sheets/{{sheetId}}/rows/4503604730062724/proofs

    data = json.loads(r.text)

    if (r.status_code == 200):
        sheetId = data['result']['id']
        primaryCol = data['result']['columns'][0]['id']
        cList.append(primaryCol)

        # inserting a row depending on number
        for j in range(rowNumber):
            rowPayload = {
                'toBottom': 'true', 'cells': [{'columnId': str(cList[0]), 'value': 'Test Data ' + str(rowNumber)}]
            }

            r = requests.post(url + '/sheets/' + str(sheetId) + '/rows?exclude=nonexistentCells',
                              data=json.dumps(rowPayload)
                              , headers=headers)
            rowData = json.loads(r.text)

            if (r.status_code == 200):
                rowId = rowData['result']['id']

                for k in range(len(cList)):
                    updatePayload = {
                        'cells': [
                            {'columnId': str(cList[k]),
                             'value': "test",
                             'strict': False
                             }]
                    }

                    r = requests.put(url + '/sheets/' + str(sheetId) + '/rows/' + str(rowId),
                                     data=json.dumps(updatePayload),
                                     headers=headers)

                    updateData = json.loads(r.text)

                    if (r.status_code == 200):
                        print("Sucess Row: " + str(rowId))

                    else:
                        print(updateData)
                        break
            else:
                print(rowData)
                break


    else:
        print(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('url', help='Your url')
    # parser.add_argument('token', help='Your API token')
    # parser.add_argument('rowNumber', help='Number of row')
    # parser.add_argument('columnNumber', help='Number of columns')
    # parser.add_argument('sheetNumber', help="Number of sheets")

    # args = parser.parse_args()
    url = args.url
    # token = args.token
    # rowNumber = args.rowNumber
    # columnNumber = args.columnNumber
    # sheetNumber = args.sheetNumber

    getComps(url)
    # for i in range(50):
    #   createProof()

main()


# Endpoints - /areas, /competitions,