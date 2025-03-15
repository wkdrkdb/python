import smtplib
from  email.mime.text import MIMEText # 이메일 내용을 위한 모듈 
from email.mime.multipart import MIMEMultipart # 이메일 메시지를 위한 모듈 

def send_mail(
        receiver: str,
        subject: str,
        body: str
):
    # 이메일 발신 정보 
    sender = 'gayou20065@gmail.com'
    password = 'wnwl toaw gvzw wiyw'

    # 이메일 구성 
    message = MIMEMultipart()
    message['From'] = sender    # 보내는 사람
    message['To'] = receiver    # 받는 사람
    message['Subject'] = subject    # 이메일 제목
    message.attach(MIMEText(body, 'plain')) # 이메일 본문 내용

    # 이메일 발송
    try:
        print('이메일 발송 중입니다.')
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, receiver, message.as_string())
            print("이메일을 성공적으로 발송하였습니다.")
    except Exception as e:
        print(f"이메일을 발송하는 중에 오류가 발생하였습니다: {e}")
