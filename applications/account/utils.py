from email import message

from django.core.mail import send_mail
from django.core.mail import EmailMessage


def send_activation_code(email, code):
    message = f'Перейдите по этой ссылке чтобы активировать аккаунт: \n\n https://api.samirkk.com/account/activate/{code}'

    email_message = EmailMessage(
        'Samirkk',
        message,
        'sassassas107@gmail.com',
        [email],
    )

    email_message.attach_file('/home/elmar20061602/samirkkk/emailimages/samirkk_.png')

    email_message.send()


def send_forgot_password_code(email, code):
    send_mail(
        'Samirkk',
        f'Вот ваш код для востоновления пароля, никому не показывайте его: {code}',
        'sassassas107@gmail.com',
        [email]
    )


