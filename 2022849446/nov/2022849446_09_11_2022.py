import socket 
import time
import os
import urllib.request, urllib.parse, urllib.error

def task1():
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80)) # ('drbiswajitsarkar.com', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()    
    # cmd = 'GET http://drbiswajitsarkar.com HTTP/1.0\r\n\r\n'.encode()    
    mysock.send(cmd)
    
    while True:
        data = mysock.recv(512)
        if (len(data) < 1):
            break
        print(data.decode(),end='')
        
    mysock.close()
    
def task2():
    # picture task
    # HOST = 'data.pre4e.org'
    # PORT = 80
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80)) # ((HOST, PORT)) <-- throws error
    mysock.sendall(b'GET https://data.pr4e.org/cover3.jpg HTTP/1.0\r\n\r\n')
    count = 0
    picture = b""
    
    while True:
        data = mysock.recv(5120)
        if (len(data) < 1): break
        time.sleep(1.0)
        count = count + len(data)
        print(len(data), count)
        picture = picture + data
    
    mysock.close()
    
    # Look for the end of the header (2 CRLF)
    pos = picture.find(b"\r\n\r\n");
    print('Header length', pos)
    print(picture[:pos].decode())
    # Skip past the header and save the picture data
    picture = picture[pos+4:]
    
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fhand = open(dir_path + "\\stuff.jpg", "wb")
    fhand.write(picture)
    fhand.close()
    
def task3():
    # video task
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    
    counts = dict()
    for line in fhand:
        words = line.decode().split()
        for word in words:
            counts[word] = counts.get(word, 0) + 1
    print(counts)
    
def main():
    print("Student id is:", 2022849446)
    task1()
    task2()
    task3()

if __name__ == "__main__":
    main()
