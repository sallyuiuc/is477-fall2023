import os
import requests
import hashlib

# URLs for the datasets
adult_data_url=  "https://archive.ics.uci.edu/static/public/2/adult.zip"
reconstruct_data_url = "https://raw.githubusercontent.com/socialfoundations/folktables/main/adult_reconstruction.csv"

# Check the File paths for downloaded data and files
path="data/folktables"
isExist=os.path.exists(path)
if not isExist:
# Create a new directory if the answer is no
    os.makedirs(path)
response_adult=requests.get(adult_data_url)

with open('data/adult.zip', mode='wb') as f:
    f.write(response_adult.content)
filename1='data/adult.zip'
with open(filename1,mode='rb') as f:
    data=f.read()
    sha256hash=hashlib.sha256(data).hexdigest()
uci_adult_sha256='7537312dd56c2b98035880805ce99e68183a30ee468aa5329d6df0fbb3cc21bb'
if uci_adult_sha256!=sha256hash:
    print("not matched")
else:
    print("matched")
    
# Reconstruced data set
reconstruct_data_url = "https://raw.githubusercontent.com/socialfoundations/folktables/main/adult_reconstruction.csv"
response_reconstruct= requests.get(reconstruct_data_url)
with open('data/folktables/adult_reconstruction.csv',mode='wb') as f:
    f.write(response_reconstruct.content)
filename2='data/folktables/adult_reconstruction.csv'
with open(filename2,mode='rb') as f:
    data2 = f.read()
    sha256hash2=hashlib.sha256(data2).hexdigest()
reconstruct_sha256='4895fd481e7ae6e2ca423e6213454b39f0f7ec0efcd741ad2f6c667554f0eb51'
if reconstruct_sha256!=sha256hash2:
    print("not matched")
else:
    print("matched")