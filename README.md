# 7dtd-tools
A toolkit for 7dtd servers

## Setup
### Python Environment
```bash
$ ./script/setup.sh
```
### Configuration
```bash
$ cp Config.py.sample Config.py
```
Update these values to point to your 7DTD host

## Running
```bash
$ source venv/bin/activate
(venv)$ fab instance:my_instance stop
(venv)$ fab instance:my_instance copy_configs
(venv)$ fab instance:my_instance deploy_configs
...
```