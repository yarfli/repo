import sys
import getpass
import os
import subprocess

sys.path.insert(0, "/content/repo/python")
from scs_crypt.crypt import encrypt_string_user, decrypt_string_user, encrypt_string, decrypt_string_user_pass

string1='gAAAAABmS0KUdcjBPea2C2kLdzOMk5aoyXrT7hAwLTUFiy5zlAH7Mx0TyRRiTOZYb--jdBDHD-4iSOXY2-onWR_aO5qG0jfA6Q=='
# 
# pass 1234
val = decrypt_string_user_pass(string1)
print(val)