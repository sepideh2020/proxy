
import os,sys,thread,socket


BACKLOG = 1           # how many pending connections queue will hold
MAX_DATA_RECV = 999999  # max number of bytes we receive at once
DEBUG = True            # set to True to see the debug msgs
def main():
    global Flag
    Flag = False


   
    if (len(sys.argv)<2):
        print "No port given, using :8383 (http-alt)" 
        port = 8383
    else:
        port = int(sys.argv[1]) # port from argument

    
    host = ''               # blank for localhost

    print "Proxy Server Running on ",host,":",port

    try:
        # create a socket
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # associate the socket to host and port
        s.bind((host, port))

        # listenning
        s.listen(BACKLOG)

    except socket.error, (value, message):
        if s:
            s.close()
        print "Could not open socket:", message
        sys.exit(1)

    # get the connection from client
    while 1:
        conn, client_addr = s.accept()

        # create a thread to handle request
        thread.start_new_thread(proxy_thread, (conn, client_addr))

    s.close()
#************** END MAIN PROGRAM ***************

#********* PROXY_THREAD FUNC ***************
# A thread to handle request from browser
#*******************************************
def proxy_thread(conn, client_addr):
    global Flag
    Flag = False

    # get the request from browser
    request = conn.recv(MAX_DATA_RECV)

    # parse the first line
    first_line = request.split('\n')[0]

    # get url
    url = first_line.split(' ')[1]
    
    os.chdir("file_directory")
    cur_dir = os.getcwd()
    print(cur_dir)
    file_list = os.listdir(cur_dir)
    print(file_list)
    for file in file_list:
        print (file)
        with open(file, 'r') as f:
            for line in f.readlines():
                f.readline()
                print(line)
                print (url)
                if  url in line:
                    print (url)
                    print("congragulatioooon")
                    Flag=True
                    break
                else:
                    print("file does not exist")
    
    if Flag== False :
        conn.close()
        sys.exit(1)
    

    # find the webserver and port
    http_pos = url.find("://")          # find pos of ://
    if (http_pos==-1):
        temp = url
    else:
        temp = url[(http_pos+3):]       # get the rest of url

    port_pos = temp.find(":")           # find the port pos (if any)

    # find end of web server
    webserver_pos = temp.find("/")
    if webserver_pos == -1:
        webserver_pos = len(temp)

    webserver = ""
    port = -1
    if (port_pos==-1 or webserver_pos < port_pos):      # default port
        port = 80
        webserver = temp[:webserver_pos]
    else:       # specific port
        port = int((temp[(port_pos+1):])[:webserver_pos-port_pos-1])
        webserver = temp[:port_pos]

    try:
        # create a socket to connect to the web server
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((webserver, port))
        s.send(request)         # send request to webserver

        while 1:
            # receive data from web server
            data = s.recv(MAX_DATA_RECV)

            if (len(data) > 0):
                # send to browser
                conn.send(data)
            else:
                break
        s.close()
        conn.close()
    except socket.error, (value, message):
        if s:
            s.close()
        if conn:
            conn.close()
        sys.exit(1)

if __name__ == '__main__':
    main()
