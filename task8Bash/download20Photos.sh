for ((i = 0; i < 10; i++))
do
	curl -L -o "./attachments/photo${i}.png" https://picsum.photos/800/400
done