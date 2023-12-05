import os

servers = [
    (
        "ct102.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm304.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm305.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm306.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "timothy-hp-laptop.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "ssh_port": os.environ["SSH_PORT"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
]

db = [
    (
        "vm303.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "ssh_port": os.environ["SSH_PORT"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
]

proxmox = [
    (
        "pve2.local.lan",
        {
            "ssh_user": os.environ["SSH_USER_PVE"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
        },
    ),
    (
        "pve3.local.lan",
        {
            "ssh_user": os.environ["SSH_USER_PVE"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
        },
    ),
]

special = [
    (
        "pihole2.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
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
        "vm310.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm313.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm314.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm320.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm321.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
    (
        "vm322.local.lan",
        {
            "ssh_user": os.environ["SSH_USER"],
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
            "_use_sudo_password": os.environ["SSH_PASSWORD"],
        },
    ),
]

oci = [
    (
        "homelab-oci01.local.lan",
        {
            "ssh_user": "ubuntu",
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
        },
    ),
    (
        "homelab-oci03.local.lan",
        {
            "ssh_user": "opc",
            "ssh_key": os.environ["SSH_KEY"],
            "ssh_key_password": os.environ["SSH_KEY_PASSWORD"],
        },
    ),
]
