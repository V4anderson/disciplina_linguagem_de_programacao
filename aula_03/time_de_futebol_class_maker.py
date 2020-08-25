from time_de_futebol_class import TimeFutebol

objeto_a = TimeFutebol('Santa Cruz','Campo','Recife')
objeto_b = TimeFutebol('Nautico','Campo','Recife')

#objeto_a.ganhou()
#objeto_a.perdeu()
#objeto_a.ganhou()

objeto_a.ganhou(objeto_b.nome)
print('\n')
print('\n')
objeto_b.ganhou(objeto_a.nome)
