import json
import requests
from tabulate import tabulate
import ipaddress
from colorama import Fore, Style, init

init(autoreset=True) #autoreset is used to reset the color of the text after each print

def is_public_ip(ip):
    try:
        return not ipaddress.ip_address(ip).is_private #returns true if the ip address is public, false if it is private
    except ValueError:
        return False

# This function takes an IP address and returns its location info (city, region, country)
def get_geo_info(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json", timeout=3) # Send a request to ipinfo.io to get info about the IP address
        if response.status_code == 200:
            data = response.json() # If the request worked, get the data in JSON format

            # Get the city, region, and country from the data (or 'N/A' if missing)
            city = data.get("city", "N/A")
            region = data.get("region", "N/A")
            country = data.get("country", "N/A")
            # Return the location as a string
            return f"{city}, {region},{country}"
        else:
            return "Lookup failed"
    except Exception as e:
        return "Error"

def summarize_ip_counts(json_file):
    with open(json_file, "r") as f:
        events = json.load(f)
    ip_counts = {}

    #for each event, get the ip address and add it to the ip_counts dictionary
    for event in events:
        ip = event.get("ip")
        if ip:
            ip_counts[ip] = ip_counts.get(ip, 0) + 1 #assigns a count to the ip address
    
    table = []
    #for each ip address, get the count and the geo info
    for ip, count in ip_counts.items():

        #if the ip address is public, get the geo info, otherwise it is a private ip address
        if is_public_ip(ip):
            geo = get_geo_info(ip)
        else:
            geo = "Private IP"

        #if the count is greater than 10, color the ip address red
        if count > 10:
            ip_colored = f"{Fore.RED}{ip}{Style.RESET_ALL}"
        else:
            ip_colored = f"{Fore.GREEN}{ip}{Style.RESET_ALL}"
        
        table.append((ip_colored,count,geo))
    
    #print the table
    headers = ["IP Address", "Count", "Location"]
    print(tabulate(table, headers, tablefmt="grid"))
    