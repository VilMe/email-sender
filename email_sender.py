import smtplib, ssl
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import Any



def create_image_attachment(path: str) -> MIMEImage:
    raise NotImplementedError('Code not implmented')


def send_email(to_email: str, subject: str, body: str, image: str | None = None)