def write_to_file(filename):
    try:
        with open(filename, 'w') as f:
            f.write("Almost done now\n")
            f.write("Age is just a number\n")
            f.write("We shall overcome\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to write to '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("File created and written successfully.")

def read_and_display(filename):
    try:
        with open(filename, 'r') as f:
            contents = f.read()
            print("Contents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to read from '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")

def append_to_file(filename):
    try:
        with open(filename, 'a') as f:
            f.write("\nThis is it\n")
            f.write("The people shall \n")
            f.write("Damn, this is goooood\n")
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except PermissionError:
        print(f"Error: Permission denied to append to '{filename}'.")
    except Exception as e:
        print(f"Error: {e}")
    else:
        print("File appended successfully.")

if __name__ == "__main__":
    filename = "my_file.txt"

    # Writing to file
    write_to_file(filename)

    # Reading and displaying file contents
    read_and_display(filename)

    # Appending to file
    append_to_file(filename)

    # Reading and displaying updated file contents
    read_and_display(filename)