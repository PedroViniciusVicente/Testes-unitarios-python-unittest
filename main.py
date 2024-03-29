import unittest

"""
    Nome: Pedro Vicente
    RA: 812124
    Descricao: Elaboracao e aplicacao de testes unitarios 
    usando o pyunit 
"""

# Classe que vai realizar os testes unitarios
class classeTestesUnitarios(unittest.TestCase):

    # Definindo os objetos que serao usados em cada teste unitario
    def setUp(self):
        self.bibliotecaUFSCar = Biblioteca(25.0)
        self.livro1 = Livro("Codigo limpo", "Robert Cecil", 10)
        self.livro2 = Livro("Extreme programming", "Kent Beck", 15)
        self.livro3 = Livro("Dom Casmurro", "Machado de Assis", 20)
        self.livro4 = Livro("Romeu e Julieta", "Willian Shakespeare", 100)
        self.aluno1 = Aluno("Pedro", 812124, 30.5)
        self.aluno2 = Aluno("Joao", 111222, 50.0)
        self.aluno3 = Aluno("Matheus", 333444, 150.0)
        self.aluno4 = Aluno("Thiago", 555666, 10.5)

    # -=+=- Definindo os 18 testes unitarios -=+=-
    
    # Testanto o costrutor da classe Biblioteca
    def testeConstrutorBiblioteca(self):
        self.assertEqual(self.bibliotecaUFSCar.dinheiro, 25.0)

    # Testanto o costrutor da classe Livro
    def testeConstrutorLivro(self):
        self.assertEqual(self.livro1.titulo, 'Codigo limpo')
        self.assertEqual(self.livro1.autor, 'Robert Cecil')
        self.assertEqual(self.livro1.preco, 10)

    # Testanto o costrutor da classe Aluno
    def testeConstrutorAluno(self):
        self.assertEqual(self.aluno1.nome, 'Pedro')
        self.assertEqual(self.aluno1.RA, 812124)
        self.assertEqual(self.aluno1.dinheiro, 30.5)
        
    # Testando o sucesso na compra com a funcao comprarNovoLivro
    def testeBCoComprarLivroBarato(self):
        # biblioteca tem $25, e o livro custa $15, logo ele deve deixar comprar
        retorno = self.bibliotecaUFSCar.comprarNovoLivro(self.livro2)
        self.assertTrue(retorno, "Comprar um livro barato deveria retornar True!")

    # Testando se o dinheiro foi cobrado corretamente da biblioteca
    def testDinheiroBCoDiminui(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro2)
        self.assertEqual(self.bibliotecaUFSCar.dinheiro, 25 - self.livro2.preco, "Dinheiro da biblioteca deveria diminuir corretamente na compra de livros!")

    # Testando a falha na compra com a funcao ComprarNovoLivro
    def testeBCoComprarLivroCaro(self):
        # biblioteca tem $25, e o livro custa $100, logo ele nao deve deixar comprar
        retorno = self.bibliotecaUFSCar.comprarNovoLivro(self.livro4)
        self.assertFalse(retorno, "Comprar um livro caro deveria retornar False!")

    # Testando o sucesso no emprestimo com a funcao pegarEmprestado
    def testeEmprestarLivroExistente(self):
        # o livro3 foi comprado e adicionado ao acervo da biblioteca
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        retorno = self.aluno2.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.assertTrue(retorno, "Pegar emprestado um livro existente deveria retornar True!")

    # Testando a falha no emprestimo com a funcao pegarEmprestado
    def testeEmprestarLivroInexistente(self):
        # note que o livro3 nao foi comprado pela biblioteca ainda
        retorno = self.aluno2.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.assertFalse(retorno, "Pegar emprestado um livro inexistente deveria retornar False!")

    # Testando o sucesso na devolucao com a funcao devolver
    def testeDevolverLivroExistente(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno2.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        retorno = self.aluno2.devolver(self.livro3, self.bibliotecaUFSCar, 5)
        self.assertTrue(retorno, "Devolver um livro existente deveria retornar True!")
        
    # Testando a falha na devolucao com a funcao devolver
    def testeDevolverLivroInexistente(self):
        # note que o aluno2 nem possui o livro3 para devolver
        retorno = self.aluno2.devolver(self.livro3, self.bibliotecaUFSCar, 5)
        self.assertFalse(retorno, "Devolver um livro inexistente deveria retornar False!")

    # Testando o sucesso na aplicacao de multa com a funcao devolver, verificaAtraso e aplicarMulta
    def testeRecebeuMulta(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno3.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.aluno3.devolver(self.livro3, self.bibliotecaUFSCar, 30)
        self.assertEqual(len(self.aluno3.multasPendentes), 1, "O aluno3 deveria receber uma multa!")

    # Testando se a multa foi feita com o valor correto 
    # obs: o valor correto deve ser: data de devolucao - data de emprestimo - 10
    def testeMultaValorCorreto(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno3.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.aluno3.devolver(self.livro3, self.bibliotecaUFSCar, 30)
        self.assertEqual(self.aluno3.multasPendentes[0].valor, 30 - 1 - 10, "A multa deveria ter o valor correto!")

    # Testando o sucesso no pagamento com a funcao pagarTodasMultas
    def testePagarMultaBarata(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno3.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.aluno3.devolver(self.livro3, self.bibliotecaUFSCar, 30)
        retorno = self.aluno3.pagarTodasMultas()
        self.assertTrue(retorno, "O aluno deveria conseguir pagar todas as multas com sucesso e deveria retornar True!")

    # Testando se a multa sai do multasPendentes corretamente apos seu pagamento
    def testePagarMultaBarataMultaRemovida(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno3.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.aluno3.devolver(self.livro3, self.bibliotecaUFSCar, 30)
        self.aluno3.pagarTodasMultas()
        self.assertEqual(len(self.aluno3.multasPendentes), 0, "A multa deveria sair do multasPendentes apos ser paga!")

    # Testanto se o valor cobrado do aluno pela multa foi descontado corretamente
    def testePagarMultaBarataAlunoPerdeuDinheiro(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno3.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.aluno3.devolver(self.livro3, self.bibliotecaUFSCar, 30)
        self.aluno3.pagarTodasMultas()
        self.assertEqual(self.aluno3.dinheiro, 150 - (30 -1 - 10), "O aluno deveria ter seu dinheiro diminuido corretamente!")

    # Testanto se o valor cobrado do aluno pela multa foi somado para a biblioteca corretamente
    def testePagarMultaBarataBCoGanhouDinheiro(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno3.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.aluno3.devolver(self.livro3, self.bibliotecaUFSCar, 30)
        self.aluno3.pagarTodasMultas()
        self.assertEqual(self.bibliotecaUFSCar.dinheiro, 25 - self.livro3.preco + (30 -1 - 10), "O dinheiro da biblioteca deveria ser acrescido corretamente!")

    # Testando a falha no pagamento com a funcao pagarTodasMultas
    def testePagarMultaCara(self):
        # note que o aluno3 tem 150 reais, mas a multa custa 354 reais
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno3.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.aluno3.devolver(self.livro3, self.bibliotecaUFSCar, 365)
        retorno = self.aluno3.pagarTodasMultas()
        self.assertFalse(retorno, "O aluno deveria nao conseguir pagar todas as multas com sucesso e deveria retornar False!")

    # Testando a falha no emprestimo devido ao aluno ter multa pendente
    def testeEmprestarLivroComMultaPendente(self):
        self.bibliotecaUFSCar.comprarNovoLivro(self.livro3)
        self.aluno2.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 1)
        self.aluno2.devolver(self.livro3, self.bibliotecaUFSCar, 30)
        # o aluno2 tenta pegar o livro3 novamente, mas agora ele tem multa pendente
        retorno = self.aluno2.pegarEmprestado(self.livro3, self.bibliotecaUFSCar, 31)
        self.assertFalse(retorno, "O aluno deveria nao conseguir pegar o livro3 novamente com multa pendente e deveria retornar False")


# -=+=- Implementacao do sistema -=+=-

class Livro:
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor
        self.preco = preco
        self.dataUltimoEmprestimo = 0
        self.dataUltimaDevolucao = 0


class Aluno:
    def __init__(self, nome, RA, dinheiro):
        self.nome = nome
        self.RA = RA
        self.dinheiro = dinheiro
        self.livrosEmprestados = []
        self.multasPendentes = []

    # Função para pegar um livro emprestado da bilioteca
    def pegarEmprestado(self, livroBuscado, biblioteca, data):
        if len(self.multasPendentes) == 0:
            if livroBuscado in biblioteca.livrosNoAcervo:
                livroBuscado.dataUltimoEmprestimo = data
                self.livrosEmprestados.append(livroBuscado)
                biblioteca.livrosNoAcervo.remove(livroBuscado)
                print(f"{self.nome} pegou o livro {livroBuscado.titulo} com sucesso!")
                return True
            else:
                print(f"O livro {livroBuscado.titulo} não está disponível \
na biblioteca!")
                return False
        else:
            print(f"{self.nome} tem multas pendentes e por isso nao pode pegar o \
livro {livroBuscado.titulo}")
            return False

    # Função para devolver um livro emprestado
    def devolver(self, livroDevolver, biblioteca, data):
        if livroDevolver in self.livrosEmprestados:
            livroDevolver.dataUltimaDevolucao = data
            # funcao da biblioteca que aplica a multa caso tenha atraso
            atrasou = biblioteca.verificaAtraso(self, livroDevolver)
            
            self.livrosEmprestados.remove(livroDevolver)
            biblioteca.livrosNoAcervo.append(livroDevolver)
            if atrasou:
                print(f"{self.nome} devolveu o livro {livroDevolver.titulo} com \
sucesso! Mas recebeu multa!")
            else:
                print(f"{self.nome} devolveu o livro {livroDevolver.titulo} com \
sucesso! e nao recebeu multa!")
            return True
        else:
            print(f"{self.nome} nao possui o {livroDevolver.titulo} para devolver!")
            return False

    # Funcao para um aluno pagar todas as suas multas pendentes
    def pagarTodasMultas(self):
        while self.multasPendentes:
            if (self.dinheiro >= self.multasPendentes[0].valor):
                self.dinheiro -= self.multasPendentes[0].valor
                self.multasPendentes[0].bibliotecaQueMultou.dinheiro += self.multasPendentes[0].valor
                print(f"Multa de R$ {self.multasPendentes[0].valor} paga com sucesso \
por {self.nome}!")
                self.multasPendentes = self.multasPendentes[1:]
            else:
                print(f"Multa de R$ {self.multasPendentes[0].valor} nao pode \
ser paga por {self.nome}!")
                return False
        return True



class Biblioteca:
    def __init__(self, dinheiro):
        self.dinheiro = dinheiro
        self.livrosNoAcervo = []

    # Função para a biblioteca comprar novos livros para o seu acervo
    def comprarNovoLivro(self, livroComprar):
        if (self.dinheiro >= livroComprar.preco):
            self.dinheiro = self.dinheiro - livroComprar.preco
            self.livrosNoAcervo.append(livroComprar)
            print(f"A biblioteca comprou o livro {livroComprar.titulo} com sucesso!")
            return True
        print(f"A biblioteca nao pode comprar o livro {livroComprar.titulo}")
        return False

    # Função chamada pelo aluno ao devolver um livro emprestado para verificar atraso
    def verificaAtraso(self, aluno, livro):
        # o aluno só pode ficar com o livro por 10 dias para nao levar multa
        diasAtrasados = livro.dataUltimaDevolucao - livro.dataUltimoEmprestimo - 10
        if diasAtrasados > 0:
            multa = Multa(aluno, diasAtrasados, self)
            multa.aplicarMulta(self, aluno)
            return True
        print(f"O aluno {aluno.nome} nao recebeu multa por atraso")
        return False



class Multa:
    def __init__(self, aluno, valor, biblioteca):
        self.aluno = aluno
        self.valor = valor
        self.bibliotecaQueMultou = biblioteca

    # Função chamada por verificaAtraso para aplicar a multa em caso de atraso na 
    #devolucao de um livro por aluno
    def aplicarMulta(self, biblioteca, aluno):
        aluno.multasPendentes.append(self)
        print(f"O aluno {aluno.nome} recebeu uma multa de R$ {self.valor}")


if __name__ == "__main__":
    unittest.main()
