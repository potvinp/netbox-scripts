import sys, time
import requests, json


#NetBox API Token
headers = {'Authorization': 'Token: YOUR TOKEN'}


def ip_prefix():
#Prefix list API. Initial API call to retreive first batch.
    prefix_list = []
    api_init = "https://HOSTNAME/api/ipam/prefixes/?status=active" #Replace HOSTNAME with NetBox URL/IP
    api_prefixes = requests.get(api_init, headers=headers, verify=False)
    z_prefixes = json.loads(api_prefixes.text)
    for prefixes in z_prefixes['results']:
        prefix_list.append(prefixes['prefix'])

#Prefix list API. Sebsequent API request(s) due to API pagination. The default MAX is value "?limit=1000"
    if(type(z_prefixes) is None):
        http_req_prefixes = requests.get(z_prefixes['next'], headers=headers, verify=False)
        z_prefixes = json.loads(http_req_prefixes.text)
        for prefixes in z_prefixes['results']:
            #print prefixes['prefix']
            prefix_list.append(prefixes['prefix'])
    else:
        return prefix_list


def ip_address():
#Initial API call to retreive first batch.
    ip_set = set()
    api_link = "https://HOSTNAME/api/ipam/ip-addresses/?limit=1000" #Replace HOSTNAME with NetBox URL/IP
    api_init = requests.get(api_link, headers=headers, verify=False)
    z_ip = json.loads(api_init.text)
    for ips in z_ip['results']:
        #print ips[u'address']
        ip_set.add(ips['address'])
    for subsequent in z_ip['next']:
        if z_ip['next']:
            http_req_prefixes = requests.get(z_ip['next'], headers=headers, verify=False)
            z_ip = json.loads(http_req_prefixes.text)
            for subsequent in z_ip['results']:
                #print subsequent[u'address']
                ip_set.add(subsequent['address'])
    return ip_set