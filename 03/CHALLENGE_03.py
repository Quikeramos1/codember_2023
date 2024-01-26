from models import *
file_path = "03/encryption_policies.txt"
file = open_file(file_path)
print(valid_pass(file))
