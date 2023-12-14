import re
message = "Tuesday: 22C, Wednesday: 21C, Thursday: 26C "

message = re.findall(r"\d{2}", message)
print(message)
message= [int(x) for x in message]
print(sum(message)//len(message))

