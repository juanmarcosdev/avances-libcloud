from google.cloud import monitoring_v3

import time

client = monitoring_v3.MetricServiceClient()
project = 'multicloudloadbalancer'  # TODO: Update to your project ID.
project_name = f"projects/{project}"

series = monitoring_v3.TimeSeries()
series.metric.type = "custom.googleapis.com/my_metric"
series.resource.type = "gce_instance"
series.resource.labels["instance_id"] = "6528037005282655319"
series.resource.labels["zone"] = "us-central1-a"
now = time.time()
seconds = int(now)
nanos = int((now - seconds) * 10 ** 9)
interval = monitoring_v3.TimeInterval(
    {"end_time": {"seconds": seconds, "nanos": nanos}}
)

point = monitoring_v3.Point({"interval": interval, "value": {"double_value": 3.14}})
series.points = [point]
client.create_time_series(request={"name": project_name, "time_series": [series]})
print("Successfully wrote time series.")