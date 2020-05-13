import unittest
from solution import *

class TestSolution(unittest.TestCase):

	def test_check_command_line_input_ip_entered(self):
		sys.argv = ['solution.py']
		response = check_command_line_input()
		self.assertEqual(response, False)

	def test_check_command_line_input_bad_ip(self):
		sys.argv = ['solution.py', '277.0.0.1']
		response = check_command_line_input()
		self.assertEqual(response, False)

	def test_check_command_line_input_ip_properly_entered(self):
		sys.argv = ['solution.py', '98.234.186.45']
		response = check_command_line_input()
		self.assertEqual(response, True)

	def test_check_ipinfo_response_no_country(self):
		ipinfo_response = {u'loc': u'37.4135,-122.1312', 
							u'city': u'Palo Alto', 
							u'region': u'California', 
							u'hostname': u'c-98-234-186-45.hsd1.ca.comcast.net', 
							u'ip': u'98.234.186.45', 
							u'org': u'AS7922 Comcast Cable Communications, LLC', 
							u'postal': u'94306'}
		response = check_ipinfo_response(ipinfo_response)
		self.assertEqual(response, False)

	def test_check_ipinfo_response_no_region(self):
		ipinfo_response = {u'loc': u'37.4135,-122.1312', 
							u'city': u'Palo Alto', 
							u'country': u'US', 
							u'hostname': u'c-98-234-186-45.hsd1.ca.comcast.net', 
							u'ip': u'98.234.186.45', 
							u'org': u'AS7922 Comcast Cable Communications, LLC', 
							u'postal': u'94306'}
		response = check_ipinfo_response(ipinfo_response)
		self.assertEqual(response, False)

	def test_check_ipinfo_response_no_city(self):
		ipinfo_response = {u'loc': u'37.4135,-122.1312', 
							u'country': u'US',
							u'region': u'California', 
							u'hostname': u'c-98-234-186-45.hsd1.ca.comcast.net', 
							u'ip': u'98.234.186.45', 
							u'org': u'AS7922 Comcast Cable Communications, LLC', 
							u'postal': u'94306'}
		response = check_ipinfo_response(ipinfo_response)
		self.assertEqual(response, False)

	def test_check_ipinfo_response_no_org(self):
		ipinfo_response = {u'loc': u'37.4135,-122.1312', 
							u'city': u'Palo Alto', 
							u'country': u'US',
							u'region': u'California', 
							u'hostname': u'c-98-234-186-45.hsd1.ca.comcast.net', 
							u'ip': u'98.234.186.45', 
							u'postal': u'94306'}
		response = check_ipinfo_response(ipinfo_response)
		self.assertEqual(response, False)

	def test_check_ipinfo_response_no_loc(self):
		ipinfo_response = {u'city': u'Palo Alto', 
							u'country': u'US',
							u'region': u'California', 
							u'hostname': u'c-98-234-186-45.hsd1.ca.comcast.net', 
							u'ip': u'98.234.186.45', 
							u'org': u'AS7922 Comcast Cable Communications, LLC', 
							u'postal': u'94306'}
		response = check_ipinfo_response(ipinfo_response)
		self.assertEqual(response, False)

	def test_check_ipinfo_response_loc_improperly_formed(self):
		ipinfo_response = {u'loc': u'37.4135', 
							u'city': u'Palo Alto', 
							u'country': u'US',
							u'region': u'California', 
							u'hostname': u'c-98-234-186-45.hsd1.ca.comcast.net', 
							u'ip': u'98.234.186.45', 
							u'org': u'AS7922 Comcast Cable Communications, LLC', 
							u'postal': u'94306'}
		response = check_ipinfo_response(ipinfo_response)
		self.assertEqual(response, False)

	def test_check_ipinfo_response_properly_formed(self):
		ipinfo_response = {u'loc': u'37.4135,-122.1312', 
							u'country': u'US',
							u'city': u'Palo Alto', 
							u'region': u'California', 
							u'hostname': u'c-98-234-186-45.hsd1.ca.comcast.net', 
							u'ip': u'98.234.186.45', 
							u'org': u'AS7922 Comcast Cable Communications, LLC', 
							u'postal': u'94306'}
		response = check_ipinfo_response(ipinfo_response)
		self.assertEqual(response, True)

if __name__ == '__main__':
	unittest.main()