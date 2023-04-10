#!/bin/sh

PASS = "1234" // 모든 유저의 패스워드를 1234로 변경 
while read line
do

        #useradd -d /home/$line $line
        useradd $line # user 생성 
        echo "$line:1234" | chpasswd
        tail -n2 /etc/passwd 
        mkdir /home/$line # user의 home 디렉토리 생성 
        chown $line:$line /home/$line # user의 홈 디렉토리 소유자를 user로 설정 
        chmod 700 /home/$line # 접근 권한 설정
        echo $line
done < user_list.txt # userID가 되는 목록이 있는 텍스트 파일 
