#DeclaracaoDasBibliotecas
import pandas as pd
from twilio.rest import Client

#InicioDoCodigo
lista_meses = [ 'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

 #LacoDeRepeticaoParaVarrerAsPlanilhas
for mes in lista_meses:
    print(mes)
    tabela_vendas  =  pd.read_excel (f'{mes}.xlsx' )
    print (tabela_vendas)
    if( tabela_vendas ['Vendas'] >55000).any() :
        vendedor = tabela_vendas.loc [tabela_vendas ['Vendas'] >55000,'Vendedor'].values[0]
        vendas = tabela_vendas.loc[ tabela_vendas ['Vendas'] >55000,'Vendas'].values[0]

#EscreveNaTelaOresultadoDaVarredura
        print(f'No mes de {mes} alguem com mais de 55000 alcançou a meta nome do vendedor: {vendedor}, Vendas: {vendas}.')

#CodigoAbaixoImplementaUmaFuncaoParaEnviarSMSdoResultadoDoCodigoAcimaBastaApenasConfigurarComUmaContaDaTwilio

"""""
 # Your Account SID from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
# Your Auth Token from twilio.com/console
auth_token  = 'your_auth_token'

client = Client(account_sid, auth_token)

message = client.messages.create(
    to='+15558675309', 
    from_='+15017250604',
    body='Hello from Python!')

print(message.sid)"""  

 