# Specify the input file and output file names
input_file = "file_to_read.txt"
output_file = "result.txt"


# Define variables for counting and replacement
count = 0
replace_count = 0

# Read the content from the input file
with open(input_file, "r") as file:
    content = file.read()

# Calculate the total times the word "terrible" appears and display it
count = content.count("terrible")
print("The word 'terrible' appears", count, "times.")

# Replace every even occurrence with "pathetic" and odd occurrence with "marvellous"
replaced_content = ""
terrible_count = 0
for word in content.split():
    if word == "terrible":
        terrible_count += 1
        if terrible_count % 2 == 0:
            replaced_content += "pathetic "
        else:
            replaced_content += "marvellous "
    else:
        replaced_content += word + " "

# Write the new text to the output file
with open(output_file, "w") as file:
    file.write(replaced_content)

print("The new text has been written to", output_file)