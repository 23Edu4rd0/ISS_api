from utils.email_sender import EmailSender
import time

if __name__ == "__main__":
    inicio = time.time()
    EmailSender().enviar_email()
    fim = time.time()
    print(f"Tempo de execução: {fim - inicio:.4f} segundos")
