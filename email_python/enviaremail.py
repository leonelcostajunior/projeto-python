import win32com.client as win32

#criar a integraçao com o outlook
outlook = win32.Dispatch('outlook.application')

#criar um email
email = outlook.CreateIten(0)

#Configurar as informações do seu e-mail
email.To = "leonel.paiva.costa@hotmail.com"
email.Subject = "E-mail automático do Python"
email.HTMLBody = """
<p>Olá Léo, tudo bem com vc, aqui é o código Python.</P>
<p>Estou te enviando um teste de envio de email.</P>
<p>Não é necessário responder.</p>

<p>Abs,</p>
<P>assinatura<p/>
"""

email.Send()
print("Email Enviado")