import numpy as np
import json

file = r'C:\temp\Unsicherheiten\abort_u=50_100_0001.json'

with open(file) as f:
    data = f.read()
    jdata = json.loads(data)
    avgs = np.array(jdata['gases'][0]['emissions'])

    threshold = 0.01/100
    counter = 0
    avg_r = np.array([]) # Leere Liste für Durchschnitte
    for i in range(1, avgs.size): # Geht durch das Emissions-Array
        try:
            avg_r = np.append(avg_r, np.mean(avgs[:i]))
            if abs(avg_r[-1]-avg_r[-2]) < avg_r[-2] * threshold:
                counter += 1
                #print(i, counter) # Listet alle counter auf
            else:
                counter = 0
        except:pass

    print(counter + 1)