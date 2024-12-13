import os
import pyaes

# Recebe o arquivo encriptado
print( "Informe o caminho do arquivo a ser descriptografado: ")
file_path = str(input())

# Abre o arquivo encriptado
file = open(file_path, "rb")
file_data = file.read()
file.close()

# Recebe a chave de descriptografia 
print("Informe a chave de descriptografia (16 bytes): ")
keyText = str(input())
key = keyText.encode()
aes = pyaes.AESModeOfOperationCTR(key)

# Descriptografa o arquivo
decrypt_data = aes.decrypt(file_data)

# Salva os dados descriptografados no arquivo sem a extensão .encrypted
decrypt_file = file_path.replace(".encrypted", "") 
decrypt_file = open(decrypt_file, "wb")
decrypt_file.write(decrypt_data)
decrypt_file.close()

#Remove o arquivo encriptado
os.remove(file_path)
