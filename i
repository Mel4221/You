#!/bin/bash


sh=/usr/local/bin/you
path=/usr/local/lib/you/
py=/usr/local/lib/you/main.py

sudo touch $sh
sudo echo "python3 "$py > $sh
sudo chmod a+x $sh
if [[ ! -d $path ]]
then 
sudo mkdir $path
fi

sudo cp *.py $path
sudo cp {i,u} $path
