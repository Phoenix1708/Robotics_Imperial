#!/bin/bash

#echo "MAC address of your Raspberry Pi:"
#read mac_address
#echo "Connecting to $mac_address"

# SSH to pi
#~dcw/tmp/git-clone-test/raspberry-pi-wifi/ssh-pi 44:33:4c:6c:b0:b6 -t -t  << 'ENDSSH'

# Create a directory for the node server
echo "Type a new password you will use when connecting to the robot server:"
read password
while [ -z "$password" ]
do
echo "You cannot leave the password blank! This is for security reasons. Please type a password you will use when connecting to the robot server:"
read password
done
mkdir server
cd server

# Download node.js
echo "Downloading Node.js"
wget http://nodejs.org/dist/v0.10.24/node-v0.10.24-linux-arm-pi.tar.gz
tar xvzf node-v0.10.24-linux-arm-pi.tar.gz
rm node-v0.10.24-linux-arm-pi.tar.gz
mv node-v0.10.24-linux-arm-pi/ node/

# Install socket.io
echo "Installing socket.io"
node/bin/npm install socket.io

# Install formidable
echo "Installing formidable"
node/bin/npm install formidable

# Clone the code
git clone https://bitbucket.org/lakySK/brickpiexplorer.git

# Create password file
cd brickpiexplorer
echo -n $password | md5sum | cut -d ' ' -f 1 >> password.txt

# Add the server to init.d
chmod 755 nodejs.sh
sudo cp nodejs.sh /etc/init.d
sudo update-rc.d nodejs.sh defaults
cd ../..
mkdir prac-files
echo "Copying example scripts."
cp server/brickpiexplorer/python/test.py prac-files/
cp server/brickpiexplorer/python/testDraw.py prac-files/
sudo /etc/init.d/nodejs.sh start
echo "The server was installed successfully and should be running now. You can access it via https://www.doc.ic.ac.uk/~jrj07/robotics/index.cgi. Next time you boot up your Pi, it should start automatically."

#ENDSSH
