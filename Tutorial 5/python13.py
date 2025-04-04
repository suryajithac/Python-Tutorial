import os
print("Files and folders in current directory:")
for item in os.listdir("."):
    print(item)