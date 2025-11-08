import random, datetime, json

def generate_test_data(num_devices=5):
    devices = ["Heater", "Lamp", "Fan", "Air Purifier", "Humidifier"]
    data = []

    for _ in range(num_devices):
        device = random.choice(devices)
        start_time = datetime.datetime.now() - datetime.timedelta(hours=random.randint(1, 10))
        duration = random.uniform(0.5, 5)  # hours
        end_time = start_time + datetime.timedelta(hours=duration)
        power_rating = random.uniform(500, 2000)  # watts
        energy_used = power_rating * duration / 1000  # kWh

        data.append({
            "device_name": device,
            "start_time": start_time.isoformat(),
            "end_time": end_time.isoformat(),
            "power_rating_watts": round(power_rating, 2),
            "duration_hours": round(duration, 2),
            "energy_used_kwh": round(energy_used, 3),
            "location": random.choice(["Living Room", "Bedroom", "Office"]),
            "status": "completed"
        })

    return json.dumps({"devices": data}, indent=4)

if __name__ == "__main__":
    print(generate_test_data())