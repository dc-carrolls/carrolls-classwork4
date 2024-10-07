arrayEvents = [['05/02/2023','WS2','Window','38'],
               ['05/02/2023','MS1','Motion','2'],
               ['06/02/2023','DS3','Door','1'],
               ['06/02/2023','MS2','Motion','3'],
               ['06/02/2023','MS1','Motion','2'],
               ['07/02/2023','WS1','Window','24'],
               ['07/02/2023','DS1','DOor','1']
               ]

date = input('Enter date:')
events = []
for arrDate, _, _, length in arrayEvents:
    if arrDate == date:
        events.append([arrDate,length])
    #end if
#next record
time = 0
for _, length in events:
    time += int(length)
#next record
print(f"Sensors activated for {time} seconds on {date}")