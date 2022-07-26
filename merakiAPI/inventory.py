import requests
import pprint as pp
import json
import csv
import time

def write_dicts_to_csv_fieldnames(list_of_dicts, file_path, field_names):
    with open(file_path, 'w', newline='', encoding='utf-8') as csv_file_object:
        writer = csv.DictWriter(csv_file_object, fieldnames=field_names)
        writer.writeheader()
        for row_dict in list_of_dicts:
            writer.writerow(row_dict)


def inventory():
    while(True):
        #Api call
        url = "https://api.meraki.com/api/v1/organizations/681155/devices/statuses?productTypes%5B%5D=appliance&productTypes%5B%5D=wireless"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
        }

        response = requests.request('GET', url, headers=headers)

        print("-----------------------------------------------------------------------")
        print("API CALL: ")
        print("-----------------------------------------------------------------------")
        pp.pprint(response.json())
        print("-----------------------------------------------------------------------")
        print("Raise for status: ", response.raise_for_status())
        print("-----------------------------------------------------------------------")    




        #keys to filter
        jsontx = response.json()
        list_keys = ['productType','model','name','mac','lanIp','publicIp','serial','status']
        filter_dict = [{key:val for key, val in ele.items() if key in list_keys} for ele in jsontx]
        print("-----------------------------------------------------------------------")
        print("Filtered Data: ")
        print("-----------------------------------------------------------------------")
        pp.pprint(filter_dict)


        path = 'inventory.csv'
        write_dicts_to_csv_fieldnames(filter_dict, path, list_keys)

        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        print("Última actualización:", current_time)
        time.sleep(300)


if __name__ == "__main__":
    inventory()