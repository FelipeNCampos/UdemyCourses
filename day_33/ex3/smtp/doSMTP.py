import smtplib
import socket
from email.mime.text import MIMEText # Importe esta classe

class DoSMTP:
    def __init__(self, user: str, host: str, password: str, port: int = 587):
        self.user = user
        self.host = host
        self.password = password
        self.port = port

    def sendMessage(self, mailTo: str, subject: str, body: str):
        """
        Envia um e-mail para o destinatário especificado, com suporte a caracteres especiais.

        Args:
            mailTo (str): O endereço de e-mail do destinatário.
            subject (str): O assunto do e-mail.
            body (str): O corpo do e-mail.

        Raises:
            ConnectionError: Se houver problemas de conexão com o servidor SMTP.
            smtplib.SMTPAuthenticationError: Se a autenticação falhar (usuário/senha inválidos).
            smtplib.SMTPException: Para outros erros gerais do SMTP.
            Exception: Para erros inesperados.
        """
        try:
            # 1. Crie a mensagem MIME usando UTF-8 para suportar caracteres especiais
            msg = MIMEText(body, 'plain', 'utf-8')
            msg['Subject'] = subject # Assunto
            msg['From'] = self.user  # Remetente
            msg['To'] = mailTo       # Destinatário

            # Obtenha a string formatada MIME para enviar
            email_content = msg.as_string()

            with smtplib.SMTP(self.host, port=self.port) as connection:
                try:
                    connection.starttls()
                except smtplib.SMTPException as e:
                    raise ConnectionError(f"Erro ao iniciar TLS: {e}. Verifique o host e a porta.")

                try:
                    connection.login(user=self.user, password=self.password)
                except smtplib.SMTPAuthenticationError:
                    raise smtplib.SMTPAuthenticationError(
                        "Falha na autenticação. Verifique seu e-mail e senha/senha do aplicativo."
                    )
                except smtplib.SMTPException as e:
                    raise smtplib.SMTPException(f"Erro de login SMTP: {e}")

                try:
                    # Passe a string MIME completa (que já inclui from, to e subject)
                    # sendmail espera from_addr e to_addrs separados, mas msg pode ser a string completa
                    print(type(email_content))
                    connection.sendmail(from_addr=self.user, to_addrs=mailTo, msg=email_content)
                    print(f"E-mail enviado com sucesso de '{self.user}' para '{mailTo}'.")
                except smtplib.SMTPException as e:
                    raise smtplib.SMTPException(f"Erro ao enviar o e-mail: {e}")

        except (socket.gaierror, ConnectionRefusedError) as e:
            raise ConnectionError(f"Erro de conexão com o host/porta ({self.host}:{self.port}): {e}. Verifique a internet e as configurações do servidor.")
        except Exception as e:
            raise Exception(f"Ocorreu um erro inesperado: {e}")

