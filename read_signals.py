import json
import csv
import pandas as pd
from datetime import datetime, timedelta
import pytz

filename = 'test/test_reg_signal.txt'

pdt = pytz.timezone("America/Los_Angeles")
data = []
# with open(filename, 'r') as input_file:
#     reader = csv.reader(input_file)
#     next(reader)
#     for row in reader:
#         start = pdt.localize(datetime.strptime(str(row[0]), "%m/%d/%y %H:%M")).isoformat()
#         end = pdt.localize(datetime.strptime(str(row[0]), "%m/%d/%y %H:%M") + timedelta(seconds=4)).isoformat()
#         setpoint = float(row[1])
#         # create new dict
#         signal_dict = {}
#         signal_dict['utility_id'] = 1
#         signal_dict['start_date'] = start
#         signal_dict['end_date'] = end
#         signal_dict['setpoint'] = setpoint
#
#         data.append(signal_dict)
#         # data = json.dumps(event)
#
# with open(jsonfile, 'w') as outfile:
#     json.dump(data, outfile,ensure_ascii=False)

# start = datetime.strftime(datetime.now(), "%a, %b %d %Y")
# end = pdt.localize(datetime.strptime(start, "%m/%d/%y %H:%M") + timedelta(seconds=60)).isoformat()
# print(end)
signal = pd.read_csv(filename, header=None)
signal.columns = ['date', 'signal']
signal['abs_signal'] = signal.signal + 50

rng = pd.date_range('1/2/2019 15:30:00', periods=3600, freq='S')
signal.index = rng
print(datetime.now())
print(signal.iloc[signal.index.get_loc(datetime.now(), method='nearest')]['abs_signal'])
print(signal)
