#!/usr/bin/python3

import socket, sys
from time import sleep

if len(sys.argv) <= 2:
	print(f"[-] Example: python3 fuzzer.py <ip> <command>")
	sys.exit(0)

ip = sys.argv[1]
prefix = f"{sys.argv[2]} "
if not ip or not prefix:
	print(f"[-] Example: python3 fuzzer.py <ip> <command>")
	sys.exit(0)
port = 1337
timeout = 5
string = prefix + "A" * 100

while True:
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		my_bytes = len(string) - len(prefix)
		s.settimeout(timeout)
		s.connect((ip, port))
		s.recv(1024)
		try:
			print(f"[+] Executing: {my_bytes}", end="\r")
			s.send(bytes(string, "latin-1"))
			s.recv(1024)
		except Exception as e:
			print(f"[+] Fuzzing crashed at {my_bytes} bytes")
			sys.exit(0)
		else:
			string += 100 * "A"
			sleep(1)

# while True:
# 	my_bytes = len(string) - len(prefix)
# 	try:
#
# 			s.settimeout(timeout)
# 			s.connect((ip, port))
# 			s.recv(1024)
# 			print(f"[+] Fuzing crashed at {my_bytes} bytes")
# 			s.send(bytes(string, "latin-1"))
# 			s.recv(1024)
# 	except Exception as e:
# 		print(f"[+] {e}")
# 		print(f"[+] Fuzing crashed at {my_bytes} bytes")
# 		sys.exit(0)
# 	string += 100 * "A"
# 	time.sleep(1)
