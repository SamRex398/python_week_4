# File Read & Write Challenge 🖋️: Create a program that reads a file and writes a modified version to a new file.
# Error Handling Lab 🧪: Ask the user for a filename and handle errors if it doesn’t exist or can’t be read.
# Outcomes 🎉

# By the end of this module, you’ll be skilled in managing files efficiently in Python, ensuring error-free code that gracefully handles unexpected issues. Mastering files and exception handling will allow you to build strong, robust applications!
def main():
    try:
        filename = input("Enter the filename to read: ")
        with open(filename, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: The file '{filename}' could not be read.")
        return

    # Modify the content - convert to uppercase
    modified_content = content.upper()

    new_filename = filename.rsplit('.', 1)[0] + "_modified.txt"
    try:
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)
        print(f"Modified content written to '{new_filename}'.")
    except IOError:
        print(f"Error: Could not write to file '{new_filename}'.")

main()
