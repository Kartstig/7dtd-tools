#!/bin/bash
PIP=venv/bin/pip

if [ -d venv ]
then
  rm -rf venv/
fi
virtualenv venv/
$PIP install --upgrade pip
$PIP install -r requirements.txt
