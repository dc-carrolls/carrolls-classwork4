msg = "Enter start time in hh:mm (24hr clock)>"
start_hrs,start_mins = [int(n) for n in input(msg).split(':')]
msg = "Enter end time in hh:mm (24hr clock)>"
end_hrs,end_mins = [int(n) for n in input(msg).split(':')]
start_mins = start_mins + 60*start_hrs
end_mins = end_mins + 60*end_hrs
time_diff = end_mins - start_mins
dist = int(input('Enter distance in miles:'))
print("Your speed was:",(dist/time_diff)*60,'mph')

