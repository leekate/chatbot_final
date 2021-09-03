"""
자신 RDS 설정 값.
"""
DB_HOST = 'database-chatbot.cbzpe1fkga6u.ap-northeast-2.rds.amazonaws.com'
DB_USER = 'admin'
DB_PASSWORD = 'dlsvlslxm66'
DB_NAME = 'chatbotDB'
DB_PORT = 3306

def DatabaseConfig():
    global DB_HOST, DB_USER, DB_PASSWORD, DB_NAME, DB_PORT