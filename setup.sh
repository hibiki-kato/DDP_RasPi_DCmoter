#!/bin/bash

# Update package list
sudo apt-get update

# Install git, tree, vim, pigpio, and Python dependencies
sudo apt-get install -y build-essential git tree vim make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

sudo service pigpiod start # Start pigpio daemon
sudo systemctl enable pigpiod.service # Enable pigpio daemon on boot

if [ ! -r ~/.pyenv/ ]
then
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
    echo '
# pyenv
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
if command -v pyenv 1>/dev/null 2>&1; then
    eval "$(pyenv init -)"
    eval "$(pyenv virtualenv-init -)" # Enable auto-activation of virtualenvs
fi' >> ~/.bashrc
    source ~/.bashrc
    exec "$SHELL"
fi



# Install Python 3.10
pyenv install 3.10
# Set Python 3.10 as global Python version
pyenv global 3.10

echo 1 | curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.

# Install Poetry
curl -sSL https://install.python-poetry.org | python3 -

# Add Poetry to PATH
echo 'export PATH="$HOME/.poetry/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc

# set up python virtual environment in poetry
poetry config virtualenvs.in-project true
poetry config virtualenvs.create true

cd ikkyo-sai_2023




