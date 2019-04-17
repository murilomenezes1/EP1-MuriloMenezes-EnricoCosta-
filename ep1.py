# EP 2019-1: Escape Insper
#
# Alunos: 

# - aluno A: Enrico Venturini Costa, enricovc@al.insper.edu.br
# - aluno B: Murilo Lima de Campos Menezes, murilolcm@al.insper.edu.br



def carregar_cenarios():
	cenarios = {
		"inicio": {
			"titulo" : "Entrada Quatá 300",
			"descricao" : "Voce esta na entrada do Insper.",
			"opcoes": {
				"casa do pão de queijo": "seguir em direcao a casa do pão de queijo",
				"biblioteca": "ir para biblioteca",
				"andar dos professores": "subir pelo elevador até o andar dos professores."
			}
		},
		"casa do pão de queijo" : {
			"titulo" : "power up store",
			"descricao" : "voce chegou a power up store! Aqui voce pode comprar upgrades.",
			"opcoes" : {
				"comprar": "falar com o vendedor para comprar seu upgrade.",
				"inicio" : "voltar para Entrada"
			}
		},
		"biblioteca" : {
			"titulo" : "biblioteca",
			"descricao": "voce chegou a biblioteca e encontrou um veterano irritado, derrote-o para ganhar XP e dinheiro",
			"opcoes" : {
				"lutar":"ganhar XP e dinheiro",
				"inicio":"voltar para a entrada"
			}
		},
		"andar dos professores" : {
			"titulo" : "salas dos professores",
			"descricao" : "voce chegou ao andar dos professores, mas tres estudantes level 5 travam a passagem para a sala do professor de Desoft. Derrote-os para seguir em frente.",
			"opcoes" : {
				"Lutar":"Desafiar cada estudante para acessar a sala do professor.",
				"inicio":"voltar para a entrada"
			}
		}

	}
	nome_cenario_atual = "inicio"
	return cenarios, nome_cenario_atual


def main():
	print("Azedou, o EP1 chegou!")
	print()
	print("---------------------")
	print()
	avatar = input("Qual é o seu nome? ")
	print()
	print("ééé {0}... A data de entrega do EP1 é amanhã e você ficou fazendo hora extra no suujinhus"
			", agora tem que correr atrás do prejuízo e tentar adiar essa bagaça."
			"Você está na entrada do Insper, veja se consegue encontrar o professor e convencê-lo a fazer a famosa 'boa'.".format(avatar))

	cenarios, nome_cenario_atual = carregar_cenarios()

	game_over = False

	while not game_over:
		cenario_atual = cenarios[nome_cenario_atual]

		print(cenario_atual["titulo"])
		print()
		print("-"*len(cenario_atual["titulo"]))
		print()
		print(cenario_atual["descricao"])
		print()
		print("Decida como seguir em frente.")
		print()


		opcoes = cenario_atual["opcoes"]
		if len(opcoes) == 0:
			print("Rodou, fiote... o Toshi vai te jantar.")
			game_over = True

		else: 
			for opcao, descricao_da_opcao in cenario_atual["opcoes"].items():
				print("{0}:{1}".format(opcao, descricao_da_opcao))
			escolha = input("Eai, qual vai ser? ")

			if escolha in opcoes:
				nome_cenario_atual = escolha

			else: 
				print("Moiou o bigode, sepa você perdeu...")
				game_over = True

	print("Azedou teu caldo, você morreu!")



# Programa Principal.
if __name__ == "__main__":

	main()

	


