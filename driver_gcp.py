from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from libcloud.compute.deployment import ScriptDeployment

SERVICE_ACCOUNT_USERNAME = "libcloud@multicloudloadbalancer.iam.gserviceaccount.com"
SERVICE_ACCOUNT_CREDENTIALS_JSON_FILE_PATH = "./multicloudloadbalancer-4c475fb5fc9c.json"
PROJECT_ID = "multicloudloadbalancer"

ComputeEngine = get_driver(Provider.GCE)
# Note that the 'PEM file' argument can either be the JSON format or
# the P12 format.
driver = ComputeEngine(
    SERVICE_ACCOUNT_USERNAME,
    SERVICE_ACCOUNT_CREDENTIALS_JSON_FILE_PATH,
    project=PROJECT_ID,
    datacenter="us-central1-a",
)

images = driver.list_images()
sizes = driver.list_sizes()


print(images)