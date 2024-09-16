temperature_readings = [25, 28, 21, 24, 27]
#Average Temperature: 25.0
#Highest Temperature: 28
#Lowest Temperature: 21
sum_of_temp=0
max_temp=float('-inf')
min_temp=float('inf')
for temp in temperature_readings:
    sum_of_temp+=temp
    max_temp=max(max_temp,temp)
    min_temp=min(min_temp,temp)

avg_temp=sum_of_temp/len(temperature_readings)

print(f"Average Temperature: {avg_temp}")
print(f"Highest Temperature: {max_temp}")
print(f"Lowest Temperature: {min_temp}")