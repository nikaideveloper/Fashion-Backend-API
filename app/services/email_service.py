from fastapi_mail import (
    FastMail,
    MessageSchema,
    ConnectionConfig
)

from app.config import settings


conf = ConnectionConfig(
    MAIL_USERNAME=settings.MAIL_USERNAME,
    MAIL_PASSWORD=settings.MAIL_PASSWORD,
    MAIL_FROM=settings.MAIL_FROM,
    MAIL_SERVER=settings.MAIL_SERVER,
    MAIL_PORT=settings.MAIL_PORT,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)


async def send_reset_email(
    email: str,
    reset_token: str
):

    reset_link = (
        f"{settings.FRONTEND_URL}"
        f"/reset-password?token={reset_token}"
    )

    message = MessageSchema(
        subject="Reset Your Password",
        recipients=[email],
        body=f"""
        <h2>Password Reset</h2>

        <p>Hello,</p>

        <p>You requested to reset your password.</p>

        <p>
            Click the button below to reset your password:
        </p>

        <p>
            <a href="{reset_link}">
                Reset Password
            </a>
        </p>

        <p>This link will expire in 15 minutes.</p>

        <p>If you did not request this, ignore this email.</p>
        """,
        subtype="html"
    )

    fm = FastMail(conf)

    await fm.send_message(message)