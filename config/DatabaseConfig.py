"""
자신 RDS 설정 값.
"""
DB_HOST = 'database-chatbot.cw2yedyk3t2l.ap-northeast-2.rds.amazonaws.com'
DB_USER = 'admin'
DB_PASSWORD = '**********'
DB_NAME = 'chatbotdb'
DB_PORT = 3306

def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT