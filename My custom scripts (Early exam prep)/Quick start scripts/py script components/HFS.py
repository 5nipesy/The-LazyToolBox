# ask user for file path
file_path = input("Enter the file path: ")

# open file and read lines
with open(file_path, "r") as file:
    lines = file.readlines()

# create color.css file and write CSS syntax
with open("color.css", "w") as css_file:
    css_file.write(":root {\n")

    # search for lines with hex values
    for i, line in enumerate(lines):
        if "#" in line:
            # remove space between hex value and # symbol
            hex_value = line.strip().replace(" #", "#")
            # get text from line above
            text = lines[i-1].strip()
            css_file.write(f"  --{text}: {hex_value};\n")

    css_file.write("}\n")

# In this script, I am asking the user for the file path of a text file. Then, I am using the open function in Python to open the file and read its lines.

# Next, I am creating a new file called color.css and writing CSS syntax to it. I am using the open function in Python to create and write to the file.

# I am using a for loop to iterate through each line in the text file. If I find a line that contains a # symbol, I know that it is a line with a hexadecimal color value. I remove the space between the hex value and the # symbol, and then I get the text from the line above. Finally, I write the text and hex value as a CSS variable to the color.css file.

# Overall, this script is reading a text file and extracting any lines with hexadecimal color values. It then creates a new color.css file and writes these values as CSS variables, along with the text from the line above the hex value. This allows the user to easily define a set of color variables that can be used in their CSS code.
