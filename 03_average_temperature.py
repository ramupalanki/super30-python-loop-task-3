temperatures = [32, 35, 28, 40, 38, 31, 42]
total_marks=0
for temperature in temperatures:
    total_marks+= temperature
print("Average temparature is ",total_marks/len(temperatures))