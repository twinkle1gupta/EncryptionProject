import base64
import os

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

kdf_algo = hashes.SHA256()
kdf_len = 32
kdf_ite = 100000


"""
to store salt in file we need to connvert salt bytes to readable form i.e hexadecimal, or in any other encoding
so we are using hexadecimal method in this we will convert randomly generated bytes i.e salt to hex. by using `.hex()`
and make to sotore in files and to get back we will again covert hex to bytes by using `bytes.fromhex(<hex_string>)` 
"""

# Text encryption

def FILEIO(text_string,salt):

    data   = str(text_string.decode("ASCII"))
    salt_to_store = salt.hex()
    # print(salt_to_store)
    
    cwpath = os.getcwd() + "/Encrypted_files"

    file = os.path.join(cwpath,"en_file.txt")

    if os.path.isfile(file):
        
        file_name, extension = os.path.splitext(file)
        i = 1
        
        while os.path.exists(file):
            file = file_name + "("+ str(i) +")" + extension
            i = i + 1
        
        create_file = open(file,'w')
        create_file.write(f"{data}||{salt_to_store}")
        create_file.close()
        return file

    elif not os.path.isfile(file):

        create_file = open(file,'w')
        create_file.write(f"{data}||{salt_to_store}")
        create_file.close()
        return file
        
    else:
        print("Unexpected error!!")
        return None

def save_dec_text(dec_data):
    data   = str(dec_data)

    cwpath = os.getcwd() + "/Decrypted_files"

    file = os.path.join(cwpath,"dec_file.txt")

    if os.path.isfile(file):
        
        file_name, extension = os.path.splitext(file)
        i = 1
        
        while os.path.exists(file):
            file = file_name + "("+ str(i) +")" + extension
            i = i + 1
        
        create_file = open(file,'w')
        create_file.write(f"{data}")
        create_file.close()
        return file

    elif not os.path.isfile(file):

        create_file = open(file,'w')
        create_file.write(f"{data}")
        create_file.close()
        return file
        
    else:
        print("Unexpected error!!")
        return None

def FILEIO_DE(text_to_decrypt):
    data = text_to_decrypt
    req_data_list = data.split("||")
    enc_data = req_data_list[0]
    req_hex_salt = req_data_list[1]
    salt_bytes = bytes.fromhex(req_hex_salt)
    return enc_data, salt_bytes

    
def encrypt(msg, pswd):

    salt = os.urandom(16)
    kdf = PBKDF2HMAC(algorithm=kdf_algo,
                    length=kdf_len,
                    salt=salt,
                    iterations=kdf_ite)
    key = kdf.derive(pswd.encode("utf-8"))

    f = Fernet(base64.urlsafe_b64encode(key))
    encrypted_msg = f.encrypt(msg.encode("utf-8"))

    return bytes(encrypted_msg), bytes(salt)

def decrypt(encrypted_msg, msg, salt):

    kdf = PBKDF2HMAC(algorithm=kdf_algo,
                    length=kdf_len,
                    salt=salt,
                    iterations=kdf_ite)

    key = kdf.derive(msg.encode("utf-8"))

    f = Fernet(base64.urlsafe_b64encode(key))
    msg = f.decrypt(encrypted_msg)

    return str(msg.decode("utf-8"))

def main_enc(password,message):

    # get encrypted text and salt
    encrypted, salt = encrypt(message, password)
    # save encrypted text and salt to file in `Encrypted_files` folder
    filename = FILEIO(encrypted,salt)

    return filename,encrypted,salt


def main_dec(password,message):

    encrypted_data, salt  = FILEIO_DE(message)

    decrypted = decrypt(encrypted_data,password,salt)

    file_name = save_dec_text(decrypted)

    return file_name, decrypted



# file Encryption

class FileEncrypter():
    def __init__(self,path,password):
        super().__init__

        self.path = str(path)
        self.pswd = password

        self.file_name , self.file_extension = os.path.splitext(self.path)

    
    def check_ext(self):
        # if text based files
        if (self.file_extension  in ['.txt','.csv','.py','.md']):
            file_name = FileTypesText(self.path,self.pswd).rtrn()
            return file_name
        # image based file
        elif (self.file_extension in ['.png','.jpg','.jpeg']):
            file_name = FileTypeImage(self.path,self.pswd).rtrn()
            return file_name
        else:
            pass
        
class FileTypesText():
    def __init__(self,file_path,pswd):
        super().__init__

        self.FilePath = file_path
        with open(self.FilePath,'r') as file:
            file_data = file.read()
        
        encrypted , salt = encrypt(file_data,pswd)
        decrypted = decrypt(encrypted, pswd,salt)

        self.file_name = EncFileSaver(self.FilePath, encrypted, salt).CheckIfFileExists()

    def rtrn(self):

        return self.file_name

class FileTypeImage():
    def __init__(self,file_path,pswd):
        super().__init__
        self.FilePath = str(file_path)
        with open(self.FilePath,'rb') as file:
            file_data_in_bytes = base64.b64encode(file.read())
        file_data_in_string = file_data_in_bytes.decode("utf-8")
        encrypted , salt = encrypt(file_data_in_string,pswd)
        self.file_name = EncFileSaver(self.FilePath, encrypted, salt).CheckIfFileExists()
        self.rtrn()

    def rtrn(self):

        return self.file_name

class EncFileSaver():
    def __init__(self, file_path, file_data, salt):
        super().__init__

        self.file_extension = os.path.splitext(file_path)[1]
        self.data = file_data.decode("ASCII")
        self.cwpath = os.getcwd() + "/Encrypted_files"

        self.file = os.path.join(self.cwpath,f"en_file{self.file_extension}")
        self.salt_hex = salt.hex()
        # self.CheckIfFileExists()

    def CheckIfFileExists(self):

        if os.path.isfile(self.file):
        
            file_name, extension = os.path.splitext(self.file)
            i = 1
            
            while os.path.exists(self.file):
                self.file = file_name + "("+ str(i) +")" + extension
                i = i + 1
            
            create_file = open(self.file,'w')
            create_file.write(f"{self.data}||{self.salt_hex}")
            create_file.close()
            return self.file

        elif not os.path.isfile(self.file):

            create_file = open(self.file,'w')
            create_file.write(f"{self.data}||{self.salt_hex}")
            create_file.close()
            return self.file
            
        else:
            print("Unexpected error!!")
            return None


class FileDecryptor():
    def __init__(self, file_path,pswd):
        super().__init__
        
        self.FilePath = str(file_path)
        self.pswd = pswd

        self.file_name, self.file_extension = os.path.splitext(self.FilePath)
        # self.check_ext()

    def check_ext(self):

        if (self.file_extension  in ['.txt','.csv','.py','.md']):
            file_name = DecryptTextFile(self.FilePath,self.pswd).rtrn()
            return file_name
        # image based file
        elif (self.file_extension in ['.png','.jpg','.jpeg']):
            file_name = DecryptImageFile(self.FilePath,self.pswd).rtrn()
            return file_name
        else:
            pass


class DecryptTextFile():
    def __init__(self, file_path,pswd):
        super().__init__

        self.FilePath = file_path

        self.extension = os.path.splitext(self.FilePath)[1]

        with open(self.FilePath,'r') as file:
            file_data = file.read()

        data = file_data
        req_data_list = data.split("||")
        enc_data = req_data_list[0]
        req_hex_salt = req_data_list[1]
        salt_bytes = bytes.fromhex(req_hex_salt)

        self.EncryptedData = enc_data
        self.SaltBytes = salt_bytes

        decrypted_data = decrypt(self.EncryptedData, pswd, self.SaltBytes)
        

        self.file_name = DecryptFileSaver(decrypted_data, self.extension).checkFile()

    def rtrn(self):
        return self.file_name


class DecryptImageFile():
    def __init__(self,file_path,pswd):
        super().__init__

        self.FilePath = file_path
        self.extension = os.path.splitext(self.FilePath)[1]

        with open(self.FilePath,'r') as file:
            file_data = file.read()

        data = file_data
        req_data_list = data.split("||")
        enc_data = req_data_list[0]
        req_hex_salt = req_data_list[1]
       
        salt_bytes = bytes.fromhex(req_hex_salt)
        
        self.SaltBytes = salt_bytes
        self.enc_data_hex = enc_data

        decrypted_data = decrypt(self.enc_data_hex,pswd,self.SaltBytes)

        self.req_data_bytes = base64.b64decode(decrypted_data.encode("utf-8"))

        self.file_name = DecryptFileSaver(self.req_data_bytes,self.extension).checkFile()

    def rtrn(self):

        return self.file_name
    

class DecryptFileSaver():
    def __init__(self,decrypted_data,extension):
        super().__init__

        self.data   = decrypted_data

        cwpath = os.getcwd() + "/Decrypted_files"

        self.file = os.path.join(cwpath,f"dec_file{extension}")
        # self.checkFile()

    def checkFile(self):

        if os.path.isfile(self.file):
            
            file_name, extension = os.path.splitext(self.file)
            i = 1
            
            while os.path.exists(self.file):
                self.file = file_name + "("+ str(i) +")" + extension
                i = i + 1
            
            create_file = open(self.file,'w')
            create_file.write(self.data)
            create_file.close()
            return self.file

        elif not os.path.isfile(self.file):

            create_file = open(self.file,'w')
            create_file.write(self.data)
            create_file.close()
            return self.file
            
        else:
            print("Unexpected error!!")
            return None




        

# FileTypeImage("/home/kaushik/Desktop/Encryption-project/test_exts/test.png")
        

# print(FileEncrypter("/home/kaushik/Desktop/Encryption-project/test_exts/test.png")) 

# DecryptImageFile("/home/kaushik/Desktop/Encryption-project/Encrypted_files/en_file.png")
