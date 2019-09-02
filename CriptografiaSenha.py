import hashlib

def main():
    senha = input("Digite sua senha aqui: ")
    senha_encode = senha.encode('utf-8')
    resposta = input("Hash md5 ou sha256: ")
    if resposta == 'md5':
        hash_md5(senha_encode)
    elif resposta == 'sha256':
        hash_sha256(senha_encode)
    else:
        print('Digite md5 para gerar hash md5 ou sha256 para hash no formato sha256: \n\
Qualquer outro valor além desses não será aceito!')


def hash_md5(pwd):
    cripto = hashlib.md5()
    cripto.update(pwd)
    print(cripto.hexdigest())

def hash_sha256(pwd):
    cripto = hashlib.sha256()
    cripto.update(pwd)
    print(cripto.hexdigest())

if __name__ == "__main__":
    main()