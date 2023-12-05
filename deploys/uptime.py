from pyinfra.api.deploy import deploy
from pyinfra.operations import server


# deploy function to check uptime
@deploy("Check uptime")
def uptime():
    server.shell(
        name="Check uptime",
        commands="echo ",
    )
