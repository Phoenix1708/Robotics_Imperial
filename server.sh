#!bin/bash

echo "[start/stop]:"
read command
sudo /etc/init.d/nodejs.sh $command
