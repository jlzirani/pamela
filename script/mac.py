import sys
import json

knowMac = {} 
hidden = []
resident = []
data = sys.stdin.readlines() # pipe
hiddenCount = 0
grey = []
color = []
for mac in data:
	mac = mac[:-1]
	if mac in hidden:
		hiddenCount += 1
	else:
		display = knowMac.get(mac,mac[:5]+":xx:xx:xx:xx")
		if display in resident:
			grey.append(display)
		else:
			color.append(display) 
plop = {'grey':grey,'color':color,'hidden':hiddenCount}
print json.dumps(plop)
