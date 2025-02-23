# Prompt user for input as a file name
file_name = input("File name: ")

# Strip whitespace from input and convert to lowercase for standardisation
new_file_name = file_name.strip().lower()

# Check the media type
if new_file_name.endswith(".gif"):
    media_type = "image/gif"
elif new_file_name.endswith(".jpg"):
    media_type = "image/jpeg"
elif new_file_name.endswith(".jpeg"):
    media_type = "image/jpeg"
elif new_file_name.endswith(".png"):
    media_type = "image/png"
elif new_file_name.endswith(".pdf"):
    media_type = "application/pdf"
elif new_file_name.endswith(".txt"):
    media_type = "text/plain"
elif new_file_name.endswith(".zip"):
    media_type = "application/zip"
else:
    media_type = "application/octet-stream"

# Print out the results
print("Media type:", media_type)