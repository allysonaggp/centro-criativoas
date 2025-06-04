from dotenv import load_dotenv
import os
from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="C:/Users/lord_/OneDrive/Área de Trabalho/projeto-faculdade/site anderson/.env")
print(os.getenv("EMAIL_REMETENTE"))
print(os.getenv("SENHA_APP"))


app = Flask(__name__)

EMAIL_REMETENTE = os.getenv('EMAIL_REMETENTE')
SENHA_APP = os.getenv('SENHA_APP')
EMAIL_DESTINO = os.getenv('EMAIL_DESTINO')

@app.route('/', methods=['GET', 'POST'])
def contato():
    if request.method == 'POST':
        nome = request.form['name']
        email = request.form['email']
        telefone = request.form['phone']
        assunto = request.form['subject']
        mensagem = request.form['message']

        corpo_email = f"""
        Nome: {nome}
        E-mail: {email}
        Telefone: {telefone}
        Assunto: {assunto}
        Mensagem:
        {mensagem}
        """

        msg = EmailMessage()
        msg['Subject'] = 'Novo contato do site'
        msg['From'] = EMAIL_REMETENTE
        msg['To'] = EMAIL_DESTINO
        msg.set_content(corpo_email)

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.set_debuglevel(1)
                smtp.login(EMAIL_REMETENTE, SENHA_APP)
                smtp.send_message(msg)
                print("Mensagem enviada com sucesso!")
             
             
        except Exception as e:
            print(f"[ERRO NO ENVIO] {e}")
            return f"Erro ao enviar mensagem: {e}"

    return render_template('index.html')

@app.route('/trabalhe_conosco')
def trabalhe_conosco():
    return render_template('trabalhe_conosco.html')
@app.route('/jovem_aprediz')
def trabalhe_conosco():
    return render_template('Jovem_aprendiz.html')

if __name__ == '__main__':
    app.run(debug=True)

