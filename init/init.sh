#!/usr/bin/env bash

# General install
if [[ ! -f /home/done.sh ]]; then

  echo "-- Get Update --"
  apt-get update
  echo "-- Install Python --"
  apt-get install python-setuptools python-pip python-dev build-essential python-software-properties -y

  touch /home/done.sh

fi

# Pip global
if [[ ! -f /usr/local/bin/virtualenvwrapper.sh ]]; then

    echo "-- Install Virtualenvwrapper --"
    pip install virtualenv==1.10.1
    pip install virtualenvwrapper

fi

# Profile
if [[ ! -f /home/vagrant/bash_profile.sh ]]; then

  echo "-- CP Bash Profile --"
  cp /home/options/.bash_profile /home/vagrant/.bash_profile

fi

# Install python requirements
if [[ ! -f /home/vagrant/.virtualenvs/tstoApp/bin/activate ]]; then

  echo "-- Config virtualenv --"
  sudo -u vagrant virtualenv /home/vagrant/.virtualenvs/tstoApp
  echo "---- Install requirements ----"
  sudo -u vagrant PYTHONUNBUFFERED=1 sh -c ". /home/vagrant/.virtualenvs/tstoApp/bin/activate && sudo pip install --upgrade pip && sudo pip install -r /home/tstoApp/requirements.txt"

fi
