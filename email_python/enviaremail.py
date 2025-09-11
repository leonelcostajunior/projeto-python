import win32com.client as win32

#criar a integraçao com o outlook
outlook = win32.Dispatch('outlook.application')

#criar um email
email = outlook.CreateIten(0)

faturamento = 1500
qtde_produtos = 10
ticket_medio = faturamento /qtde_produtos

#Configurar as informações do seu e-mail
#A quantidade de email precisa ser separada por ;
email.To = "leonel.paiva.costa@hotmail.com"
email.Subject = "E-mail automático do Python"
email.HTMLBody = f"""
<p>Olá Léo, tudo bem com vc, aqui é o código Python.</P>

<p>O faturamento da loja foi de R${faturamento}</P>
<p>vendemos {qtde_produtos}</p>
<p>O ticket médio foi de R${ticket_medio}</P>


<p>Abs,</p>
<P>assinatura<p/>
"""
#precisa inserir o caminho onde o arquivo de anexo vai ser encontrado
anexo = "C://Users/joaozinho/downloads/nomedoarquivo.xlsx"
#Se existir mais de um anexo copiar a quantidade necessário o texto abaixo
email.Attachments.add(anexo)
email.Attachments.add(anexo)

email.Send()
print("Email Enviado")