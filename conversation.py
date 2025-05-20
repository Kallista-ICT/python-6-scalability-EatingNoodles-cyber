time = int(input("Hey, what time is it? "))  

if time in range(6, 10):  
    hour = 'Morning'  
elif time in range(10, 14):  
    hour = 'afternoon'  
elif time in range(14, 18):  
    hour = 'evening'  
elif time in range(18, 23):  
    hour = 'night'  
else:    
    hour = 'Invalid time'  

print(f"Oh so, it's {hour}, good {hour}")  


