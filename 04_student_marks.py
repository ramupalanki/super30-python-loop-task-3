marks = [78, 92, 45, 67, 88, 53, 99]
above_90=0
between_75_89=0
between_50_74=0
below_50=0
for mark in marks:
    if mark>=90:
        above_90+=1
    elif mark>=75 and mark<=89:
        between_75_89+=1
    elif mark>=50 and mark<=74:
        between_50_74+=1
    else:
        below_50+=1

print("Number of marks above 90:", above_90)
print("Number of marks between 75 and 89:", between_75_89)
print("Number of marks between 50 and 74:", between_50_74)
print("Number of marks below 50:", below_50)