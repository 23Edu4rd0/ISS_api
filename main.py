from utils.email_sender import EmailSender
import time

if __name__ == "__main__":
    try:
        EmailSender().enviar_email()
    except Exception as e:
        print(f"Erro ao enviar email: {e}")
