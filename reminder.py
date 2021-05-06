import time

print("what shall I remind you about?")
text=str(input())
ptint("In  how many Minutes?")
local_time = float(input())
local_time = local_time * 60
time.sleep(local_time)
print(text)