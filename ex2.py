import matplotlib.pyplot as plt
tempo_site = [5,10,15,20,25,30,35,40,45,50]
valor_compra = [50,80,100,120,150,160,180,200,210,220]
plt.scatter(tempo_site, valor_compra, color='green')
plt.title("Tempo no site vs Valor da compra")
plt.xlabel("Tempo no site (min)")
plt.ylabel("Valor da compra (R$)")
plt.show()