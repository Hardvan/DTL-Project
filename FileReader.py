import os


def read_files_in_directory(directory='.', file_list=None, output_file='fileContents.txt'):
    """Reads all files in a directory and writes the contents to a file.

    Args:
        - directory (str, optional): The directory to read files from. Defaults to '.'.
        - file_list (list, optional): A list of files to read. Defaults to None.
        - output_file (str, optional): The file to write the contents to. Defaults to 'fileContents.txt'.
    """

    if file_list is None:
        return

    # Open the output file
    with open(output_file, 'w', encoding='utf-8') as f:

        # Loop through the files in the list
        for file_name in file_list:

            # Construct the absolute file path
            file_path = os.path.join(directory, file_name)

            # Make sure the file exists
            if os.path.exists(file_path):

                # Open the file with the appropriate encoding
                with open(file_path, 'r', encoding='utf-8') as f2:

                    # Write the contents to the output file
                    # Title
                    f.write(f"{file_name}:\n")
                    # Contents
                    f.write(f2.read())
                    # New line
                    f.write("\n\n")

                    print(f"✅ '{file_path}' read successfully")

            else:
                print(f"File '{file_path}' does not exist.")

        # Close the output file
        f.close()


if __name__ == "__main__":

    app_py = "app.py"
    index_html = "templates/index.html"
    index_css = "static/css/index.css"
    index_js = "static/js/index.js"

    completed_html = "templates/completed.html"
    dashboard_html = "templates/dashboard.html"
    eventDetails_html = "templates/eventDetails.html"
    events_html = "templates/events.html"
    ongoing_html = "templates/ongoing.html"
    upcoming_html = "templates/upcoming.html"

    file_list = [app_py,
                 completed_html,
                 ongoing_html,
                 upcoming_html,
                 events_html,
                 ]

    read_files_in_directory(".", file_list)
