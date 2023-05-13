# Taking user input
def main():
    input("What time is it? ").strip()

# using split to slice the string
def convert(time):
    hours, minutes = time.split(":")
# convert integers to float
# calculating time dividing minutes by full hour in minutes (60)
    h = float(hours)
    m = float(minutes)
    mins = m / 60
    x = h + mins
    return x

# taking the result from above calculation and convert it
t = input("What time is it? ").strip()
x = convert(t)
# check inputs against conditionals below
if 7.0 <= x <= 8.0:
    print("Breakfast time")
elif 12.0 <= x <= 13.0:
    print("Lunch time")
elif 18.0 <= x <= 19.0:
    print("Dinner time")
else:
    print("Invalid input")



