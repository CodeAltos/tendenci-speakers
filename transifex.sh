#!/usr/bin/env bash
#
# push message files to Transifex.
#
# run once and only on master branch
echo $TRAVIS_JOB_NUMBER | grep "\.1$"
if [ $? -eq 0 ] && [ $TRAVIS_BRANCH == master ]; then
    echo "Submitting translation files to Transifex"
    cd speakers
    django-admin.py makemessages -a
    pip install "transifex-client==0.10"
    # create .transifexrc file
    echo "[https://www.transifex.com]" > ~/.transifexrc
    echo "hostname = https://www.transifex.com" >> ~/.transifexrc
    echo "password = $TENDENCI_TRANSIFEX_PASSWORD" >> ~/.transifexrc
    echo "token =" >> ~/.transifexrc
    echo "username = tendenci" >> ~/.transifexrc
    tx push --source --no-interactive --skip
fi
