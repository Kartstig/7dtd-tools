# 7dtd-tools
A toolkit for 7dtd servers

## Setup
```bash
$ ./script/setup.sh
```

This will install the python environment and dependencies

## Running
```bash
$ source venv/bin/activate
(venv)$ fab instance:my_instance stop
(venv)$ fab instance:my_instance copy_configs
(venv)$ fab instance:my_instance deploy_configs
...
```