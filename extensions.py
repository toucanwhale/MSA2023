#get user input
file_name = input("Please enter the file name: ")
#convert inputs to lowercase 
#find file types
file_type = ((file_name.casefold())[(file_name.find(".")) + 1:])

#print the corresponding file type
if file_type == "gif":
    print("image/gif")
elif file_type == "jpg":
    print("image/jpeg")
elif file_type == "jpeg":
    print("image/jpeg")
elif file_type == "png":
    print("image/png")
elif file_type == "pdf":
    print("document/pdf")
elif file_type == "txt":
    print("document/txt")
elif file_type == "zip":
    print("file/zip")
else:
    print("application/octet-stream")
