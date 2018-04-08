#!/usr/bin/ python
# -*- coding: utf-8 -*-
from __future__ import with_statement

import re, os
from fabric.api import task, run, sudo, \
  env, hide, put, get
from fabric.colors import red, green, yellow

import sdtdtools as sdtd
from sdtdtools.config import app_config

env.hosts = ['{}@{}:{}'.format(app_config.SSH_USER,
    app_config.HOST, app_config.SSH_PORT)]

_conf_files = [
  'admins.xml',
  'players.xml',
  'webpermissions.xml',
  'config.xml'
]

# Global Operations
@task
def uninstall():
  sudo('rm {}'.format(' '.join(sdtd.LOCAL_FILES)))
  sudo('rm -rf {}'.format(' '.join(sdtd.LOCAL_FOLDERS)))
  sudo('userdel {}'.format(sdtd.USER))
  sudo('groupdel {}'.format(sdtd.GROUP))

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
  for c in _conf_files:
    local_path = 'configs/{}/{}'.format(env.instance, c)
    remote_path = '{}/instances/{}/{}'.format(app_config.SDTD_DIR, env.instance, c)
    get(remote_path,
        local_path)

@task
def deploy_configs():
  stop()
  for c in _conf_files:
    local_path = 'configs/{}/{}'.format(env.instance, c)
    remote_path = '{}/instances/{}/{}'.format(app_config.SDTD_DIR, env.instance, c)
    put(local_path,
        remote_path,
        use_sudo=True)
    sudo('chown sdtd:sdtd {}'.format(remote_path))

  start()
