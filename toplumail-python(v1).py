import smtplib
import time

def send_email(sender_email, sender_password, receiver_email, subject, message, smtp_server, smtp_port, encryption):
    msg = f"Subject: {subject}\n\n{message}"

    with smtplib.SMTP(smtp_server, smtp_port) as smtp:
        if encryption.lower() == 'ssl':
            smtp.ehlo()
            smtp.login(sender_email, sender_password)
        else:  # Use TLS by default
            smtp.starttls()
            smtp.login(sender_email, sender_password)
        
        smtp.sendmail(sender_email, receiver_email, msg)

def send_emails(sender_email, sender_password, receiver_emails, subject, message, interval, sender_smtp_server, sender_port, sender_encryption, receiver_smtp_server, receiver_port, receiver_encryption):
    for receiver_email in receiver_emails:
        send_email(sender_email, sender_password, receiver_email, subject, message, sender_smtp_server, sender_port, sender_encryption)
        print(f"E-posta gönderildi: {receiver_email}")
        time.sleep(interval)

sender_email = input("Gönderici e-posta adresi: ")
sender_password = input("Gönderici e-posta şifresi: ")
sender_smtp_server = input("Gönderici SMTP sunucusu: ")
sender_port = input("Gönderici SMTP portu: ")
sender_encryption = input("Gönderici şifreleme yöntemi (TLS/SSL): ")
receiver_emails = input("Alıcı e-posta adreslerini virgülle ayırarak girin: ").split(',')
receiver_smtp_server = input("Alıcı SMTP sunucusu: ")
receiver_port = input("Alıcı SMTP portu: ")
receiver_encryption = input("Alıcı şifreleme yöntemi (TLS/SSL): ")
subject = input("E-posta konusu: ")
message = input("E-posta mesajı: ")
interval = 604800 # saniye cinsinden aralik

while True:
    send_emails(sender_email, sender_password, receiver_emails, subject, message, interval, sender_smtp_server, sender_port, sender_encryption, receiver_smtp_server, receiver_port, receiver_encryption)
    time.sleep(interval)
