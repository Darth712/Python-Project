# ----------------------------------------------2.1.1-----------------------------------------------#
#                                         TAD intersecao                                           #


# Construtores
def cria_intersecao(col, lin):
    """
    Esta função recebe uma coluna e uma linha e
    cria uma interseção, um tuplo neste caso

    Args:
        col (str): coluna da interseção
        lin (int): linha da interseção

    Raises:
        ValueError: caso os parâmetros não estejam dentro do goban

    Returns:
        tuplo: coordenadas da interseção
    """
    if not (
        isinstance(col, str)
        and len(col) == 1
        and "A" <= col <= "S"
        and isinstance(lin, int)
        and 1 <= lin <= 19
        and isinstance(col, bool) is False
        and isinstance(lin, bool) is False
    ):
        raise ValueError("cria_intersecao: argumentos invalidos")
    return (col, lin)


# Seletores
def obtem_col(i):
    """
    Esta função recebe interseção
    e recebe a sua coluna

    Args:
        i (tuplo): interseção

    Returns:
        int: linha da interseção

    """
    return i[0]


def obtem_lin(i):
    """
    Esta função recebe interseção
    e recebe a sua linha

    Args:
        i (tuplo): interseção

    Returns:
        int: linha da interseção

    """ """"""
    return i[1]


# Reconhecedores
def eh_intersecao(i):
    """
    Esta função recebe um argumento e devolve
    um bool se é uma interseção ou não

    Args:
        i (any): Qualquer coisa

    Returns:
        bool: "True" caso seja uma interseção
        "False" caso contrário

    """
    return (
        isinstance(i, tuple)
        and len(i) == 2
        and isinstance(obtem_col(i), str)
        and len(obtem_col(i)) == 1
        and "A" <= obtem_col(i) <= "S"
        and isinstance(obtem_lin(i), int)
        and 1 <= obtem_lin(i) <= 19
    )


def eh_str(s):
    """
    Esta função recebe um argumento e
    devolve se é uma interseção ou não

    Args:
        s (any): Qualquer coisa

    Returns:
        bool: "True" caso seja uma interseção
        "False" caso contrário
    """
    if len(s) == 2:
        return "A" <= s[0] <= "S" and 1 <= int(s[1]) <= 9
    elif len(s) == 3:
        return "A" <= s[0] <= "S" and s[1] == "1" and 0 <= int(s[2]) <= 9


# Testes
def intersecoes_iguais(i1, i2):
    """
    Esta função recebe duas interseções
    e devolve um bool

    Args:
        i1 (tuplo): interseção
        i2 (tuplo): interseção

    Raises:
        ValueError: caso as interseções não forem interseções

    Returns:
        bool: "True" caso os argumentos forem iguais
        "False" caso contrário
    """
    if not (eh_intersecao(i1) and eh_intersecao(i2)):
        raise ValueError("intersecoes_iguais: argumentos invalidos")
    if obtem_col(i1) == obtem_col(i2) and obtem_lin(i1) == obtem_lin(i2):
        return True
    return False


# Transformadores
def intersecao_para_str(i):
    """
    Esta função recebe uma interseção
    e devolve a mesma interseção na
    forma de string

    Args:
        i (tuplo): interseção

    Raises:
        ValueError: caso a interseção não seja uma interseção

    Returns:
        str: string da interseção
    """
    if not eh_intersecao(i):
        raise ValueError("intersecao_para_str: argumento invalido")
    return obtem_col(i) + str(obtem_lin(i))


def str_para_intersecao(s):
    """
    Esta função recebe uma interseção
    e devolve a mesma interseção em
    forma de tuplo

    Args:
        s (str): string da interseção

    Returns:
        tuplo: interseção
    """
    if len(s) == 2:
        return (s[0], int(s[1]))
    elif len(s) == 3:
        return (s[0], int(s[1] + s[2]))


# Funções de alto nível
def obtem_intersecoes_adjacentes(i, l):
    """
    Esta função recebe duas interseções,
    uma onde devolve as interseções
    adjacentes desta, e outra para
    limitar o goban

    Args:
        i (tuplo): interseção
        l (tuplo): ultima interseção do goban

    Raises:
        ValueError: caso os argumentos não sejam interseções

    Returns:
        tuplo: tuplo contendo as interseções adjacentes de i
    """
    if not (eh_intersecao(i) and eh_intersecao(l)):
        raise ValueError("obtem_intesecoes_adjacentes: argumentos invalidos")

    res = [
        (chr(ord(obtem_col(i)) + 1), obtem_lin(i)),
        (chr(ord(obtem_col(i)) - 1), obtem_lin(i)),
        (obtem_col(i), obtem_lin(i) + 1),
        (obtem_col(i), obtem_lin(i) - 1),
    ]
    j = 0
    while j < len(res):
        if (
            obtem_col(res[j]) > obtem_col(l)
            or obtem_lin(res[j]) > obtem_lin(l)
            or not eh_intersecao(res[j])
        ):
            del res[j]
        else:
            j += 1
    return tuple(ordena_intersecoes(res))


def compara(x):
    return obtem_lin(x), obtem_col(x)


def ordena_intersecoes(tup):
    """
    Esta função recebe um tuplo
    contendo interseções e ordena-os
    de acordo com a linha e a coluna
    de seguida

    Args:
        tup (tuplo): conjunto de interseções

    Raises:
        ValueError: caso os argumentos do tuplo não sejam interseções

    Returns:
        tuplo: conjunto de interseções ordenado
    """
    for i in tup:
        if not eh_intersecao(i):
            raise ValueError("ordena_intesecoes: argumento invalido")
    return tuple(sorted(tup, key=compara))


# ----------------------------------------------2.1.2-----------------------------------------------#
#                                            TAD pedra                                             #


# Construtores
def cria_pedra_branca():
    """
    Esta função cria uma pedra branca

    Returns:
        str: pedra branca
    """
    return "O"


def cria_pedra_preta():
    """
    Esta função cria uma pedra preta

    Returns:
        str: pedra preta
    """
    return "X"


def cria_pedra_neutra():
    """
    Esta função cria uma pedra neutra

    Returns:
        str: pedra netura
    """
    return "."


# Reconhecedores
def eh_pedra(arg):
    """
    Esta função recebe um argumento
    e devolve se é uma pedra ou não

    Args:
        arg (any): Qualquer coisa

    Returns:
        bool: Se é uma pedra ou não
    """
    return (
        arg == cria_pedra_branca()
        or arg == cria_pedra_preta()
        or arg == cria_pedra_neutra()
    )


def eh_pedra_branca(arg):
    """
    Esta função recebe um argumento e
    devolve se é uma pedra branca ou não

    Args:
        arg (any): Qualquer coisa

    Returns:
        bool: Se é uma pedra branca ou não
    """
    return arg == cria_pedra_branca()


def eh_pedra_preta(arg):
    """
    Esta função recebe um argumento e
    devolve se é uma pedra preta ou não

    Args:
        arg (any): Qualquer coisa

    Returns:
        bool: Se é uma pedra preta ou não
    """
    return arg == cria_pedra_preta()


# Testes
def pedras_iguais(p1, p2):
    """
    Esta função recebe duas pedras e
    devolve se as pedras são iguais

    Args:
        p1,p2 (str): duas pedras

    Returns:
        bool: Se as pedras são iguais
    """
    if not (eh_pedra(p1) and eh_pedra(p2)):
        raise ValueError("pedras_iguais: argumentos invalidos")
    return p1 == p2


# Transformadores
def pedra_para_str(p):
    """
    Esta função recebe uma pedra e
    devolve a pedra em forma de string
    no goban

    Args:
        p (str): pedra
    Raises:
        ValueError: caso o argumento não seja uma pedra

    Returns:
        str: string da pedra no goban
    """
    if not eh_pedra(p):
        raise ValueError("pedra_para_str: argumento invalido")
    if p == cria_pedra_branca():
        return "O"
    elif p == cria_pedra_preta():
        return "X"
    elif p == cria_pedra_neutra():
        return "."


# Funções de alto nível
def eh_pedra_jogador(p):
    """
    Esta função recebe uma pedra e
    devolve se é uma pedra de um jogador

    Args:
        p (str): pedra

    Returns:
        bool: "True" se p é uma pedra de um jogador
        "False" caso contrário
    """
    return p == cria_pedra_branca() or p == cria_pedra_preta()


# ----------------------------------------------2.1.3-----------------------------------------------#
#                                            TAD pedra                                             #


# Construtores
def cria_goban_vazio(n):
    """
    Esta função recebe um número
    e devolve um goban vazio
    de tamanho n x n

    Args:
        n (int): tamanho do goban

    Raises:
        ValueError: o goban tem de ter 9, 13, 19 de tamanho da linha

    Returns:
        dict: goban
    """
    valores_possiveis = (9, 13, 19)
    if n not in valores_possiveis:
        raise ValueError("cria_goban_vazio: argumento invalido")
    goban = {}
    for coluna in range(1, n + 1):
        letra = chr(coluna + 64)
        territorio = ". " * n
        goban[letra] = territorio.split()
    return goban


def cria_goban(n, ibs, ips):
    """
    Esta função recebe um numero e dois
    conjuntos de tuplos, devolvendo um
    goban com as pedras nas respetivas
    interseções

    Args:
        n (int): tamanho do goban
        ibs (tuplo): interseções das pedras brancas
        ips (tuplo): interseções das pedras pretas

    Raises:
        ValueError: caso n não seja 9, 13 ou 19
        ValueError: caso os argumentos dos tuplos não sejam interseções
        ValueError: caso os argumentos dos tuplos não sejam interseções

    Returns:
        dict: goban
    """
    if n not in (9, 13, 19):
        raise ValueError("cria_goban: argumentos invalidos")
    goban = cria_goban_vazio(n)
    for ib in ibs:
        if not eh_intersecao(ib) or ib in ips or len(ibs) != len(set(ibs)):
            raise ValueError("cria_goban: argumentos invalidos")
        goban[obtem_col(ib)][obtem_lin(ib) - 1] = cria_pedra_branca()
    for ip in ips:
        if not eh_intersecao(ip) or ip in ibs or len(ips) != len(set(ips)):
            raise ValueError("cria_goban: argumentos invalidos")
        goban[obtem_col(ip)][obtem_lin(ip) - 1] = cria_pedra_preta()
    return goban


def cria_copia_goban(g):
    """
    Esta função recebe um goban
    e devolve uma cópia do mesmo

    Args:
        g (dict): goban

    Returns:
        dict: cópia do goban
    """
    return {key: value[:] for key, value in g.items()}


# Seletores
def obtem_ultima_intersecao(g):
    """
    Esta função recebe um goban e
    devolve a ultima interseção do
    mesmo

    Args:
        g (dict): goban

    Returns:
        tuplo: ultima interseção do goban
    """
    return (chr(len(g) + 64), len(g))


def obtem_pedra(g, i):
    """
    Esta função recebe um goban
    e uma interseção, e devolve
    a pedra da interseção

    Args:
        g (dict): goban
        i (tuplo): interseção

    Returns:
        str: pedra
    """
    p = g[obtem_col(i)][obtem_lin(i) - 1]
    if p == "O":
        return cria_pedra_branca()
    elif p == "X":
        return cria_pedra_preta()
    elif p == ".":
        return cria_pedra_neutra()


def obtem_cadeia(g, i):
    """
    Esta função recebe um goban e
    uma interseção e devolve a cadeia
    em que esta interseção pertence

    Args:
        g (dict): goban
        i (tuplo): interseção

    Raises:
        ValueError: caso o g não seja um goban e caso i
        não seja um interseção

    Returns:
        tuplo: conjunto das interseções da cadeia
    """
    if not eh_intersecao_valida(g, i):
        raise ValueError("obtem_cadeia: argumentos invalidos")
    res = [
        i,
    ]
    j = 0
    l = obtem_ultima_intersecao(g)
    while j < len(res):
        adjs = obtem_intersecoes_adjacentes(res[j], l)
        for adj in adjs:
            if adj not in res:
                if (
                    g[obtem_col(adj)][obtem_lin(adj) - 1]
                    == g[obtem_col(i)][obtem_lin(i) - 1]
                ):
                    res.append(adj)
        j += 1
    return tuple(ordena_intersecoes(tuple(res)))


# Modificadores
def coloca_pedra(g, i, p):
    """
    Esta função recebe um goban, uma interseção
    e uma pedra, devolvendo um novo goban com
    a pedra posta

    Args:
        g (dict): goban
        i (int): interseção
        p (str): pedra

    Raises:
        ValueError: caso g e i não seja uma interseção
        válida e caso p não seja uma pedra

    Returns:
        dict: goban modificado
    """
    if not (eh_intersecao_valida(g, i) and eh_pedra_jogador(p)):
        raise ValueError("coloca_pedra: argumentos invalidos")
    g[obtem_col(i)][int(obtem_lin(i)) - 1] = pedra_para_str(p)
    return g


def remove_pedra(g, i):
    """
    Esta função recebe um goban e uma interseção
    devolvendo um goban novo, sem a pedra na
    interseção

    Args:
        g (dict): goban
        i (tuplo): interseção

    Raises:
        ValueError: caso g e i não seja uma interseção válida

    Returns:
        dict: goban modificado
    """
    if not eh_intersecao_valida(g, i):
        raise ValueError("coloca_pedra: argumentos invalidos")
    if (
        g[obtem_col(i)][int(obtem_lin(i)) - 1] == "X"
        or g[obtem_col(i)][int(obtem_lin(i)) - 1] == "O"
    ):
        g[obtem_col(i)][int(obtem_lin(i)) - 1] = "."
    return g


def remove_cadeia(g, t):
    """
    Esta função recebe um goban e uma cadeia
    de interseções, removendo a cadeia do goban

    Args:
        g (dict): goban
        t (tuplo): cadeia

    Returns:
        dict: goban modificado
    """
    for i in t:
        remove_pedra(g, i)
    return g


# Reconhecedores
def eh_goban(arg):
    """
    Esta função recebe um argumento
    devolvendo "True" caso seja um goban
    e "False" caso contrário

    Args:
        arg (any): Qualquer coisa

    Returns:
        bool: "True" ou "False
    """
    valores_possiveis = (9, 13, 19)
    if isinstance(arg, dict) and len(arg) in valores_possiveis:
        for key, value in arg.items():
            if (
                len(key) == 1
                and "A" <= key <= chr(len(arg) + 65)
                and isinstance(value, list)
                and len(value) == len(arg)
            ):
                for i in value:
                    if i == "." or i == "X" or i == "O":
                        continue
                    return False
            else:
                return False
    else:
        return False
    return True


def eh_intersecao_valida(g, i):
    """
    Esta função recebe um goban e uma interseção
    devolvendo "True" caso i esteja no goban
    e "False" caso contrário

    Args:
        g (dict): goban
        i (tuplo): interseção

    Returns:
        bool: "True" ou "False"
    """
    if not (eh_goban(g) and eh_intersecao(i)):
        return False
    if obtem_col(i) in g.keys() and int(obtem_lin(i)) <= len(g[f"{obtem_col(i)}"]):
        return True
    return False


# Testes
def gobans_iguais(g1, g2):
    """
    Esta função recebe dois gobans
    e devolve "True" caso sejam iguais,
    "False" caso contrário

    Args:
        g1 (dict): goban
        g2 (dict): goban

    Returns:
        bool: "True" ou "False"
    """
    if not (eh_goban(g1) and eh_goban(g2)):
        return False
    if len(g1.keys()) != len(g2.keys()):
        return False
    for key in g1:
        if g1[key] != g2.get(key):
            return False
    return True


# Trasnformadores
def goban_para_str(g):
    """
    Esta função recebe um goban
    e devolve o mesmo goban na
    forma de string, para os nossos
    olhos

    Args:
        g (dict): goban

    Raises:
        ValueError: caso g não for um goban

    Returns:
        str: goban para os nossos olhos
    """
    if not eh_goban(g):
        raise ValueError("goban_para_str: argumento invalido")
    inicio = "   "
    j = len(g["A"])
    for letra in g.keys():
        inicio += f"{letra} "
    meio = ""
    while j > 0:
        if j < 10:
            meio += f" {j} "
        elif j > 9:
            meio += f"{j} "
        for coluna in g.items():
            meio += f"{coluna[1][j - 1]} "
        if j < 10:
            meio += f" {j}" + "\n"
        elif j > 9:
            meio += f"{j}" + "\n"
        # Se o tamanho for menor que 10, é necessário um espaço
        j -= 1

    return inicio[:-1] + "\n" + meio + inicio[:-1]


# Funções de alto nível
def obtem_territorios(g):
    """
    Esta função recebe um goban
    e devolve os territórios do
    mesmo

    Args:
        g (dict): goban

    Raises:
        ValueError: caso g não for um goban

    Returns:
        tuplo: conjunto dos territórios
    """
    if not eh_goban(g):
        raise ValueError("obtem_adjacentes_diferentes: argumentos invalidos")
    terr = ()
    for letra, col in g.items():
        for j in range(len(col)):
            if (
                col[j] == pedra_para_str(cria_pedra_neutra())
                and cria_intersecao(letra, j + 1) not in terr
            ):
                # Por cada interseção na coluna, vê se a interseção é uma pedra neutra,
                # e se a interseção não está no território
                cadeia = obtem_cadeia(g, cria_intersecao(letra, j + 1))
                if cadeia not in terr:
                    terr += (cadeia,)
    return tuple(tuple(cadeia) for cadeia in terr)


def obtem_adjacentes_diferentes(g, t):
    """
    Esta função recebe um goban e um conjunto
    de interseções, devolvendo as cadeias
    das interseções diferentes adjacentes

    Args:
        g (dict): goban
        t (tuplo): conjunto de interseções

    Raises:
        ValueError: caso g não seja um goban
        ValueError: caso i não seja uma interseção válida em g

    Returns:
        tuplo: conjunto de interseções diferentes
    """
    res = ()
    if not eh_goban(g):
        raise ValueError("obtem_adjacentes_diferentes: argumentos invalidos")
    for i in t:
        if not eh_intersecao_valida(g, i):
            raise ValueError("obtem_adjacentes_diferentes: argumentos invalidos")
        adjs = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
        for adj in adjs:
            if (
                g[obtem_col(adj)][obtem_lin(adj) - 1] == "."
                and (
                    g[obtem_col(i)][obtem_lin(i) - 1] == "X"
                    or g[obtem_col(i)][obtem_lin(i) - 1] == "O"
                )
                and adj not in res
            ):
                res += (adj,)
            elif (
                (
                    g[obtem_col(adj)][obtem_lin(adj) - 1] == "X"
                    or g[obtem_col(adj)][obtem_lin(adj) - 1] == "O"
                )
                and g[obtem_col(i)][obtem_lin(i) - 1] == "."
                and adj not in res
            ):
                res += (adj,)
    return tuple(ordena_intersecoes(res))


def jogada(g, i, p):
    """
    Esta função recebe um goban, uma interseção
    e uma pedra, devolvendo um goban novo com a
    jogada na interseção

    Args:
        g (dict): goban
        i (tuplo): interseção
        p (string): pedra

    Raises:
        ValueError: caso os argumentos não sejam válidos

    Returns:
        dict: goban modificado
    """
    if not (eh_intersecao_valida(g, i) and eh_pedra_jogador(p)):
        raise ValueError("jogada: argumentos invalidos")
    adjs = obtem_intersecoes_adjacentes(i, obtem_ultima_intersecao(g))
    if g[obtem_col(i)][obtem_lin(i) - 1] == ".":
        g1 = coloca_pedra(g, i, p)
        ilegal = obtem_adjacentes_diferentes(g1, obtem_cadeia(g1, i))
    for adj in adjs:
        liberdades = obtem_adjacentes_diferentes(g1, obtem_cadeia(g1, adj))
        if liberdades == ():
            g2 = remove_cadeia(g, obtem_cadeia(g1, adj))
            return g2
    if ilegal == ():
        remove_pedra(g1, i)
        return g1
        # Caso a jogada seja ilegal
    return g1


def obtem_pedras_jogadores(g):
    """
    Esta função recebe um goban e devolve
    as pedras presentes de cada jogador

    Args:
        g (dict): goban

    Raises:
        ValueError: caso g não for um goban

    Returns:
        tuplo: contém as pedras de ambos os jogadores
    """
    if not eh_goban(g):
        raise ValueError("obtem_pedras_jogadores: argumento invalido")
    pretas = 0
    brancas = 0
    for key in g.keys():
        for i in g[key]:
            if i == pedra_para_str(cria_pedra_branca()):
                brancas += 1
            elif i == pedra_para_str(cria_pedra_preta()):
                pretas += 1
    return (brancas, pretas)


# ----------------------------------------------2.2.1-----------------------------------------------#
#                                         Calcula pontos                                           #


def calcula_pontos(g):
    """
    Esta função recebe um goban e devolve
    os pontos de cada jogador

    Args:
        g (dict): goban

    Raises:
        ValueError: caso g não for um goban

    Returns:
        tuplo: contém os pontos de cada jogador
    """
    if not eh_goban(g):
        raise ValueError("calcula_pontos: argumento invalido")
    terrs = obtem_territorios(g)
    pontos_p = 0
    pontos_b = 0
    for terr in terrs:
        pretas, brancas = [], []
        adjs = obtem_adjacentes_diferentes(g, terr)
        for i in range(1, len(adjs)):
            if (
                g[obtem_col(adjs[i])][obtem_lin(adjs[i]) - 1] == cria_pedra_preta()
                and g[obtem_col(adjs[i - 1])][obtem_lin(adjs[i - 1]) - 1]
                == cria_pedra_preta()
            ):
                pretas += [
                    cria_pedra_preta(),
                ]
                brancas += [
                    cria_pedra_preta(),
                ]
            elif (
                g[obtem_col(adjs[i])][obtem_lin(adjs[i]) - 1] == cria_pedra_branca()
                and g[obtem_col(adjs[i - 1])][obtem_lin(adjs[i - 1]) - 1]
                == cria_pedra_branca()
            ):
                pretas += [
                    cria_pedra_branca(),
                ]
                brancas += [
                    cria_pedra_branca(),
                ]
        if cria_pedra_preta() in pretas and cria_pedra_branca() not in pretas:
            pontos_p += len(terr)
        elif cria_pedra_branca() in brancas and cria_pedra_preta() not in brancas:
            pontos_b += len(terr)
    return (
        pontos_b + obtem_pedras_jogadores(g)[0],
        pontos_p + obtem_pedras_jogadores(g)[1],
    )


def eh_jogada_legal(g, i, p, l):
    """
    Esta função recebe um goban, uma interseção,
    uma pedra e um outro goban, para comparar com
    o 1º, devolvendo caso a jogada da pedra na interseção
    é legal

    Args:
        g (dict): goban
        i (tuplo): interseção
        p (str): pedra
        l (dict): goban que não pode ser obtido

    Returns:
        bool: "True" ou "False"
    """
    if not (eh_intersecao_valida(g, i) and eh_pedra_jogador(p) and eh_goban(l)):
        return False
    copy = cria_copia_goban(g)
    i1 = g[obtem_col(i)][obtem_lin(i) - 1]
    if pedras_iguais(i1, cria_pedra_neutra()):
        g1 = jogada(copy, i, p)
    elif pedras_iguais(i1, cria_pedra_preta()) or pedras_iguais(
        i1, cria_pedra_branca()
    ):
        return False
    if eh_pedra_preta(p) and calcula_pontos(g1)[1] <= calcula_pontos(g)[1]:
        if obtem_pedras_jogadores(g1)[1] > obtem_pedras_jogadores(g)[1]:
            return True
        return False
    if eh_pedra_branca(p) and calcula_pontos(g1)[0] <= calcula_pontos(g)[0]:
        if obtem_pedras_jogadores(g1)[0] > obtem_pedras_jogadores(g)[0]:
            return True
        return False
    if gobans_iguais(g1, l):
        return False
    return True


def turno_jogador(g, p, l):
    """
    Esta função recebe um goban, uma pedra
    e um outro goban para ser comparado com
    o 1º, e um input que recebe uma interseção
    devolvendo "True" se o turno ser jogado e
    "False" caso contrário

    Args:
        g (dict): goban
        p (str): pedra
        l (dict): goban que não pode ser obtido

    Raises:
        ValueError: caso não sejam argumentos válidos

    Returns:
        bool: "True" ou "False"
    """
    if not (eh_goban(g) and eh_pedra_jogador(p) and eh_goban(l) and len(g) == len(l)):
        raise ValueError("turno_jogador: argumentos invalidos")
    if pedras_iguais(p, cria_pedra_preta()):
        x = input("Escreva uma intersecao ou 'P' para passar [X]:")
    elif pedras_iguais(p, cria_pedra_branca()):
        x = input("Escreva uma intersecao ou 'P' para passar [O]:")
    if x == "P":
        return False
    else:
        if not (eh_str(x)):
            return turno_jogador(g, p, l)
        i = cria_intersecao(x[0], int(x[1:]))
        if eh_intersecao_valida(g, i) and eh_jogada_legal(g, i, p, l):
            jogada(g, i, p)
            return True
        else:
            return turno_jogador(g, p, l)


def go(n, tb, tp):
    """
    Esta função recebe um número do tamanho do
    goban, e dois conjuntos contendo as interseções
    onde as pedras dos jogadores estão na posição
    incial, devolvendo "True" caso as brancas ganhem
    e "False" caso contrário

    Args:
        n (int): tamanho do goban
        tb (tuplo): conjunto das interseções das pedras brancas
        tp (tuplo): conjunto das interseções das pedras pretas

    Raises:
        ValueError: caso não seja uma interseção
        ValueError: caso não seja uma interseção
        ValueError: caso não seja um goban

    Returns:
        bool: "True" ou "False"
    """
    int_brancas = ()
    int_pretas = ()
    for branca in tb:
        if not eh_str(branca):
            raise ValueError("go: argumentos invalidos")
        int_brancas += (str_para_intersecao(branca),)
    for preta in tp:
        if not eh_str(preta):
            raise ValueError("go: argumentos invalidos")
        int_pretas += (str_para_intersecao(preta),)
    g = cria_goban(n, int_brancas, int_pretas)
    j = -1
    k = 0
    l = cria_copia_goban(g)
    while j != 0 or k != 2:
        if not eh_goban(g):
            raise ValueError("jogo: argumento invalido")
        print(
            f"Branco (O) tem {calcula_pontos(g)[0]} pontos\nPreto (X) tem {calcula_pontos(g)[1]} pontos\n{goban_para_str(g)}"
        )
        if j < 0:
            p = cria_pedra_preta()
        if j > 0:
            p = cria_pedra_branca()
        if turno_jogador(g, p, l):
            k = 0
            j *= -1
            l = cria_copia_goban(g)
        else:
            k += 1
            j *= -1
    return calcula_pontos(g)[0] > calcula_pontos(g)[1]
