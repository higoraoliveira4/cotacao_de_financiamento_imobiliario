valorcasa = int(input("Olá, para fazer a simulação de financiamento, a primeira informação necessária é o valor da casa que você deseja adquirir. R$:"))
salario = int(input("Agora preciso que você digite o valor do seu salário mensal. Pode digitar o valor bruto"))
tempofinanciamento = int(input("agora me conte em quantos anos você deseja pagar a sua casa"))

simulacaoparcela = salario*30/100
conversaoano = tempofinanciamento*12
simulacaofinanciamento = valorcasa/conversaoano

if simulacaofinanciamento > simulacaoparcela:
    print ("o valor da sua renda mensal seria comprometido em mais de 30%, portanto, você não está apto a realizar este financiamento.")
elif simulacaofinanciamento < simulacaoparcela:
    print ("a sua renda mensal é suficiente para à aprovação do financiamento!")

print ("se deseja tirar dúvidas com nossos corretores, entre em contato agora mesmo!")
