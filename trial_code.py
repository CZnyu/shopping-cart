from datetime import datetime, date, time, timezone

now = datetime.now()

#print(now)

dt = now.strftime("%A, %B %d, %Y %I:%M %p")

print(dt)