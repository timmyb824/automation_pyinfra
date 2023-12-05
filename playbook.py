from pyinfra.operations import server

from deploys.create_vm_template import create_vm_template
from deploys.docker_ce import deploy_docker
from deploys.update_pkgs import update_packages
from deploys.upgrade_pkgs import upgrade_packages
from deploys.uptime import uptime

# Useful for testing with Vagrant
# from pyinfra import config
# config.SU_USER=""

# This is the playbook file. It is the entry point for my pyinfra deployment scripts.
# Uncomment the functions you want to run and run this file
DEPLOY_FUNCS = [
    # update_packages,
    # upgrade_packages,
    # uptime
    # deploy_docker,
    # create_vm_template,
    # Function with arguments example:
    # lambda: deploy_docker(config={...})
]

for func in DEPLOY_FUNCS:
    func()
