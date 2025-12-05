with open("artifacts/text.txt", "r") as f:
    s = f.read()
    print(s)


with open("artifacts/output.txt", "w") as f:
    f.write("I am learning DVC")
    print("output file created successfully")