import sys
import json
import requests,time

ip_addr, jobid,bagseal_number = sys.argv[1], 1 ,507033756
url_scan = "http://{0}/api/v2/controller/c1/shipment/scan/".format(ip_addr)

url_dimension = "http://{0}/api/v2/controller/c1/shipment/dimension/".format(ip_addr)

url_sort = "http://{0}/api/v2/controller/c1/shipment/sort/".format(ip_addr)

url_ss_shipment_scan = "http://{0}/api/v1/controller/s1/pms/gpms/event/".format(ip_addr)

url_ss_pptl_button_press = "http://{0}/api/v1/controller/s1/pms/gpms/event/".format(ip_addr)

url_ss_pptl_scan = "http://{0}/api/v1/controller/s1/pms/gpms/event/".format(ip_addr)

url_ss_bagseal_scan = "http://{0}/api/v1/controller/s1/pms/gpms/event/".format(ip_addr)

url_ss_pptl_scan_again = "http://{0}/api/v1/controller/s1/pms/gpms/event/".format(ip_addr)

url_ss_cancel_scan = "http://{0}/api/v1/controller/s1/pms/gpms/event/".format(ip_addr)


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


headers_ss_shipment_scan = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "3646e440-9ac1-40e6-a88b-e6f48166160b"
    }




headers_ss_pptl_button_press = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "ece71225-f88b-49a5-8d2c-90ec0d573fc9"
    }


headers_ss_pptl_scan = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "3fd12b9a-7e4a-4b9d-8ba8-394bccd1a8a0"
    }

headers_ss_bagseal_scan = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "83fd8e26-a612-41a6-b81c-faca98042a36"
    }

headers_ss_pptl_scan_again = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "ac04a639-76b5-4540-a4a0-43c034e1993c"
    }

headers_ss_cancel_scan = {
    'Content-Type': "application/json",
    'cache-control': "no-cache",
    'Postman-Token': "41155449-30b4-4d45-8416-6f4ca4c43fb5"
    }

with open("awb.txt") as f:
    data = f.readlines()
f.close()

for barcode in data:

    print("\n" + barcode + "\n")


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

    controller_id = int(arm_id) + 512

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
    time.sleep(0.3)
    payload_ss_shipment_scan = {
        "event_name": "scan",
        "controller_id": "{0}".format(controller_id),
        "peripheral_id": "1",
        "event_data": {
            "last_seen_at": "",
            "barcode": "{0}".format(barcode.strip()),
        }
    }

    payload_ss_shipment_scan = json.dumps(payload_ss_shipment_scan)
    response_ss_shipment_scan = requests.request("POST", url_ss_shipment_scan, data=payload_ss_shipment_scan,headers=headers_ss_shipment_scan)
    resp_str_ss_shipment_scan = response_ss_shipment_scan.text
    print(resp_str_ss_shipment_scan)
    resp_ss_shipment_scan = json.loads(resp_str_ss_shipment_scan)

    payload_ss_pptl_button_press = {
        "event_name": "pptl_button_press",
        "controller_id": "{0}".format(controller_id),
        "peripheral_id": "{0}".format(pptl_id),
        "event_data": {
            "last_seen_at": ""
        }
    }

    payload_ss_pptl_button_press = json.dumps(payload_ss_pptl_button_press)
    response_ss_pptl_button_press = requests.request("POST", url_ss_pptl_button_press,
                                                     data=payload_ss_pptl_button_press,
                                                     headers=headers_ss_pptl_button_press)
    resp_str_ss_pptl_button_press = response_ss_pptl_button_press.text
    print(resp_str_ss_pptl_button_press)
    resp_ss_pptl_button_press = json.loads(resp_str_ss_pptl_button_press)


    payload_ss_pptl_scan ={
        "event_name": "scan",
        "controller_id": "{0}".format(controller_id),
        "peripheral_id": 1,
        "event_data": {
            "last_seen_at": "",
            "barcode": "#GP{0}".format(pptl_id)
        }
    }

    payload_ss_pptl_scan = json.dumps(payload_ss_pptl_scan)
    response_ss_pptl_scan = requests.request("POST", url_ss_pptl_scan, data=payload_ss_pptl_scan,
                                             headers=headers_ss_pptl_scan)
    resp_str_ss_pptl_scan = response_ss_pptl_scan.text
    print(resp_str_ss_pptl_scan)
    resp_ss_pptl_scan = json.loads(resp_str_ss_pptl_scan)

    payload_ss_bagseal_scan = {
        "event_name": "scan",
        "controller_id": "{0}".format(controller_id),
        "peripheral_id": 1,
        "event_data": {
            "last_seen_at": "",
            "barcode": "{0}".format(bagseal_number)
        }
    }

    payload_ss_bagseal_scan = json.dumps(payload_ss_bagseal_scan)
    response_ss_bagseal_scan = requests.request("POST", url_ss_bagseal_scan, data=payload_ss_bagseal_scan,
                                                headers=headers_ss_bagseal_scan)
    resp_str_ss_bagseal_scan = response_ss_bagseal_scan.text
    print(resp_str_ss_bagseal_scan)
    resp_ss_bagseal_scan = json.loads(resp_str_ss_bagseal_scan)

    bagseal_number = bagseal_number + 1

    payload_ss_pptl_scan_again = {
        "event_name": "scan",
        "controller_id": "{0}".format(controller_id),
        "peripheral_id": 1,
        "event_data": {
            "last_seen_at": "",
            "barcode": "#GP{0}".format(pptl_id)
        }
    }

    payload_ss_pptl_scan_again = json.dumps(payload_ss_pptl_scan_again)
    response_ss_pptl_scan_again = requests.request("POST", url_ss_pptl_scan_again, data=payload_ss_pptl_scan_again,
                                                   headers=headers_ss_pptl_scan_again)
    resp_str_ss_pptl_scan_again = response_ss_pptl_scan_again.text
    print(resp_str_ss_pptl_scan_again)
    resp_ss_pptl_scan_again = json.loads(resp_str_ss_pptl_scan_again)



    payload_ss_cancel_scan = {
        "event_name": "scan",
        "controller_id": "{0}".format(controller_id),
        "peripheral_id": 1,
        "event_data": {
            "last_seen_at": "",
            "barcode": "#CANCEL"
        }

    }

    payload_ss_cancel_scan = json.dumps(payload_ss_cancel_scan)
    response_ss_cancel_scan = requests.request("POST", url_ss_cancel_scan, data=payload_ss_cancel_scan,
                                               headers=headers_ss_cancel_scan)
    resp_str_ss_cancel_scan = response_ss_cancel_scan.text
    print(resp_str_ss_cancel_scan)
    resp_ss_cancel_scan = json.loads(resp_str_ss_cancel_scan)

    jobid = jobid + 1
