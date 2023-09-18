import time
# nested loops = the "inner loop" will finish all of it's iterations before
# finishing one iteration of the "outer loop"

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")  # end="" will prevent cursor for going to next line after a print
        time.sleep(.25)
    time.sleep(.25)
    print(" Row is done!") # Symbolizes each iteration of outer loop, use print("") for cleaner output
