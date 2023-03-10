"""
Arquivo responsável por descriptografar um arquivo e converter seu
conteúdo para um DataFrame do pandas.
"""

from io import BytesIO

from Crypto.Cipher import AES
import pandas as pd

# Tenta obter os dados utilizados na descriptografia
try:
    # Obtém a chave a partir do arquivo "key.bin"
    with open("key.bin", "rb") as file:
        key = file.read()

    # Obtém o nonce, a tag e o texto criptografado do arquivo "encrypted_data.bin"
    with open("encrypted_data.bin", "rb") as file:
        # Obtém o nonce do arquivo
        nonce = file.read(16)

        # Obtém a tag do arquivo
        tag = file.read(16)

        # Obtém o texto criptografado
        cipherText = file.read()
# Se pelo menos um dos arquivos não for encontrado, escreve no terminal uma mensagem de erro
except FileNotFoundError:
    print("Não foi possível encontrar os arquivos para realizar a descriptografia")
# Senão, se os dados utilizados na descriptografia forem obtidos, realiza a descriptografia
else:
    # Instancia o objeto responsável pela descriptografia
    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # Tenta descriptografar o texto criptografado
    try:
        # Descriptografa o texto criptografado
        decryptedData = cipher.decrypt_and_verify(cipherText, tag)
    # Se a chave estiver errada ou o conteúdo do arquivo estiver corrompido, escreve no terminal uma mensagem de erro
    except ValueError:
        print("A chave está errada ou o conteúdo do arquivo está corrompido")
    # Senão, se a criptografia for bem-sucedida, converte o texto descriptografado para o formato de DataFrame
    else:
        # Converte o texto descriptografado para o formato de DataFrame
        originalData = pd.read_csv(BytesIO(decryptedData))

        # Escreve no terminal o DataFrame
        print("Dados Descriptografados:\n")
        print(originalData)
