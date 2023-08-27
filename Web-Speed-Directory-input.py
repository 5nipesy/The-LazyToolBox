import os
import tkinter as tk

# Function to handle button click
def on_submit():
    global number
    number = entry.get()
    root.destroy()

# Function to handle enter key press
def on_enter(event):
    # Check if the entry field is not empty
    if entry.get():
        on_submit()
    else:
        # Close the window
        root.quit()

# Create the Tkinter window
root = tk.Tk()
root.title("Enter a number")

# Create the label and place it above the entry field
label = tk.Label(root, text="day ( ) ?")
label.pack()

# Create the entry field and submit button
entry = tk.Entry(root)
entry.pack(padx=10)
submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

# Bind the enter key to the entry field
entry.bind("<Return>", on_enter)

# Run the Tkinter main loop
root.mainloop()


# Create the "opgaver" folder
dayFolder = f"day {number}"
os.makedirs(dayFolder, exist_ok=True)

# Create the "day_intro" and "day_opgave" folders inside the "opgaver" folder
day_intro_folder = os.path.join(dayFolder, "day_intro")
os.makedirs(day_intro_folder, exist_ok=True)
day_opgave_folder = os.path.join(dayFolder, "day_opgave")
os.makedirs(day_opgave_folder, exist_ok=True)

# Create the HTML file inside the "day_intro" folder
intro_html_filename = os.path.join(day_intro_folder, "intro.html")
with open(intro_html_filename, "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<title>Intro</title>\n")
    f.write("</head>\n")
    f.write("<body>\n")
    f.write('<script src="./intro.js"></script>')
    f.write("</body>\n")
    f.write("</html>")

# Create the HTML files inside the "day_opgave" folder
for i in range(1, 6):
    filename = os.path.join(day_opgave_folder, f"Øvelse{i}.html")
    with open(filename, "w", encoding="utf-8") as f:
        f.write("<!DOCTYPE html>\n")
        f.write("<html>\n")
        f.write("<head>\n")
        f.write(f"<title>Øvelse{i}</title>\n")
        f.write("</head>\n")
        f.write("<body>\n")
        if i > 1 or i < 5:
         f.write('<div style="display: flex; column-gap: 3px;">\n')
        if i > 1:
         f.write(f'  <button style= "border-radius:3px; "><a href="Øvelse{i-1}.html" style="text-decoration: none;">previous</a></button>\n')
        if i < 5:
         f.write(f'  <button style= "border-radius:3px; "><a href="Øvelse{i+1}.html" style="text-decoration: none;">next</a></button>\n')
        f.write('</div>\n')
        f.write(f'<script src="./js/Øvelse{i}.js"></script>')
        f.write("</body>\n")
        f.write("</html>")

# Create the "js" folder inside the "opgaver" folder
js_folder = os.path.join(day_opgave_folder, "js")
os.makedirs(js_folder, exist_ok=True)

# Create the JavaScript file inside the "js" folder for the intro HTML file
intro_js_filename = os.path.join(day_intro_folder, "intro.js")
with open(intro_js_filename, "w", encoding="utf-8") as f:
    f.write("// This is the intro script\n")
    f.write("console.log('Hello from intro!');\n")

# Create the JavaScript files inside the "js" folder for the Øvelse HTML files
for i in range(1, 6):
    filename = os.path.join(js_folder, f"Øvelse{i}.js")
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"// This is script {i}\n")
        f.write(f"console.log('Hello from Øvelse{i}!');\n")
