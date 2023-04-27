#open mylife.txt file with the write method
file = open("mylife.txt", "w" )

#use a while loop to keep asking for user text input and store in file until stopped
while True:
    ##ask for user input
    text = input("Enter line: ")
    ##write it over to the file
    file.write(text + "\n")
    ##if there are more line of text to input, type y for yes/continue and n for no/stop
    option = input("Are there more lines (y/n)? ")
    ##continue the loop until the user terminate the loop
    if option.lower() == "n":
        break 

#file close
file.close() 