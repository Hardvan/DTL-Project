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
                print(f"❌ File '{file_path}' does not exist.")

        # Close the output file
        f.close()


if __name__ == "__main__":

    # .py files
    app_py = "app.py"
    post_handler_py = "PostHandler.py"

    # .html files
    dashboard_html = "templates/dashboard.html"
    chatbot_html = "templates/chatbot.html"
    events_html = "templates/events.html"
    all_in_one_html = "templates/all_in_one.html"
    eventDetails_html = "templates/eventDetails.html"
    find_location_html = "templates/find_location.html"
    clubDetails_html = "templates/clubDetails.html"

    # .css files
    achieve_css = "static/styles/achieve.css"
    card_css = "static/styles/card.css"
    chatbot_css = "static/styles/chatbot.css"
    dashboard_css = "static/styles/dashboard.css"
    events_css = "static/styles/events.css"
    find_location_css = "static/styles/find_location.css"
    navbar_css = "static/styles/navbar.css"

    # .js files
    index_js = "static/js/index.js"
    chatbot_js = "static/javaScript/chatbot.js"

    file_list = [
        dashboard_html,
        dashboard_css,
        card_css,
        navbar_css
    ]

    read_files_in_directory(".", file_list)
