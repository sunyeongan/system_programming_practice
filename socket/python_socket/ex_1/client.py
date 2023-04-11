from socket import *

# AF_INET -> 서로 다른 호스트에서 실행되는 프로세스 사이의 통신 지원
# SOCK_STREAM -> TCP
ClientSocket = socket(AF_INET, SOCK_STREAM) # 파일 기술자 리턴
ClientSocket.connect(('127.0.0.1', 8080)) # 자기 자신을 8080번 포트로 연결

print("연결 확인 ! ")

#메세지 전송하기
ClientSocket.send('I am a clinet'.encode('utf-8'))
print('메시지 전송 완료 ! ')

data = ClientSocket.recv(1024)

print('받은 메시지 : ', data.decode('utf-8'))
