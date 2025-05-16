from utils.email_sender import EmailSender
import time

if __name__ == "__main__":
    while True:
        try:
            EmailSender().enviar_email()
        except Exception as e:
            print(f"Erro ao enviar email: {e}")
        time.sleep(60)
