outlets, quarters = (50, 4)  
outlet_sales = [[0 for i in range(quarters)] for j in range(outlets)]  
print(outlet_sales)
total = [5,13,45,12]
for quarter in range(quarters):
    total[quarter]=0
    for outlet in range(outlets):
        total[quarter] = total[quarter]  + outlet_sales[outlet][quarter]
    #next outlet
    print("Quarter", quarter+1,"Total is",total[quarter])
#next quarter

