from pyinfra import host
from pyinfra.api.deploy import deploy
from pyinfra.facts.server import Hostname, LinuxName
from pyinfra.operations import apt, dnf, server


def _apt_update() -> None:
    apt.update(
        name="Update apt repositories",
        cache_time=3600,
        _sudo=True,
    )


def _dnf_update() -> None:
    dnf.update(name="Update dnf repositories", _sudo=True)


UPDATE_FUNCTIONS = {
    "Ubuntu": _apt_update,
    "Raspbian GNU/Linux": _apt_update,
    "Oracle Linux Server": _dnf_update,
    "Debian": _apt_update,
}


@deploy("Update packages")
def update_packages() -> None:
    linux_name = host.get_fact(LinuxName)

    update_function = UPDATE_FUNCTIONS.get(linux_name)

    if update_function is None:
        raise NotImplementedError(f"No update function for {linux_name}")

    update_function()
