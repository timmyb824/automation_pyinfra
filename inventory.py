import os

servers = [
    (
        "watchyourlan.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "actualbudget.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "adguard.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "podman-01.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "hp-laptop-ubuntu.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "pihole2.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "logging.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "prometheus.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
]

db = [
    (
        "mongodb.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "postgresql.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
]

proxmox = [
    (
        "proxmox2.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "proxmox3.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
]

special = [
    (
        "rasberrypi.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
        },
    ),
]

k8s = [
    (
        "vm310.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "ssh_port": 22,
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm313.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm314.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "ssh_port": 22,
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm320.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "ssh_port": 22,
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm321.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "ssh_port": 22,
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm322.homelab.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "ssh_port": 22,
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
]

oci = [
    (
        "homelab-oci01.homelab.lan",
        {
            "ssh_user": "ubuntu",
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
        },
    ),
    (
        "homelab-oci03.homelab.lan",
        {
            "ssh_user": "opc",
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
        },
    ),
]
