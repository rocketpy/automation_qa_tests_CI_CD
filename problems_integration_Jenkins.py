# install the module first:

#  pip install -U pytest

# create a virtualenv and execute your script inside in isolation.

#!/bin/bash

export WORKSPACE=`pwd`

# Create/Activate virtualenv
virtualenv testenv -p /path/to/python/bin
source testenv/bin/activate

pip install -U pytest 

#  run script here
....

"""
#  created virtualenv like this:

PYENV_HOME=$WORKSPACE/.pyenv/
virtualenv --no-site-packages $PYENV_HOME
source $PYENV_HOME/bin/activate
pip install -U pytest
pip install -r requirements.txt
py.test test_file_name.py 
deactivate
"""
