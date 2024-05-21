file = input("file name: ").strip().lower()

if "." not in file:
    print("application/octet-stream")

elif file.rsplit(".", 1)[1] == "jpg" or file.rsplit(".", 1)[1] == "jpeg":
    print("image/jpeg")

elif file.rsplit(".", 1)[1] == "gif":
    print("image/gif")

elif file.rsplit(".", 1)[1] == "png":
    print("image/png")

elif file.rsplit(".", 1)[1] == "pdf":
    print("application/pdf")

elif file.rsplit(".", 1)[1] == "txt":
    print("text/plain")

elif file.rsplit(".", 1)[1] == "zip":
    print("application/zip")

else:
    print("application/octet-stream")
