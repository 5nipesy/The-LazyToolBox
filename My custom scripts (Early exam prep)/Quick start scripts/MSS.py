import time

# create index.html file and write HTML syntax
with open("index.html", "w") as html_file:
    html_file.write("<!DOCTYPE html>\n")
    html_file.write("<html lang=\"en\">\n")
    html_file.write("<head>\n")
    html_file.write("  <meta charset=\"UTF-8\">\n")
    html_file.write("  <meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n")
    html_file.write("  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n")
    html_file.write("  <link rel=\"stylesheet\" href=\"style.css\">\n")
    html_file.write("  <link rel=\"stylesheet\" href=\"color.css\">\n")
    html_file.write("  <link rel=\"stylesheet\" href=\"media_queries.css\">\n")
    html_file.write("  <title>Document</title>\n")
    html_file.write("</head>\n")
    html_file.write("\n")
    html_file.write("<body>\n")
    html_file.write("  <header></header>\n")
    html_file.write("  <nav></nav>\n")
    html_file.write("  <main>\n")
    html_file.write("    <!-- correct structure -->\n")
    html_file.write("    <article>\n")
    html_file.write("      <section>\n")
    html_file.write("        <!-- work in here  -->\n")
    html_file.write("      </section>\n")
    html_file.write("    </article>\n")
    html_file.write("  </main>\n")
    html_file.write("  <footer></footer>\n")
    html_file.write("</body>\n")
    html_file.write("<!-- for scripts  -->\n")
    html_file.write("<script></script>\n")
    html_file.write("<script src=\"\"></script>\n")
    html_file.write("</html>\n")

# create style.css file and write CSS syntax
with open("style.css", "w") as css_file:
    css_file.write("/* Add your CSS styles here */\n")

# create color.css file and write CSS syntax
with open("color.css", "w") as css_file:
    css_file.write("/* Add your CSS styles for colors here */\n")
    
# create media_queries.css file and write CSS syntax
with open("media_queries.css", "w") as css_file:
    css_file.write("/* Add your CSS styles here */\n")
    css_file.write("\n")
    css_file.write("/* Desktop styles */\n")
    css_file.write("@media (min-width: 1025px) {\n")
    css_file.write("  /* Add your desktop styles here */\n")
    css_file.write("}\n")
    css_file.write("\n")
    css_file.write("/* Tablet styles */\n")
    css_file.write("@media (min-width: 769px) and (max-width: 1024px) {\n")
    css_file.write("  /* Add your tablet styles here */\n")
    css_file.write("}\n")
    css_file.write("\n")
    css_file.write("/* Phone styles */\n")
    css_file.write("@media (max-width: 768px) {\n")
    css_file.write("  /* Add your phone styles here */\n")
    css_file.write("}\n")

print("Waiting for main script to run...")
time.sleep(10)  # wait for 10 seconds

# define num_variables before running set_variables script
num_variables = None

while True:
    print("Which script would you like to run next? set_variables, extract_hex_values or exit?")
    script = input("Enter the name of the script: ")
    if script == "exit":
        break
    elif script == "set_variables":
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
    elif script == "extract_hex_values":
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
    else:
        print("Invalid script name. Please try again.")
        

        
        
#         This script creates four files: index.html, style.css, color.css, and media_queries.css.

# index.html is an HTML file that defines the structure of a webpage. It includes elements such as <html>, <head>, <body>, <header>, <nav>, <main>, <article>, <section>, <footer>, and <script>.

# style.css is a CSS file that controls the styling of the webpage. It's a blank file, and you can add your own CSS styles to it.

# color.css is also a CSS file that controls the colors of the webpage. It's a blank file, and you can add your own CSS styles for colors to it.

# media_queries.css is a CSS file that specifies different styles for different screen sizes. It includes @media rules for desktop, tablet, and phone styles. You can add your own styles to these different rules.

# After creating these files, the script prints a message and waits for 10 seconds before asking wich is the next script to launch
