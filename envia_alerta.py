import smtplib
import requests
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from utils.logs import logger_instance

class SendAlert:
    def send_email_alert(self,body,to_address,from_address,subject,password):
        try:
            msg = MIMEMultipart()
            msg['From'] = from_address
            msg['To'] = to_address
            msg['Subject'] = f"{subject}"        
            msg.attach(MIMEText(body, 'plain'))

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(from_address, password)
            server.sendmail(from_address, to_address, msg.as_string())
            server.quit()
            print(f"Alerta enviado por e-mail para {to_address}")
        except Exception as e:
            logger_instance.error(f"Erro ao enviar e-mail: {e}")

    def send_slack_alert(self,webhook_url,slack_data):
        try:
            response = requests.post(webhook_url, json=slack_data)
            if response.status_code == 200:
                print("Alerta enviado para o Slack com sucesso!")
            else:
                print(f"Erro ao enviar alerta no Slack. Código: {response.status_code}")
        except Exception as e:
            logger_instance.error(f"Erro ao enviar alerta para o Slack: {e}")
