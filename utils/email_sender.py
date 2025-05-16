import smtplib
from email.message import EmailMessage
from services.iss_comparator import ISSComparator


class EmailSender:
    def send_email(self, subject, html_content, to_email):
        # Configurações do servidor SMTP (exemplo para Gmail)
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        from_email = 'eduardosecundario72@gmail.com'
        password = 'enjj eioe pftr ihwc'  # lembre de usar senha de app aqui

        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        msg.set_content('Este e-mail requer um cliente compatível com HTML.')
        msg.add_alternative(html_content, subtype='html')

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(from_email, password)
            server.send_message(msg)

    def enviar_email(self):
        comparador = ISSComparator()
        iss_lat, iss_lon = comparador.get_iss_data()
        if comparador.compare():
            html = f"""
            <html>
                <body>
                    <h1>ISS visível!</h1>
                    <p>A Estação Espacial Internacional está passando
                     pelo céu agora!</p>
                    <p>Posição atual da ISS: {iss_lat}, {iss_lon}</p>
                </body>
            </html>
            """
            self.send_email(
                subject="A ISS está visível!",
                html_content=html,
                to_email="eduardo.vchaves23@gmail.com"
            )
            print('Email enviado com sucesso!')
            return True
        else:
            print(f'A ISS não está visível no momento, ela esta na posição:\n'
                  f'latitude: {iss_lat} , longitude: {iss_lon}.')
            return False
