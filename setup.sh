#!/bin/bash

# Update package list
sudo apt-get update

# Install git, tree, vim, pigpio, and Python dependencies
sudo apt install -y build-essential git tree vim pigpio make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

sudo service pigpiod start # Start pigpio daemon
sudo systemctl enable pigpiod.service # Enable pigpio daemon on boot

# Add pyenv to PATH
echo 'export PATH="$HOME/.pyenv/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
source ~/.bashrc

# Install pyenv
curl https://pyenv.run | bash




# Install Python 3.7.3
pyenv install 3.7.3
# Set Python 3.7.3 as global Python version
pyenv global 3.7.3

echo 1 | curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.

# # Install Poetry
# curl -sSL https://install.python-poetry.org | python3 -

# # Add Poetry to PATH
# echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.bashrc
# source ~/.bashrc




