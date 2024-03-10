from email import message

from django.core.mail import send_mail
from django.core.mail import EmailMessage


def send_activation_code(email, code):
    message = f'Перейдите по этой ссылке чтобы активировать аккаунт: \n\n http://35.198.109.24/api/v1/account/activate/{code}'

    email_message = EmailMessage(
        'Samirkk',
        message,
        'sassassas107@gmail.com',
        [email],
    )

    email_message.attach_file('/home/user/Desktop/SAMIRKK/samirkkk/emailimages/samirkk_.png')

    email_message.send()


def send_forgot_password_code(email, code):
    send_mail(
        'Samirkk',
        f'Вот ваш код для востоновления пароля, никому не показывайте его: {code}',
        'sassassas107@gmail.com',
        [email]
    )


