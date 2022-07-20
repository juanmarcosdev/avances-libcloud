from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from dotenv import dotenv_values
from libcloud.compute.deployment import ScriptFileDeployment, ScriptDeployment
from libcloud.compute.base import NodeAuthSSHKey
from libcloud.compute.deployment import MultiStepDeployment
import os


config = dotenv_values(".env")

ACCESS_ID = config["ACCESS_ID"]
SECRET_KEY = config["SECRET_KEY"]

PRIVATE_SSH_KEY_PATH = "/home/marcos/Documentos/avances-libcloud/root.pem"

#key = NodeAuthSSHKey('/home/marcos/Documentos/avances-libcloud/root.pem')

cls = get_driver(Provider.EC2)
driver = cls(ACCESS_ID, SECRET_KEY, region="us-east-1")

nodes = driver.list_nodes()
#print(nodes)
print([x for x in nodes if "pokeapi" in x.name][0])

driver.start_node([x for x in nodes if "pokeapi" in x.name][0])
#filter_nodes = [x for x in nodes if x.state.value == "running"]

#print(filter_nodes[0].extra)

#key_pair = driver.create_key_pair(name="my-key-pair-7")

#text_file = open("id_rsa_ec2", "w")
#text_file.write(key_pair.private_key)
#text_file.close()

#nodes = driver.list_nodes()
#print(nodes)

#images = driver.list_images()
#sizes = driver.list_sizes()

#print(images)
#print([x for x in images if "ubuntu" in x.name])

#sizes_filter = [x for x in sizes if x.name is not None]

#print([x for x in sizes_filter if "t2.medium" in x.name])

#print(images[0])
#print(sizes[0])

#images_filter = [x for x in images if x.name is not None]

#print([x for x in images_filter if "ubuntu-22.04-x86_64-2.0.2" in x.name])

#initscript = ScriptFileDeployment("/home/marcos/Documentos/avances-libcloud/init_script.sh")

#step = ScriptDeployment('sudo apt update ; sudo apt install -y make apt-transport-https ; curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg ; echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null ; sudo apt update ; sudo apt install -y docker-ce docker-compose ; git clone https://github.com/PokeAPI/pokeapi ; cd pokeapi ; sudo make docker-setup')

#msd = MultiStepDeployment([key, step])

#step = ScriptDeployment('ls')

#node = driver.create_node(
#    image=[x for x in images_filter if "ami-052efd3df9dad4825" in x.id][0],
#    size=[x for x in sizes_filter if "t2.medium" in x.name][0],
#    name='libcloud24-aws',
#    ex_keyname="root",
#    ex_userdata="#!/bin/bash \n apt update \n apt install make"
#)


#print([x for x in images_filter if "ami-052efd3d" in x.id])