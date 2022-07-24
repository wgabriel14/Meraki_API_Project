import requests
import pprint as pp
import json
import csv


def list_appliance_devices():


    url = "https://api.meraki.com/api/v1/organizations/681155/devices/statuses?productTypes%5B%5D=appliance"

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


    jsontx = response.json()


    #keys to filter
    list_keys = ['productType','model','name','mac','lanIp','publicIp','serial','statuses']
    
    filter_dict = [{key:val for key, val in ele.items() if key in list_keys} for ele in jsontx]
    print("-----------------------------------------------------------------------")
    print("Filtered Data: ")
    print("-----------------------------------------------------------------------")    
    pp.pprint(filter_dict)

    # filter_dict to csv
    def write_dicts_to_csv(list_of_dicts, file_path):
        field_names = list_of_dicts[0].keys()
        with open(file_path, 'w', newline='', encoding='utf-8') as csv_file_object: 
            writer = csv.DictWriter(csv_file_object, fieldnames=field_names)
            writer.writeheader()
            for row_dict in list_of_dicts:
                writer.writerow(row_dict)

    path = 'appliance.csv'
    write_dicts_to_csv(filter_dict, path)

if __name__ == "__main__":
    list_appliance_devices()