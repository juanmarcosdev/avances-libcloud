from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver

from libcloud.loadbalancer.types import Provider as Provider_lb
from libcloud.loadbalancer.providers import get_driver as get_driver_lb
import os 

SERVICE_ACCOUNT_USERNAME = "libcloud@multicloudloadbalancer.iam.gserviceaccount.com"
SERVICE_ACCOUNT_CREDENTIALS_JSON_FILE_PATH = "./multicloudloadbalancer-4c475fb5fc9c.json"
PROJECT_ID = "multicloudloadbalancer"

# Path to the private SSH key file used to authenticate
PRIVATE_SSH_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa_gce")

# Path to the public SSH key file which will be installed on the server for
# the root user
PUBLIC_SSH_KEY_PATH = os.path.expanduser("~/.ssh/id_rsa_gce.pub")

ComputeEngine = get_driver(Provider_lb.GCE)
LoadBalancer = get_driver_lb(Provider_lb.GCE)
# Note that the 'PEM file' argument can either be the JSON format or
# the P12 format.
gce_driver = ComputeEngine(
    SERVICE_ACCOUNT_USERNAME,
    SERVICE_ACCOUNT_CREDENTIALS_JSON_FILE_PATH,
    project=PROJECT_ID,
    datacenter="us-central1-c",
)

print(gce_driver.list_nodes())

#LoadBalancer = lb_get_driver(LBProvider.GCE)
#lb_driver = LoadBalancer(    SERVICE_ACCOUNT_USERNAME,
#    SERVICE_ACCOUNT_CREDENTIALS_JSON_FILE_PATH,
#    project=PROJECT_ID,
#    datacenter="us-central1-c")

#print(lb_driver.list_protocols())

#images = driver.list_images()
#sizes = driver.list_sizes()
#nodes = driver.list_nodes()
#for elem in nodes:
#    print(elem)
#    print(elem.state)
#print([x for x in images if "ubuntu-2204-jammy-v2" in x.name])
#print("----------------------------------------------------------------")
#print([x for x in sizes if "e2-medium" in x.name])

#initscript = ScriptFileDeployment("/home/marcos/Documentos/avances-libcloud/init_script.sh")


#step = ScriptDeployment('apt update ; apt install -y make apt-transport-https ; curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg ; echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | tee /etc/apt/sources.list.d/docker.list > /dev/null ; apt update ; apt install -y docker-ce docker-compose ; git clone https://github.com/PokeAPI/pokeapi ; cd pokeapi ; make docker-setup')

#ex_metadata = metadata = {
#    "items": [{"key": "startup-script", "value": initscript}]
#}

#node = driver.deploy_node(
#    image=[x for x in images if "ubuntu-2204-jammy-v2" in x.name][0],
#    size=[x for x in sizes if "e2-medium" in x.name][0],
#    deploy=step,
#    name='libcloud11',
#    ssh_key=PRIVATE_SSH_KEY_PATH,
#    )

#print([x for x in images if "ubuntu" in x.name])
#print(sizes)
#print([x for x in sizes if "f1-micro" in x.name])
#print(nodes)

#nodes = driver.list_nodes()

#print(dir(nodes[0]))
#print(nodes[0].extra)