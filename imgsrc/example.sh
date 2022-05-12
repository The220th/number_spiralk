#/bin/bash

python3 number_spiralk.py -w 1920 -h 1080 -max 100000 -scale 0.1 -o primes_scale_0.1.png &

python number_spiralk.py -w 1920 -h 1080 -max 100000 -scale 1 -o primes_scale_1.png &

python number_spiralk.py -w 1920 -h 1080 -max 100000 -scale 5 -o primes_scale_5.png &

python number_spiralk.py -w 1920 -h 1080 -max 100000 -scale 10 -o primes_scale_10.png &

python number_spiralk.py -w 1920 -h 1080 -max 100000 -scale 25 -o primes_scale_25.png &

python number_spiralk.py -w 1920 -h 1080 -max 100000 -scale 50 -o primes_scale_50.png &

python number_spiralk.py -w 1920 -h 1080 -max 100000 -scale 75 -o primes_scale_75.png &

python number_spiralk.py -w 1920 -h 1080 -max 1000000 -scale 100 -o primes_scale_100.png &

python number_spiralk.py -w 1920 -h 1080 -max 1000000 -scale 250 -o primes_scale_250.png &

python3 number_spiralk.py -max 100000000 -scale 500 -o primes_scale_500.png & # i5-7100 где-то часа 4

python3 number_spiralk.py -max 100000000 -scale 1000 -o primes_scale_1000.png & # i5-7100 где-то часа 4

python3 number_spiralk.py -max 100000000 -scale 2000 -o primes_scale_2000.png & # i5-7100 где-то часа 4

python3 number_spiralk.py -max 100000000 -scale 5000 -o primes_scale_5000.png & # i5-7100 где-то часа 4

python3 number_spiralk.py -max 1000000000 -scale 10000 -o primes_scale_10000.png & # i5-7100 где-то часов 40

python3 number_spiralk.py -max 1000000000 -scale 100000 -o primes_scale_100000.png & # i5-7100 где-то часов 40

python3 number_spiralk.py -max 1000000000 -scale 1000000 -o primes_scale_1000000.png & # i5-7100 где-то часов 40

python3 number_spiralk.py -max 1000000000 -scale 10000000 -o primes_scale_10000000.png & # i5-7100 где-то часов 40

python3 number_spiralk.py -max 1000000000 -scale 100000000 -o primes_scale_100000000.png & # i5-7100 где-то часов 40

python3 number_spiralk.py -max 1000000000 -scale 1000000000 -o primes_scale_1000000000.png # i5-7100 где-то часов 40



ffmpeg -i primes_scale_500.png -vf scale=1500:1000 o.primes_scale_500.png

ffmpeg -i primes_scale_1000.png -vf scale=1500:1000 o.primes_scale_1000.png

ffmpeg -i primes_scale_2000.png -vf scale=1500:1000 o.primes_scale_2000.png

ffmpeg -i primes_scale_5000.png -vf scale=1500:1000 o.primes_scale_5000.png

ffmpeg -i primes_scale_10000.png -vf scale=1500:1000 o.primes_scale_10000.png

ffmpeg -i primes_scale_100000.png -vf scale=1500:1000 o.primes_scale_100000.png

ffmpeg -i primes_scale_1000000.png -vf scale=1500:1000 o.primes_scale_1000000.png

ffmpeg -i primes_scale_10000000.png -vf scale=1500:1000 o.primes_scale_10000000.png

ffmpeg -i primes_scale_100000000.png -vf scale=1500:1000 o.primes_scale_100000000.png

ffmpeg -i primes_scale_1000000000.png -vf scale=1500:1000 o.primes_scale_1000000000.png
