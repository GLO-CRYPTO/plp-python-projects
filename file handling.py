
def process_file():
    try:
        # Step 1: Ask the user for a filename
        input_filename = input("Enter the filename you want to read: ")

        # Step 2: Try to open and read the file
        with open(input_filename, "r") as infile:
            content = infile.read()

        print("\nOriginal file content:\n")
        print(content)

        # Step 3: Modify the content (example: convert to uppercase)
        modified_content = content.upper()

        # Step 4: Ask for an output filename
        output_filename = input("\nEnter the name for the new file: ")

        # Step 5: Write modified content to new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"\nModified content has been written to '{output_filename}'")

    except FileNotFoundError:
        print("Error: That file does not exist. Please check the filename and try again.")
    except PermissionError:
        print("Error: You don’t have permission to read this file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
process_file()
