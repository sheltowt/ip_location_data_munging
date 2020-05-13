import sys
import requests
from tabulate import tabulate
import json
from IPy import IP
from markdown import markdown
from BeautifulSoup import BeautifulSoup

ipinfo_base_url = "https://ipinfo.io/"

## checks for properly formed IP input entered via command line
def check_command_line_input():
	if len(sys.argv) != 2:
		print "You must input one IP address when running this script, see the README for more information"
		return False
	else:
		try:
			IP(sys.argv[1])
		except:
			print "A properly formed IP address was not entered as a command line argument, see the README for more information"
			return False

	return True

## checks the response from ipinfo
def check_ipinfo_response(ipinfo_response):
	if "country" in ipinfo_response.keys() and \
		"region" in ipinfo_response.keys()and \
		"city" in ipinfo_response.keys()and \
		"loc" in ipinfo_response.keys()and \
		len(ipinfo_response["loc"].split(',')) == 2 and \
		"org" in ipinfo_response.keys():
		return True
	else:
		print "The IP info service did not return a properly formed object, see the README for more information"
		return False

## fetches the data from ipinfo
def fetch_data(IP):
	url = ipinfo_base_url + IP 
	IPData_raw = requests.get(url)
	IPData = json.loads(IPData_raw.text)
	return IPData

## returns the markdown table and headers
def return_markdown(IPData):
	return_object = "<p> </em></p>"
	return_object = "<p> Location</em></p>"
	return_object += "<p> </em></p>"

	location_data = [["Country", "Region", "City"], [IPData["country"], IPData["region"], IPData["city"]]]

	return_object += "<p>" + tabulate(location_data, headers="firstrow", tablefmt="fancy_grid") + "</em></p>"
	return_object += "<p> Coordinates </em></p>"
	return_object += "<p> </em></p>"

	latitude = (IPData["loc"].split(','))[0]
	longitude = (IPData["loc"].split(','))[1]
	coordinate_data = [["Latitude", "Longitude"], [latitude, longitude]]

	return_object += "<p>" + tabulate(coordinate_data, headers="firstrow", tablefmt="fancy_grid")+ "</em></p>"
	return_object += "<p> Organizations </em></p>"
	return_object += "<p> </em></p>"
	return_object += IPData["org"]
	return_object += "<p> </em></p>"
	return markdown(return_object)

## main function that orchestrates the execution of the script
def queryIPInfo(ip_input):
	retrieved_IPData = fetch_data(ip_input)
	if check_ipinfo_response(retrieved_IPData):
		processed_markdown = return_markdown(retrieved_IPData)
		## prints properly formatted output to the command line
		print(''.join(BeautifulSoup(processed_markdown).findAll(text=True)))
		return processed_markdown

if __name__ == '__main__':
	if check_command_line_input():
		queryIPInfo(sys.argv[1])