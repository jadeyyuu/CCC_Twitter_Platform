#!/bin/bash

. ./CCC-grp-30-openrc.sh; ansible-playbook --ask-become-pass set_environment.yaml -i inventory/hosts.ini 