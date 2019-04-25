from terminaltables import AsciiTable
d = {}

def menu():
    print('Listagem de Disciplinas')
    print('''
    Digite:
    [1] para cadastrar disciplina.
    [2] para localizar disciplina.
    [3] para alterar valores da disciplina.
    [4] para excluir disciplina.
    [5] para listar todas as disciplinas.
    [6] para sair.
        ''')
    pass

def cadastrar():
    print('Opção cadastrar.')
    codigo = input('Digite o código: ')
    if codigo in d.keys():
        print('Código informado já cadastrado.\nRetornando ao menu.\n')

    elif codigo not in d.keys(): #tentei com o else mas ele não estava funcionando.
        nome = str(input('Digite o nome:'))
        ch = int(input('Digite o CH:'))
        nota = float(input('Digite a nota:'))
        d[codigo] = [nome, ch, nota] # essa linha cria uma key do dicionario e o valor é construido como lista, pois assim posso saber em qual lugar da lista está o valor que desejo.

        print('Disciplina cadastrada com sucesso!\n')
        table_data = [
            ['Código', 'Nome da disciplina','CH','Nota'],
            [codigo, d[codigo][0], d[codigo][1], d[codigo][2]],
            ]
        table = AsciiTable(table_data)
        print (table.table)

    pass

def localizar():
    print('Opção localizar.')
    codigo = input('Digite o codigo da disciplina que desejas localizar: ')
    if codigo in d.keys():
        table_data = [
            ['Código', 'Nome da disciplina','CH','Nota'],
            [codigo, d[codigo][0], d[codigo][1], d[codigo][2]],
        ]
        table = AsciiTable(table_data)
        print (table.table)
    else:
        print('Código não listado.')
    pass

def alterar():
    print('Opção alterar.')
    codigo = input('Digite o codigo da disciplina que desejas alterar: ')
    if codigo in d.keys():
        while True:
            try:
                letra = str(input('Digite o que desejas alterar:\n [A] Nome da disciplina \n [B] CH da disciplina \n [C] Nota da disciplina \n [D] Codigo da disciplina \n [X] Sair da alteração \n:'))
                if letra.upper() == 'A':
                    print('Modificar o nome da disciplina.')
                    nome = str(input('Novo nome:'))
                    d[codigo][0] = nome
                    print('Nome modificado com sucesso!\n')
                    pass

                elif letra.upper() == 'B':
                    print('Modificar o CH da disciplina.')
                    ch = int(input('Novo CH:'))
                    d[codigo][1] = ch
                    print('CH modificado com sucesso!\n')
                    pass

                elif letra.upper() == 'C':
                    print('Modificar a nota da disciplina.')
                    nova_nota = float(input('Nova nota:'))
                    d[codigo][2] = nova_nota
                    print('Nota modificada com sucesso!\n')
                    pass

                elif letra.upper() == 'D':
                    print('Modificar o Código da disciplina.')
                    novo_codigo = int(input('Novo código:'))
                    d[novo_codigo] = d[codigo] #essa linha cria uma key igual a do usuario deseja alterar
                    del d[codigo] #aqui a chave com o codigo não desejado é excluido, sobrando a key nova com os mesmos valores
                    print('Código modificado com sucesso!\n')
                    pass

                elif letra.upper() == 'X':
                    if codigo in d.keys():
                        table_data = [
                            ['Código', 'Nome da disciplina','CH','Nota'],
                            [codigo, d[codigo][0], d[codigo][1], d[codigo][2]],
                        ]
                        table = AsciiTable(table_data)
                        print(table.table) #mostra o codigo modificado antes de sair, evitando ter que localizar posteriormente.
                        pass
                    else:
                        lst = list(d.items())
                        x = lst[-1][0] # como tinha a possibilidade do usuário ter modificado o código antes de sair, se o codigo estivesse mudado, a condição iria furar. E como sempre que se adiciona uma chave no dicionario, ela vai para o final do dicionario, só tive q construir uma lista do dicionario e localizar o último termo.
                        if x in d.keys():
                            table_data = [
                                ['Código', 'Nome da disciplina','CH','Nota'],
                                [x, d[x][0], d[x][1], d[x][2]],
                            ]
                            table = AsciiTable(table_data)
                            print(table.table)
                            pass
                        pass
                    print('Opção escolhida: Sair da alteração.\n')
                    break

                else:
                    print('Digite uma opção válida.')
                pass

            except:
                if KeyboardInterrupt: #digite ctrl + c para parar o loop / ou poderia simplismente digitar X.
                    break
                else:
                    print('Digite uma opção válida.')
                    pass
    else:
        print('Código não listado.')


def excluir():
    codigo = input('Digite o codigo da disciplina que desejas localizar: ')
    if codigo in d.keys():
        table_data = [
            ['Código', 'Nome da disciplina','CH','Nota'],
            [codigo, d[codigo][0], d[codigo][1], d[codigo][2]],
        ]
        table = AsciiTable(table_data)
        print(table.table) #mostra qual código/disciplina será excluído
        del d[codigo]
        print('Disciplina excluida.\n')
        pass

    else:
        print('Código não listado.')
        pass
    pass

def listar():
    if len(d) > 0:
        lst = list(d.keys())
        y = 0
        x = len(lst) -1
        ch = 0
        nota = 0
        table_data = [['Código', 'Nome da disciplina','CH','Nota']]
        while y <= x:
            z = lst[y]
            table_data.append([lst[y], d[z][0], d[z][1], d[z][2]])
            ch = ch + d[z][1]
            nota = nota + d[z][2]
            y += 1
            pass
        table_data.append(['------------------------','-','---','----'])
        table_data.append(['Total / Média das notas:',len(d), ch, nota/(x+1)])
        table = AsciiTable(table_data)
        print(table.table)
        pass

    else:
        print('Não há disciplinas a se listar.')
        pass
    pass

while True:
    try:
        menu()
        op = input('Opção:\t')
        if op == 1:
            cadastrar()
            pass

        elif op == 2:
            localizar()
            pass

        elif op == 3:
            alterar()
            pass

        elif op == 4:
            excluir()
            pass

        elif op == 5:
            listar()
            pass

        elif op == 6:
            print('Opção escolhida: Sair')
            break

    except:
        if KeyboardInterrupt: #digite ctrl + c para parar o loop / ou poderia simplismente digitar 6.
            break
        else:
            print('Digite uma opção válida.')
            pass
    pass
