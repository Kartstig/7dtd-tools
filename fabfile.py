#!/usr/bin/ python
# -*- coding: utf-8 -*-
from __future__ import with_statement

import re, os
from fabric.api import task, run, sudo, \
  env, hide, put, get
from fabric.colors import red, green, yellow
from sdtdtools.config import app_config

env.hosts = ['{}@{}:{}'.format(app_config.SSH_USER,
    app_config.HOST, app_config.SSH_PORT)]

# Global Operations

@task
def updateengine():
  sudo('{} updateengine'.format(app_config.SDTD_SCRIPT))

@task
def updatescripts():
  sudo('{} updatescripts'.format(app_config.SDTD_SCRIPT))

@task
def updatefixes():
  sudo('{} updatefixes'.format(app_config.SDTD_SCRIPT))

@task
def instances():
  with hide('output'):
    r = sudo('{} instances list'.format(app_config.SDTD_SCRIPT))
    print(yellow(r))

@task
def instance(instance_name):
  env.instance = instance_name

# Instance Operations

@task
def stop():
  sudo('{} kill {}'.format(app_config.SDTD_SCRIPT, env.instance))

@task
def start():
  sudo('{} start {}'.format(app_config.SDTD_SCRIPT, env.instance))

@task
def restart():
  stop()
  start()

@task
def copy_configs():
  config_files = ['admins.xml', 'players.xml', 'webpermissions.xml']
  for c in config_files:
    get('{}/instances/{}/{}'.format(app_config.SDTD_DIR, env.instance, c),
        'configs/{}/{}'.format(env.instance, c))

@task
def deploy_configs():
  config_files = ['admins.xml', 'players.xml', 'webpermissions.xml']
  stop()
  for c in config_files:
    orig_path = 'configs/{}/{}'.format(env.instance, c)
    dest_path = '{}/instances/{}/{}'.format(app_config.SDTD_DIR, env.instance, c)
    put(orig_path,
        dest_path,
        use_sudo=True)
    sudo('chown sdtd:sdtd {}'.format(dest_path))

  start()