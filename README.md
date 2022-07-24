# MERAKI API PROJECT

## Description

In the network field is important to have access to relevant and updated information of the Meraki networks.
"Meraki API Project" is a project built to extract valuable information using the "Meraki Dashboard API"
A RESTful API to programmatically manage and monitor Meraki networks at scale. With the scripts that are
contained in this project you can consult the organizations that can be accesed using the public API key.
Also you can make and inventary of different types of devices from the organization called "Delab". 
Specially, for the products types "wireless" & "appliance".

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)

## Installation

Step-by-step description of how to get the development environment running:
1. Clone this repository on your local workspace.
2. Once you have cloned this repository, you have to install the necesary dependencies.
To do this, run the following command using your terminal:
            "pip install -r requirements.txt"
3. Use one of the following scripts:
    - organizations.py
    - inventory.py
    - wireless.py
    - appliance.py

## Usage

1. organizations.py: This script allows you to list the organizations that the user has privileges on (In this case we are using the public API key)
2. inventory.py: This scripts allows you to generate an inventory of the DeLab's Organization devices (In case you want to consult another organization is necessary to modify the organization id in the API call url.)
3. appliance.py: This scripts allows you to generate an inventory of the DeLab's Organization devices where productTypes = appliance (In case you want to consult another organization is necessary to modify the organization id in the API call url.)
4. wireless.py: This scripts allows you to generate an inventory of the DeLab's Organization devices where productTypes = wireless (In case you want to consult another organization is necessary to modify the organization id in the API call url.)


E.g. (Inventory.py)

<p align="center">
  <img alt="inventorycsv" src="https://github.com/wgabriel14/Meraki_API_Project/blob/main/assets/images/inventorycsv.PNG">
</p>

<p align="center">
  <img alt="inventorycsv in excel" src="https://github.com/wgabriel14/Meraki_API_Project/blob/main/assets/images/inventorycsvexcel.PNG">
</p>


## Meraki API Documentation

https://developer.cisco.com/meraki/api-v1/

## License




