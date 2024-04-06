import os
import re

# Define the path to the directory
path = "./filestack"

uuids = set()
file_uuids = []
content_uuids = []
count = 0


def next_file_name(file_name):
    with open(file_name, "r") as file:
        content = file.read()
        match = re.search(r"filestack/(.+)", content)
        if match:
            return match.group(1)
        else:
            return None


if __name__ == "__main__":

    for filename in os.listdir(path):
        count += 1
        uuids.add(filename)
        file_uuids.append(filename)
        # Open the file
        with open(os.path.join(path, filename), "r") as file:
            # Read the content
            content = file.read()

            # The files with the correct uuids have a different length, due to a newline character
            if len(content) != 36:
                print(content)
            else:
                # Delete the file (otherwise the GitHub repo would be too big)
                os.remove(os.path.join(path, filename))

            uuids.add(content)
            content_uuids.append(content)

    print("Flag is THAINNOS{<last-part-of-uuid-a><last-part-of-uuid-b>}")
