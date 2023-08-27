# ask user for number of variables
num_variables = int(input("Enter the number of variables: "))

# create color.css file and write CSS syntax
with open("color.css", "w") as css_file:
    css_file.write(":root {\n")

    # ask user for name and value of each variable
    for i in range(num_variables):
        name = input(f"Enter the name of variable {i+1}: ")
        value = input(f"Enter the value of variable {i+1}: ")
        css_file.write(f"  --{name}: {value};\n")

    css_file.write("}\n")

# In this script, I am creating a new file called color.css and writing CSS syntax to it. I am using the open function in Python to create and write to the file.

# I am asking the user for the number of variables that they want to include in the file. Then, I am using a for loop to iterate through each variable. For each variable, I am asking the user to enter the name and value of the variable. Finally, I am writing the name and value of the variable to the color.css file as a CSS variable.

# Overall, this script is creating a new color.css file and allowing the user to define a number of variables with their own names and values. These variables can then be used in the CSS code to specify colors or other values for the content of a web page.
