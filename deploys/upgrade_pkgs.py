from pyinfra import host
from pyinfra.api.deploy import deploy
from pyinfra.facts.server import LinuxName
from pyinfra.operations import apt, dnf, server

UPGRADE_FUNCTIONS = {
    "Ubuntu": apt.upgrade,
    "Raspbian GNU/Linux": apt.upgrade,
    "Oracle Linux Server": dnf.update,
    "Debian": apt.upgrade,
}


@deploy("Upgrade packages")
def upgrade_packages() -> None:
    linux_name = host.get_fact(LinuxName)

    upgrade_function = UPGRADE_FUNCTIONS.get(linux_name)

    if upgrade_function is None:
        raise NotImplementedError(f"No upgrade function for {linux_name}")

    upgrade_function(name=f"Upgrade {linux_name} packages", _sudo=True)
