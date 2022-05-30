from libcloud.compute.types import Provider
from libcloud.compute.providers import get_driver
from dotenv import dotenv_values

config = dotenv_values(".env")

ACCESS_ID = config["ACCESS_ID"]
SECRET_KEY = config["SECRET_KEY"]

cls = get_driver(Provider.EC2)
driver = cls(ACCESS_ID, SECRET_KEY, region="us-east-1")

images = driver.list_images()

print(images)