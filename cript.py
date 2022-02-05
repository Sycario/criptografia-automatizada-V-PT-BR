import hashlib

uname = input('palavra que sera criptografada:')
print('escolha uma das criptografias sha512, sha256, md5, sha1')
tipo = input('criptografia escolhida:')
if (tipo) == 'sha512':
    hash = hashlib.sha512(str( uname ).encode("utf-8") ).hexdigest()
    print (hash)
elif tipo == 'sha256':
    hash1  = hashlib.sha256(str( uname ).encode("utf-8") ).hexdigest()
    print(hash1)
elif tipo == 'md5':
    hash2  = hashlib.md5(str( uname ).encode("utf-8") ).hexdigest()
    print(hash2)
elif tipo == 'sha1':
    hash3  = hashlib.sha1(str( uname ).encode("utf-8") ).hexdigest()
    print(hash3)
else:
    print('tente novamente algo esta errado')
    exit()
print('sim para continuar, se nao quiser coloque nao')
quant = (input('vc quer repetir a criptografia == '))
if quant == 'nao':
    print('terminamos aqui obrigado por usar')
    print('==================================')
    print('made by Sycario')
    exit()
elif quant == 'sim':
    print('criptografia sha512 unica que foi construida ainda')
    cripto = input('escolha a criptografia == ')
    if cripto == 'sha512':
        print('Ok vamos la entao')
    else:
        print('vc colocou algum comando errado')
        exit()
    vezes = int(input('quantas vezes vc quer criptografar(3 é o maximo)? == ')) 
if vezes == 1:
        a = hashlib.sha512(str( hash ).encode("utf-8") ).hexdigest()
        print(a)
        print('TERMINAMOS POR AQUI!!!')
        print('made by Sycario')
elif vezes == 2:
    r = hashlib.sha512(str( hash ).encode("utf-8") ).hexdigest()
    e = hashlib.sha512(str( r ).encode("utf-8") ).hexdigest()
    print(r)
    print('============================================================================================================================')
    print(e)
    print('TERMINAMOS POR AQUI!!!')
    print('made by Sycario')
elif vezes == 3:
    f = hashlib.sha512(str( hash ).encode("utf-8") ).hexdigest()
    d = hashlib.sha512(str( f ).encode("utf-8") ).hexdigest()
    s = hashlib.sha512(str( d ).encode("utf-8") ).hexdigest()
    print(f)
    print('==============================================================================================================================')
    print(d)
    print('==============================================================================================================================')
    print(s)
    print('TERMINAMOS POR AQUI!!!')
    print('made by Sycario')
else:
    print('vc deve ter colocado algum comando errado')
    exit()
