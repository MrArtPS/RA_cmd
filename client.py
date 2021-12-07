import socket



client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(( 'server ip',1296))#Connect to server`

while True:
    print('------------------------')
    print('Successfully connected')
    print('------------------------')
    while True:    
        mes=input('$ // ')

        client.send(mes.encode('utf-8'))


  
        



    

    
