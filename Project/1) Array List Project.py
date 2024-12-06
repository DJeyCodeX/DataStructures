
user_input = int(input("How many day's temperature?: "))
lst= []
for i in range(user_input):
    temperature = float(input(f"Day {i+1} high temperature: "))
    lst.append(temperature)
avg = round(sum(lst)/user_input,2)
print("Average = ", avg)

total = 0
for i in lst:
    if i > avg:
        total += 1
print(str(total), "day(s) above average")
