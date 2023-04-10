#/bin/bash

while read line
do
        userdel -r $line #userlist로 읽어온 user들을 모두 삭제
        echo $line
done < userlist.txt 
