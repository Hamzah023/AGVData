import time
import random
import json
import paho.mqtt.client as mqtt

client = mqtt.Client()
client.connect("test.mosquitto.org", 1883, 60) #the 60 is the keepalive interval, which is the maximum time interval in seconds between communications with the broker

agv_ids = [f"AGV-{i+1}" for i in range(3)]  # Simulate 3 AGVs
positions = {agv_id: [0, 0] for agv_id in agv_ids}
statuses = ["moving", "idle", "charging"]

try:
    while True:
        
        for agv_id in agv_ids:

            x, y = positions[agv_id]

            x += random.randint(-1, 1)
            y += random.randint(-1, 1)
            positions[agv_id] = [x, y]

            payload = {
                "agvId": agv_id,
                "x": x,
                "y": y,
                "status": random.choice(statuses)
            }

            client.publish("agv/telemetry", json.dumps(payload))
            print(f"Published: {payload}")
        time.sleep(1)

except KeyboardInterrupt:
    print("Simulation stopped.")