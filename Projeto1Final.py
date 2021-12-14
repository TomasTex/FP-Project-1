"""
Fundamentos da Programação - Projeto 1
Tomás Teixeira, nº104165
3/11/2021
contacto: tomasteixeira5@gmail.com




breve explicação sobre o que faz cada função

    Args:
        'nome' (tipo do argumento)
                
    Returns:
        (tipo do ): todas as vogais na senha
"""     


#               1 Correção da documentação

# 1.2.1
def corrigir_palavra(caracteres: str) -> str:  # falta comentar 
    """[summary]

    Args:
        caracteres (str): [description]

    Returns:
        str: [description]
    """
    #esta func é recursuva 
    delta_maiuscula_minuscula = ord('a') - ord('A')
    len_caracteres = len(caracteres)
 
    if len_caracteres < 2: #condição de paragem
        return caracteres
 
    char1 = caracteres[0]
    char2 = caracteres[1]
 
    delta_char1_char2 = ord(char1) - ord(char2)
 
    if abs(delta_char1_char2) == delta_maiuscula_minuscula:
        caracteres = corrigir_palavra(caracteres[2:])
    else:
        caracteres = caracteres[0] + corrigir_palavra(caracteres[1:])
 
    if len(caracteres) != len_caracteres:
        caracteres = corrigir_palavra(caracteres)
 
    return caracteres

#1.2.2
def obter_dicionario_de_chars(palavra: str) -> dict:

    """ vai criar um dicionario inde se pode ver o nº de ocorrencias de uma letra.

    Args:
        palavra (str): [palavra dada]

    Returns:
        dict: [dicionario com as ocorrencias]
    """
    dicionario = {}
 
    for caracter in palavra.lower(): #não é case-sensitive
        dicionario[caracter] = dicionario.setdefault(caracter, 0) + 1
 
    return dicionario
 
 
def eh_anagrama(palavra1: str, palavra2: str) -> bool:

    """ recebe 2 palavras e vê se são anagramas.

    Args:
        palavra1 (str)
        palavra2 (str)

    Returns:
        bool: [é anagrama?]
    """

    if len(palavra1) == 0:
        return False
    if palavra1.lower()==palavra2.lower():
        return False
    dicionario_palavra1 = obter_dicionario_de_chars(palavra1)
    dicionario_palavra2 = obter_dicionario_de_chars(palavra2)
 
    return dicionario_palavra1 == dicionario_palavra2 

#1.2.3
def corrigir_doc (doc):   

    """ recebe texto com erros e filtra-os, juntamente com os anagramas.

    Args:
        doc (str)

    Returns:
        str: [texto arranjado]
    """
    if not isinstance(doc, str):
        raise ValueError('corrigir_doc: argumento invalido')
    listaPalavras = doc.split(' ')
    
    listaCorrigida = []
    for i in listaPalavras:
        if not i.isalpha():
            raise ValueError('corrigir_doc: argumento invalido')            
        palavraCorrigida = corrigir_palavra(i)
        listaCorrigida.append(palavraCorrigida)

    for p1 in range(len(listaCorrigida)-1):
        for p2 in range(p1+1, len(listaCorrigida)):
            temAnagrama= eh_anagrama(listaCorrigida[p1], listaCorrigida[p2])
            if temAnagrama:                                
                listaCorrigida[p2]=''
    
    for i in reversed(range(len(listaCorrigida))):
        if listaCorrigida[i] == '':
            del listaCorrigida[i]

    listaCorrigida= " ".join(listaCorrigida)
    return listaCorrigida.replace('  ', ' ')


#               2 Descoberta do PIN  

#  2.2.1 
def obter_posicao(mov:str, pos:int) -> int:

    """ recebendo uma direcao e uma posicao inicial, devolve a posicao final.

        Args:
            mov (str): [direcao para onde anda]
            por (int): [posicao inicial]

        Returns:
            int: [posicao final]
        """    

    if mov == 'C':
        if pos == 1 or pos== 2 or pos == 3:
            return pos
        else:
            pos= pos-3
            return pos
        
        
    if mov == 'B':
        if pos == 7 or pos== 8 or pos== 9:
            return pos   
        else:
            pos= pos+3
            return pos
        
        
    if mov == 'E':
        if pos == 1 or pos== 4 or pos== 7:
            return pos 
        else:
            pos= pos-1
            return pos
        
    if mov == 'D':
        if pos == 3 or pos== 6 or pos== 9: 
            return pos
        else:
            pos=pos+1
            return pos

# 2.2.2
def obter_digito(mov:str, pos:int) -> int: 

    """ recebendo uma sequencia de direcoes e uma posicao inicial, devolve a posicao final.

        Args:
            mov (str): [ sequencia de direcoes para onde anda]
            pos (int): [posicao inicial]

        Returns:
            int: [posicao final]
        """    

    seq=[]          #seq(uencia) será a minha list que vou percorrer                 
    seq[:0]=mov     #transforma a string numa list               
    for i in range(len(seq)):
        if seq[i] == 'C':
            if pos not in {1, 2, 3}:
                pos=pos-3
                
            
            
        if seq[i] == 'B':
            if pos not in {7, 8, 9}:
                pos= pos+3
            
                            
        if seq[i] == 'E':
            if pos not in{1, 4, 7}:
                pos= pos-1
            
                        
        if seq[i] == 'D':
            if pos not in {3, 6, 9}: 
                pos= pos+1
    return pos

#2.2.3
def obter_pin(tup: tuple) -> tuple: 

    """ recebendo um tuplo c\ sequencias de direcoes e uma posicao inicial, devolve a posicao final.

        Args:
            tup (tuple): [sequencias de direcoes para onde anda]

        Returns:
            tuple: [pin]
        """    
    if not isinstance(tup, tuple):
        raise ValueError('obter_pin: argumento invalido')
    if not len(tup):
        raise ValueError('obter_pin: argumento invalido')
    if len(tup)<4 or len(tup)>10:
        raise ValueError('obter_pin: argumento invalido')
    pos=5
    for i in tup:
        if  i=='':
            raise ValueError('obter_pin: argumento invalido')
        for j in i:
            if j not in ('C','B', 'D', 'E'):
                raise ValueError('obter_pin: argumento invalido')

    digitos = []

    for i in range(len(tup)):
        pos = obter_digito(tup[i],pos)
        digitos.append(pos)
    return tuple(digitos)


#               3 Verificação de Dados

# 3.2.1
# auxiliares(parse_... )
def parse_cifra(cifra) -> list:
   return  cifra.split('-')
    
def parse_checksum(checksum):
   return checksum[1:-1]

def eh_entrada(arg):

    """ recebe um argumento de qualquer tipo e devolve True se e só se o seu argumento corresponde a uma entrada da BDB.

    Args:
        arg (any): [argumento de qualquer tipo]

    Returns:
        [bool]: [é uma entrada da BDB?]
    """

    if not isinstance(arg, tuple):
        return False
    if len(arg)!=3:
        return False

    cifra, controlo, codigo = arg

    if not isinstance(controlo, str):
        return False

    if len(controlo) != 7:
        return False

    if '[' != controlo[0] or ']' != controlo[-1]:
        return False
    
    if not isinstance(cifra,str) or len(cifra)<2:
        return False
    
    cifra = parse_cifra(cifra)
    controlo= parse_checksum(controlo)

    if not controlo.islower() or not controlo.isalpha():
        return False

    if not isinstance(codigo, tuple):
        return False

    if len(codigo)<2:
        return False
    for i in codigo:
        if not isinstance(i, int) or i<=0:
            return False
    for parte_cifra in cifra:
        if not isinstance(parte_cifra, str):
            return False
        for i in parte_cifra:
            if i != '-' and (i < 'a' or i > 'z'):
                return False     

    return True

# 3.2.2
#auxiliar(caracteres_mais_comuns)
def caracteres_mais_comuns(count_per_chars):
    
    """ Vai verificar quais os caracteres mais comuns e retornar uma lista com eles ordenados.

    Args:
        count_per_chars ([dict])

    Returns:
        [list]: [caracteres ordenados por vezes que aparecem]
    """

    def funcao_sort(tuplo): #recebe um tuplo e devolve o contador desse caracter
        return tuplo[1] 

    ordered = sorted(count_per_chars.items(), key= funcao_sort, reverse=True ) #ordenar criando uma lista de tuples que são (chave, valor)
    return ordered[0:5]

#def validar_cifra(cifra: str, controlo: str) -> bool: 
   
    """ recebe uma cifra e uma seq de controlo e devolve True se forem coerentes.

    Args:
        cifra (str)
        controlo (str)

    Returns:
        [bool]: [os Args são coerentes?]
    """     
    
    # cifra= parse_cifra(cifra)
    # controlo= parse_checksum(controlo)
    # if len(controlo)!= 5:
    #     return False
    # count_per_chars = {}
    # for part_cifra in cifra:
    #     for caracter in part_cifra:
    #         count_per_chars[caracter]= count_per_chars.setdefault(caracter,0)+1

    # maisComuns= caracteres_mais_comuns(count_per_chars)
    # a= sorted(map(lambda tuplo_caracter_contador: tuplo_caracter_contador[0], maisComuns)) 
    # # map recebe func. mapeamento ((lambda é uma func anonima toda feita na horizontal), coleção a transformar(maisComuns))
    # a = ''.join(a)
    # return a== controlo
def validar_cifra(cifra: str, sequencia_controlo: str) -> bool:
    dicionario = obter_dicionario_de_chars(cifra)
    dicionario.pop('-', False)
    
    chars_count = list(dicionario.items())
    len_chars_count = len(chars_count)
 
    # bubble sort: https://realpython.com/sorting-algorithms-python/#the-bubble-sort-algorithm-in-python
    for i in range(len_chars_count):
        ordenado = True
 
        for j in range(len_chars_count - i - 1):
            char1, count_char1 = chars_count[j]
            char2, count_char2 = chars_count[j + 1]
 
            if count_char2 > count_char1 or (count_char1 == count_char2 and char1 > char2):
                chars_count[j], chars_count[j + 1] = chars_count[j + 1], chars_count[j]
                ordenado = False
 
        if ordenado:
            break
 
    chars = ''
    for entry in chars_count[:5]:
        chars += entry[0]
 
    return '[' + chars + ']' == sequencia_controlo
       

# 3.2.3
def filtrar_bdb(lista: list) -> list:

    """ recebe uma lista com entradas BDB e retorna as não coerentes.

    Args:
        lista (list)
        
    Returns:
        [list]: [lista com os casos não coerentes]
    """     
    if not isinstance(lista, list):
        raise ValueError('filtrar_bdb: argumento invalido')
    if not len(lista):
        raise ValueError('filtrar_bdb: argumento invalido')

    listaNaoCoerente=[]

    for tuplo in lista:
        if not isinstance(tuplo, tuple) or len(tuplo)!= 3:
            raise ValueError('filtrar_bdb: argumento invalido')
        if not eh_entrada(tuplo):
            listaNaoCoerente.append(tuplo)
            continue
        senha, controlo, codigo = tuplo
        if not validar_cifra(senha, controlo):
            listaNaoCoerente.append(tuplo)
    return listaNaoCoerente

#               4 Desencriptação de Dados

# 4.2.1 (igual à 3.2.1)

#4.2.2
def obter_num_seguranca(codigos: tuple) -> int:

    """ recebe um tuplo com numeros e devolve o numero de seguranca.

    Args:
        codigos (tuple)
        
    Returns:
        [int]: [numero de seguranca]
    """     

    minimo_absoulto = float('inf')  # começa a infinito pois assim tenho a certeza que nenhum será maior

    len_codigos = len(codigos)

    for i in range(len_codigos):
        for j in range(i + 1, len_codigos):
            num1 = codigos[i]
            num2 = codigos[j]

            minimo_local = abs(num1 - num2) # faço o módulo pois quero que seja sempre um nº positivo

            if minimo_local < minimo_absoulto:
                minimo_absoulto = minimo_local # cada vez que há uma 'diferença' mais pequena, essa passa a ser a que guardamos

    return minimo_absoulto

# 4.2.3
def decifrar_texto(cifra: str, nSeguranca: int) -> str: 

     """ recebe uma cifra e um número de segurança, e devolve o texto decifrado.

    Args:
        cifra (str)
        nSeguranca (int)
        
    Returns:
        [str]: [texto decifrado]
    """     
  
     texto=''
     
     for i in range(len(cifra)):
        _char = cifra[i]
        if _char == '-':
            texto+= ' '
            continue
        Ascii=ord(_char)
        quantasMuda= nSeguranca % 26 

        if i%2==0:
            if (Ascii + quantasMuda + 1)<= 122: # se o ascii + x + 1 for mais pequeno que o ascii do z- 122
                Ascii= Ascii + quantasMuda + 1
            else:
                sobra= (Ascii + quantasMuda + 1)-122
                Ascii = 96 + sobra #tem de começar no 96 porque se não, excluimos o A->97
            
        else:
            if (Ascii + quantasMuda - 1)<= 122: # se o ascii + x + 1 for mais pequeno que o ascii do z- 122
                    Ascii= Ascii + quantasMuda - 1
            else:
                sobra= (Ascii + quantasMuda - 1)-122
                Ascii = 96 + sobra #tem de começar no 96 porque se não, excluimos o A->97
        texto+= chr(Ascii)

     return texto

# 4.2.4
def decifrar_bdb(listaEntradas: list) -> list:

    """ recebe lista com entradas da BDB, e devolve uma lista com o texto decifrado pela mesma ordem.

    Args:
        listaEntradas (str)
                
    Returns:
        [list]: [lista c\ texto decifrado]
    """     

    if not isinstance(listaEntradas, list):
        raise ValueError('decifrar_bdb: argumento invalido')
    if len(listaEntradas)==0:
        raise ValueError('decifrar_bdb: argumento invalido')
    for entrada in listaEntradas:
        if not isinstance(entrada, tuple) or len(entrada)!=3:
            raise ValueError('decifrar_bdb: argumento invalido')

    listaDecifrada=[]

    for entrada in listaEntradas:
        cifra, _ , codigo = entrada    #a variavel _ não será usada, daí o nome
        decifrada= decifrar_texto(cifra, obter_num_seguranca(codigo) )
        listaDecifrada.append(decifrada)
    return listaDecifrada

#               5 Depuração de Senhas

#5.2.1
def eh_utilizador(arg) -> bool:

    """ recebe um argumento de qualquer tipo e devolve True apenas se o seu argumento é um dicionário c\ informação relevante.

    Args:
        arg (any)
                
    Returns:
        [bool]: [é um dicionário c\ informação relevante?]
    """     

    if not isinstance(arg, dict):
        return False
    if len(arg)!=3:
        return False
    if 'name' not in arg or 'pass' not in arg or 'rule' not in arg:
        return False
    name= arg['name']
    passe=arg['pass']
    rule= arg['rule']
    if not isinstance(rule, dict):
        return False
    if not isinstance(name, str):
        return False
    if not isinstance(passe, str):
        return False
    if 'vals' not in rule or 'char' not in rule:
        return False
    vals= rule['vals']
    char= rule['char']
    if not isinstance(vals, tuple) or not isinstance(char, str):
        return False
    if len(char)!=1:
        return False
    if len(vals)<2:
        return False
    for val in vals:
        if not isinstance(val, int):
            return False
        if val<0:
            return False
    if vals[0]>vals[1]:
        return False
    if arg['name'] == '' or arg['pass'] =='' :
        return False
    
    return True

# 5.2.2
#auxiliar(get_vogais)
def getVogais(senha:str) -> list:

    """ recebe uma senha e devolve uma lista c\ as vogais que encontrou.

    Args:
        senha (str)
                
    Returns:
        [list]: [todas as vogais na senha]
    """     

    letras_vogais = []
    lista_vogais = ['a', 'e', 'i', 'o', 'u']

    for letra in senha:
        if letra in lista_vogais:
            letras_vogais.append(letra)

    return letras_vogais

def eh_senha_valida(senha: str,dictRegras: dict) -> bool:  

    """ recebe uma senha e um dict com a regra individual, e devolve True se a senha cumprir as regras indiv. e gerais.

    Args:
        senha (str)
        dictRegras (dict)
                
    Returns:
        [list]: [todas as vogais na senha]
    """     

    # regras gerais
    consecutiva=False
    for i in range(len(senha)-1):
        if senha[i]== senha[i+1]:
            consecutiva=True
    if not consecutiva:
        return False
    if len(getVogais(senha))<3:
        return False  
    #regras privadas 
    char_value= dictRegras.get('char', False) #em vez de rebentar devolve false
    if not char_value:
        return False
    vals_value= dictRegras.get('vals', False)
    if not vals_value:
        return False

    minimo, maximo = vals_value
           
    contagem=senha.count(char_value) 
    if not contagem: 
        return False
    if contagem< minimo or contagem> maximo:
        return False
    return True


# 5.2.3
def filtrar_senhas(bdb: list) -> list:

    """ recebe a lista que contém um ou mais dicionários correspondentes às entradas da BDB e apenas devolve os c\ senhas erradas.

    Args:
        senha (str)
        dictRegras (dict)
                
    Returns:
        list: todas as vogais na senha
    """     
    
    if not isinstance(bdb, list):
        raise ValueError('filtrar_senhas: argumento invalido')
    if len(bdb)==0:
        raise ValueError('filtrar_senhas: argumento invalido')
    
    listaErradas=[]

    for sequencia in bdb: 
        if not isinstance(sequencia, dict):
            raise ValueError ('filtrar_senhas: argumento invalido')
        if 'name' not in sequencia or 'pass' not in sequencia or  'rule' not in sequencia:

            raise ValueError('filtrar_senhas: argumento invalido')
        nome=sequencia['name']
        senha=sequencia['pass']
        regras=sequencia['rule']

        

        if not eh_senha_valida(senha, regras):
            listaErradas.append(nome)
        listaErradas.sort()
        
    return listaErradas


    

