# ping
./profile -f "--net=host" -i debian:jessie -c "ping google.com -c 2 " -n ping

# assuming gcc, g++ and make are available in the container
./profile -r -i repo:image -c "ls" -n ls-with-mica-recompiled

# execute a command first
./profile -p "run daemon" -i repo:image -c "anexe" -n run-daemon-first
