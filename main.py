print("Bem vindo à Loja de Tintas do seu ZÉ")
metros_quadrados = input("Qual a área em m²?\n")
metros_quadrados = float(metros_quadrados)

# Coloque o código para resolver o problema nessa parte do programa

lit = metros_quadrados / 3

if 0 < metros_quadrados <= 54:
  print("Serão necessárias 1 latas totalizando R$ 80")

elif metros_quadrados == 0:
  print("Serão necessárias 0 latas totalizando R$ 0")
  
else: 
  qtd_de_latas = lit / 18
  if lit % 18 > 0:
    qtd_de_latas += 1
  valor_total = int(qtd_de_latas) * 80
  print(f"Serão necessárias {int(qtd_de_latas)} latas totalizando R$ {valor_total}")

# As duas variáveis qtd_de_latas e valor_total devem guardar a resposta do problema
# Troque os zeros pelos valores corretos.


