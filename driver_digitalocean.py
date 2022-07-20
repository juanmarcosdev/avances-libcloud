from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.deployment import ScriptFileDeployment, ScriptDeployment
import os

cls = get_driver(Provider.DIGITAL_OCEAN)

config = dotenv_values(".env")

DIGITAL_OCEAN = config["DIGITAL_OCEAN"]

driver = cls(DIGITAL_OCEAN, api_version="v2")

PRIVATE_SSH_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa_droplet")

print(PRIVATE_SSH_KEY_PATH)

#options = {"backups": True, "private_networking": True, "ssh_keys": [123456, 123457]}

#name = "test.domain.tld"
#size = driver.list_sizes()[0]
#image = driver.list_images()[0]
#location = driver.list_locations()[0]

#sizes = driver.list_sizes()
#images = driver.list_images()
#locations = driver.list_locations()

#print([x for x in sizes if "s-2vcpu-4gb" in x.name])
#print("------------------------------------------------")
#print([x for x in images if "22.04 x64" in x.name])
#print("------------------------------------------------")
#print([x for x in locations if "New York 1" in x.name])


#step = ScriptDeployment('apt update ; apt install -y make apt-transport-https ; curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg ; echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null ; apt update ; apt install -y docker-ce docker-compose ; git clone https://github.com/PokeAPI/pokeapi ; cd pokeapi ; make docker-setup')

#name = "test.domain.tld2"
#size = [x for x in sizes if "s-2vcpu-4gb" in x.name][0]
#image = [x for x in images if "22.04 x64" in x.name][0]
#location = [x for x in locations if "New York 1" in x.name][0]

#node = driver.deploy_node(deploy=step, name=name, size=size, image=image, location=location, ssh_key=PRIVATE_SSH_KEY_PATH)