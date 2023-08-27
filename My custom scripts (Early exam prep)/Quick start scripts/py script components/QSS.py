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


# this script is creating three new files: index.html, style.css, and color.css. The first file, index.html, is written in HTML and contains the structure and content of a web page. The second file, style.css, is written in CSS and is used to style the content of the web page. The third file, color.css, is also written in CSS and is used to specify colors for the content of the web page.

# I am using the open function in Python to create and write to these files. For the index.html file, I am writing specific lines of HTML code to it. For the style.css and color.css files, I am writing comments to them, which are lines of text that provide information or explanations to someone reading the code.

# Overall, this script is creating three new files and writing some basic syntax to them. These files are the base of my website