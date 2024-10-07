
# carpark = [["Empty1","Empty2","Empty3"],
#            ["Empty4","Empty5","Empty6"],
#            ["Empty7","Empty8","Empty9"]]
           
# row = 1
# col = 0
rows = 10
cols = 20

carpark = [["Empty" for col in range(cols)] for row in range(rows)]

carpark[0][0]="Full"
print(carpark)
def message():
    print('My First Library')
#end procedure



def main():
    print('this is my main bit of code')
    message()


if __name__ == '__main__':
    main()
