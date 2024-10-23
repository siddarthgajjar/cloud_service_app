import os

def get_config():
    return {
        'API_URL': os.getenv('API_URL', 'https://jsonplaceholder.typicode.com/posts'),
        'SQS_QUEUE_NAME': os.getenv('SQS_QUEUE_NAME', ''),
        'AWS_ACCESS_KEY_ID': os.getenv('AWS_ACCESS_KEY_ID', ''),
        'AWS_SECRET_ACCESS_KEY': os.getenv('AWS_SECRET_ACCESS_KEY', ''),
        'AWS_REGION': os.getenv('AWS_REGION', '')
    }
