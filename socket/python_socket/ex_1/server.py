from socket import *

# AF_INET -> 서로 다른 호스트에서 실행되는 프로세스 사이의 통신 지원
# SOCK_STREAM -> TCP

ServerSocket = socket(AF_INET, SOCK_STREAM)

ServerSocket.bind(('', 8080)) # 생성된 소켓에 주소를 부여
ServerSocket.listen(1) # 소켓에서 대기할 수 있는 클라이언트의 연결 요청 개수를 지정 (TCP)

clienSock, addr = ServerSocket.accept() # 클라이언트가 connect함수를 호출해 접속 요청시, 해당 접속 요청 수락

print(str(addr),'에서 접속이 확인 ! ')

data = clienSock.recv(1024)
print('받은 메시지 : ', data.decode('utf-8'))

clienSock.send('I am a server.'.encode('utf-8'))
print('메시지 전송 ! .')
