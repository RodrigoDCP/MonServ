#!/bin/bash

# Actualizar lista de paquetes
sudo apt update

# Instalar Python
sudo apt install -y python3

# Instalar pip
sudo apt install -y python3-pip

# Instalar librerías de Python
sudo pip3 install itertools
sudo pip3 install random
sudo pip3 install datetime
sudo pip3 install termcolor
sudo pip3 install colorama

# Instalar herramientas adicionales
sudo apt install -y john
sudo apt install -y nmap

# Instalar firewalld
sudo apt install -y firewalld
