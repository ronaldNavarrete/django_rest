import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_correo(msg_destinatario_mail, msg_destinatario_nombre, msg_asunto, msg_body):
    
    from_email = 'ventanillacj@uniandes.edu.ec'
    to_email = msg_destinatario_mail
    subject = msg_asunto
    body = msg_body

    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.office365.com', 587)
    server.starttls()
    server.login('ventanillacj@uniandes.edu.ec', 'Consultorio2023*')

    try:
        server.sendmail(from_email, to_email, msg.as_string())
        estado = "ok"
    except Exception as e:
        estado = "error: " + str(e)

    server.quit()

    return {"estado": estado}