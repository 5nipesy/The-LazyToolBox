# ask user for number of sections
num_sections = int(input("Enter the number of sections: "))

# open index.html file and write HTML syntax
with open("index.html", "a") as html_file:
    html_file.write("<!-- remember to move this up into the article space above  -->  \n")
    html_file.write("  <article>\n")

    # open style.css file and write CSS syntax
    with open("style.css", "a") as css_file:
        # ask user for number of divs per section
        for i in range(num_sections):
            num_divs = int(input(f"Enter the number of divs for section {i+1}: "))

            # write section and divs to index.html file
            html_file.write(f"    <section id=\"section{i+1}\">\n")
            for j in range(num_divs):
                html_file.write(f"      <div id=\"div{j+1}\"></div>\n")
            html_file.write("    </section>\n")

            # write section id to style.css file
            css_file.write(f"#section{i+1} \n")
            css_file.write("  {display: flex;\n")
            css_file.write("  /* Add your other CSS styles for section here */\n")
            css_file.write("}\n")

    html_file.write("  </article>\n")