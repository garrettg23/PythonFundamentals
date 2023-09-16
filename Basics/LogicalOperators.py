# logical operators (and, or, not) used to check if two or more conditional statements are true

temp = int(input("What is the temperature outside?: "))

if temp>=60 and temp<=75:
    print("The temperature is mild today!")
    print("Go outside!")
elif temp>75 and temp <=90:
    print("The temperature is mildly hot today")
    print("Got outisde, but be sure to stay hydrated")
elif temp>=32 and temp<60:
    print("The temperature is chilly today")
    print("Go outside, but bring a jacket")
elif temp>90 and temp<=100:
    print("The temperature is HOT today")
    print("Enjoy the AC!")
elif temp<32 or temp>100:
    print("The weather outside sucks.")
    print("It is either too hot or too cold to go outside.")

# you can use not to reverse one or more conditional statements
if not(temp<32 or temp>100):
    print("The weather is anywhere from chilly to hot, but you can be outside")
else:
    print("You should probably stay inside")
