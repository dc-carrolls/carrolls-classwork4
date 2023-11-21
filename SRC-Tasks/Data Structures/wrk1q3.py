Outlet1Sales_array = [10, 12,15,10]
Outlet2Sales_array = [5,8,3,6]
Outlet3Sales_array = [10,12,15,10]

for qtr in range(4):
    total=Outlet1Sales_array[qtr]+Outlet2Sales_array[qtr]+Outlet3Sales_array[qtr]
    print("Total for quarter",qtr+1,total)
#next qtr