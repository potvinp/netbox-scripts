# NetBox custom scripts (Python 3.x)
This is an attempt to share some of my work with the [NetBox](https://github.com/digitalocean/netbox) community. I plan on adding more scripts later on.
# Dependencies
Make sure you have all dependencies installed i.e.  
```
$sudo pip3 install sys time re socket psycopg2
```
If you don't have pip installed then follow this [guide](https://pip.pypa.io/en/stable/installing/) 
# Installation
Clone the repository and modify **db_con.py** file with your DB information i.e.
```python
import psycopg2
conn = psycopg2.connect("dbname='YOUR_NETBOX_DB_NAME' user='YOUR_NETBOX_USERNAME' host='YOUR_NETBOX_DB_IP_ADDRESS' password='YOUR_NETBOX_DB_PASSWORD'")
cur = conn.cursor()
```

## ipam_mgmt.py 
The script attmepts to resolve each hostname in netbox DB then creates a **"mgmt"** interface with its corresponding IPv4/IPv6 addresses. 

## fping_prefixes.py 
Makes an API call to NetBox and returns the list of IPv4 prefixes, then saves the list of returned prefixes to **fping_prefixes file**. 

## fping.sh
Runs fping against each subnet found in **fping_prefixes** file and saves "Alive" hosts in **fping_hosts** file. 

## fping.py
Adds unique entries found **fping_hosts** file and ultimately adds them to NetBox. 
 
