import calendar
c= calendar.TextCalendar(calendar.SUNDAY)

print("Programa em Python para se calcular os dias de serviço na escala. Utiliza a biblioteca Calendar do Python do ano 2024.")
dia_servico = int(input("Digite APENAS o dia do seu serviço/ EX: 3 \n "))
mes_servico = int(input("Digite o APENAS mês do seu serviço/ EX: 5 \n"))
escala = int(input("Sua escala é:\n1-Destacamento\n2-Sede\n "))

dias_do_ano = []
#[1,1],[2,1],[3,1] | todos os dias até o ano acabar

mes = 1

while mes < 13: 
    for  i in c.itermonthdays(2024,mes):
        if i != 0:
            dias_do_ano.append([i,mes])
    mes +=1

i = 0
while i < len(dias_do_ano):
    if dias_do_ano[i] == [dia_servico,mes_servico]:
        dia_servico = i
        break
    i+=1
#dia_serviço virou a posição de um vetor, que é o dia do serviço localizado nos dias_do_ano
#encontrou o dia de serviço no vetor dias_do_ano

if escala == 1:
    while len(dias_do_ano) > dia_servico:
        dia_escala1 = dias_do_ano[dia_servico]
        dia_escala2= dias_do_ano[dia_servico+1]
        dia_servico += 6
        print(f"Seu serviço é {dia_escala1[0]}/{dia_escala1[1]} e {dia_escala2[0]}/{dia_escala2[1]}")
elif escala == 2:                                              
    while len(dias_do_ano) > dia_servico:
        dia_escala1 = dias_do_ano[dia_servico]
        dia_servico += 4
        print(f"Seu serviço é {dia_escala1[0]}/{dia_escala1[1]}")
else:
    print("Vai pro destacamento praça novo.")
