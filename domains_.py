import sys
import socket
from datetime import datetime as dt
import time

def whois(ip):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("whois.arin.net", 43))
    s.send(('n ' + ip + '\r\n').encode())

    response = b""

    # setting time limit in secondsmd
    startTime = time.mktime(dt.now().timetuple())
    timeLimit = 3
    while True:
        elapsedTime = time.mktime(dt.now().timetuple()) - startTime
        data = s.recv(4096)
        response += data
        if (not data) or (elapsedTime >= timeLimit):
            break
    s.close()

    print(response.decode())

def main():
    domain = sys.argv[1];
    ip = socket.gethostbyname(domain);
    whois(ip)

main()