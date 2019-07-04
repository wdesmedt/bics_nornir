# bics_nornir
Nornir is a Python automation framework that provides support for concurrent execution of tasks against a set of hosts. It comes with pluggable inventory and task capabilities to promote composability and reusability.

`Bics_nornir` provides a set of BICS-developed plugins that addresses required functionality for communicating with the infrastructure as well as plugins as building blocks to implement _runbooks_. These plugins are:

- `.../plugins/connections/ncclient`: a connection plugin that uses `ncclient` to communicate with devices using Netconf
- `.../plugins/tasks/networking/nc`: a set of high-level task-plugins:
    - `get_config`: retrieves (a part of) the device's configuration using netconf. The selection of a subtree of the configuration is through the `path` parameter
    - `get`/ retrieves (a part of) the device's state information using netconf.
    - `nc_configure`: sends a configuration (python object) to the device, with support of candidate/running comparision, dry-run and associated commit() and discard()
- `.../plugins/tasks/data/load_intent`: loads intent files from a directory

# Installation
1. set up your Python virtualenv (e.g. `python3 -m venv v ; source v/bin/activate`)

## Install using pip
This is the recommended method if you're familiar with the plugins or when you want to run a Nornir _runbook_. 
2. install `bics_nornir` using pip from the default public PyPI repository:
    `pip install bics-nornir`
    This will install bics_nornir and all its dependencies, including `nornir` and its depdendencies, in the current Python environment.

## Install using Git
This is the recommended method if you want to familiarize yourself with the plugin functionality.
2. install `nornir` with `pip install nornir` from a PyPI repo that has the Nornir package and its depdendencies (default: pypi.org)
3. clone the bics_nornir Git repo into the current project dir: `git clone https://bcgit.bc/wdesmedt/bics_nornir.git`
4. install `poetry` with `pip install poetry`
5. install dependencies with `poetry install`

The bics_nornir package is now available for use within the local Python environment.

# Usage
The bics_nornir package introduces support for netconf connections to Nokia SROS routers. In order to use Nornir and bics_nornir plugins, following is required:

- a Nornir config file (see Nornir documentation for details). This config file must reference an Inventory plugin (defaul:SimpleInventory) that has appropriate host entries to reachable Nokia SROS devices (see examples directory for a sample config file)
- a Nornir inventory, referenced from the config file, containing reachable hosts and appropriate username/password (see examples directory for a sample inventory (type:SimpleInventory)) 
- one or more reachable nokia SROS nodes referenced in the inventory. 

A reachable node means netconf must be enabled for the user so that `ssh user@router -p 830 -s netconf` returns:
```
~ ssh nc@172.30.2.2 -p 830 -s netconf
TiMOS-B-16.0.R7 both/x86_64 Nokia 7750 SR Copyright (c) 2000-2019 Nokia.
All rights reserved. All use subject to applicable license agreements.
Built on Wed Apr 10 16:45:38 PDT 2019 by builder in /builds/c/160B/R7/panos/main

nc@172.30.2.2's password:
<?xml version="1.0" encoding="UTF-8"?>
<hello xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <capabilities>
        <capability>urn:ietf:params:netconf:base:1.0</capability>
        <capability>urn:ietf:params:netconf:base:1.1</capability>
        <capability>urn:ietf:params:netconf:capability:candidate:1.0</capability>
        <capability>urn:ietf:params:netconf:capability:confirmed-commit:1.1</capability>
        <capability>urn:ietf:params:netconf:capability:notification:1.0</capability>
        <capability>urn:ietf:params:netconf:capability:interleave:1.0</capability>
...
```
Also, model-driven configuration-mode must be enabled on the nodes to support configuration candidates.

Install Jupyter with `pip install jupyter` and run the included notebook _nornir_netconf.ipynb_ to get familiar with the plugins:
    ```
    cd examples
    jupyter notebook nornir_netconf.ipynb
    ```

# Todo
- make connection plugin multi-vendor. Current implementation is for Nokia SROS only

