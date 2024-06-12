import sys
sys.path.insert(0, "/content/repo/python")
from scs_crypt.crypt import encrypt_string_user_pass, decrypt_string_user_pass

if sys.argv[1] == "en":
  res = encrypt_string_user_pass(sys.argv[2])
  print (res)
if sys.argv[1] == "dec":
  res = decrypt_string_user_pass(sys.argv[2])  
  print (res)

# try:
# pass 1234
# !python /content/repo/python/scs_crypt/test_arg.py dec gAAAAABmagFD_4YvxuN80aRJOgXJ3okcRUZz7sOU5wTnEUPbyMuKINLsqhj6wobgvavbNDBX-qBG82HhoBF0Wi9SfGgyGTykyRiX_dxyM_5eNU1LzkuyReg= 