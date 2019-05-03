import sys
import json
import requests
import time
ip_addr, jobid = sys.argv[1], 1
url_scan = "http://{0}/api/v2/controller/c1/shipment/scan/".format(ip_addr)
url_dimension = "http://{0}/api/v2/controller/c1/shipment/dimension/".format(ip_addr)
url_sort = "http://{0}/api/v2/controller/c1/shipment/sort/".format(ip_addr)
headers_scan = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "edebcab7-d6a6-433e-b5ec-1d1fa1826e54"
}
headers_dimensions = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "52e043cb-1b1c-4c11-b8b3-366b7f198a70"
}
headers_sort = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "5957666f-5064-4ccf-897b-71d63dcd0430"
    }
with open("awb.txt") as f:
    data = f.readlines()
f.close()

for barcode in data:
    print(barcode)
    payload_scan = {
        "status_code": "0000",
        "barcode": "{0}".format(barcode.strip()),
        "job_id": "{0}".format(jobid)
    }
    payload_scan = json.dumps(payload_scan)
    response_scan = requests.request("POST", url_scan, data=payload_scan, headers=headers_scan)
    resp_str_scan = response_scan.text
    print(resp_str_scan)
    resp_scan = json.loads(resp_str_scan)
    arm_id, hubcode, pptl_id = resp_scan.get('arm_id'), resp_scan.get('hubcode'), resp_scan.get('pptl_id')
    print(arm_id, hubcode, pptl_id)
    time.sleep(3)
    #payload_scan = json.dumps(payload_scan)
    payload_dimension = {
        "job_id": "{0}".format(jobid),
        "weight": 800,
        "length": 10, "breadth": 10, "height": 100,
        "real_volume": 1000090, "box_volume": 10000,
        "status_code": "0000"
    }
    payload_dimension = json.dumps(payload_dimension)
    response_dimension = requests.request("POST", url_dimension, data=payload_dimension, headers=headers_dimensions)
    resp_str_dimension = response_dimension.text
    print(resp_str_dimension)
    resp_str_dimension = json.loads(resp_str_dimension)
    time.sleep(3)
    payload_sort = {
        "job_id": "{0}".format(jobid),
        "status_code": "1",
        "arm_id": "{0}".format(arm_id)
    }
    payload_sort = json.dumps(payload_sort)
    response_sort = requests.request("POST", url_sort, data=payload_sort, headers=headers_sort)
    resp_str_sort = response_sort.text
    print(resp_str_sort)
    resp_str_sort = json.loads(resp_str_sort)
    time.sleep(3)
    jobid = jobid + 1
