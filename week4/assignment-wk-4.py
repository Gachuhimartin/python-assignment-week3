# file = open("jsMummies_Contacts.txt","w")
# file.write("Jsmammi1,Jsmammies2,Jsmammies3")


# #Appending to the file
# file = open("jsMummies_Contacts.txt","a")
# file.write("\n Ooh my sheila,I love you so much")

#Read the file
# file = open("jsMummies_Contacts.txt","r")
# content = file.readline()
# print(content)


#Reading image content from a file

# image_file =open("/home/mockingbird/PLP folder/Python/Screenshot_2025-02-11_16_26_51.png","rb")
# image_data=image_file.read()
# print(image_data[:100])

#Read the contents of input.txt

# Read the contents of input.txt.
file = open("input.txt","r")

content = file.read()
 
print(content)

# Count the number of words in the file.

print("Number of words in this file is:",len(content))

# Convert all text to uppercase.

print("File contents in upppercase: ",content.upper())

# Write the processed text and the word count to a new file called output.txt.

new_file = open("output.txt","w")
new_file.write(
    f"Number of words in this file is: {len(content)}\n"
    f"File contents in upppercase: { content.upper()}"
    )