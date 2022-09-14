# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

print ("Which conversion would you like to use?")
print ("1: KPH")
print ("2: m/s")
print ("3: ft/s")
choice = input("Input the number corresponding to your choice: ")

def mph_to_kph(mph):
    return 1.609*mph

def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600

def mph_to_fts(mph):
    return mph*5280/3600

def get_mph():
    mph = input("Input speed in mph: ")
    mph = float(mph)
    return mph

if choice == "1":
    mph = get_mph()
    print("Speed in kph is", mph_to_kph(mph))

elif choice == "2":
    mph = get_mph()
    print("Speed in m/s is", mph_to_ms(mph))

elif choice == "3":
    mph = get_mph()
    print("Speed in ft/s is", mph_to_fts(mph))
else:
    print("Invalid menu option")