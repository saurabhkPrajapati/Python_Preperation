from datetime import datetime, timedelta

timestamp = 1617253820000
dt = datetime.fromtimestamp(timestamp / 1000)  # Divide by 1000 for milliseconds
print(dt)


# Get the current time in milliseconds
end_time = int(datetime.now().timestamp() * 1000)
# Get the time 24 hours ago in milliseconds
start_time = int((datetime.now() - timedelta(days=1)).timestamp() * 1000)
a = (datetime.now() - timedelta(minutes=20)).timestamp() * 1000

print(end_time, start_time)
