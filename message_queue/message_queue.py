import boto3
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError, ClientError

class SQSMessageQueue:
    def __init__(self, aws_access_key_id, aws_secret_access_key, aws_region, queue_name):
        self.sqs = boto3.client('sqs',
                                aws_access_key_id=aws_access_key_id,
                                aws_secret_access_key=aws_secret_access_key,
                                region_name=aws_region)
        self.queue_url = self.get_queue_url(queue_name)

    def get_queue_url(self, queue_name):
        try:
            response = self.sqs.get_queue_url(QueueName=queue_name)
            return response['QueueUrl']
        except (NoCredentialsError, PartialCredentialsError, ClientError) as e:
            logging.error(f"Failed to get queue URL: {e}")
            return None

    def send_message(self, message_body):
        try:
            response = self.sqs.send_message(
                QueueUrl=self.queue_url,
                MessageBody=message_body
            )
        except Exception as e:
            logging.error(f"Failed to send message: {e}")

    def receive_message(self):
        try:
            response = self.sqs.receive_message(
                QueueUrl=self.queue_url,
                MaxNumberOfMessages=1,
                WaitTimeSeconds=10
            )
            messages = response.get('Messages', [])
            if messages:
                return messages[0]['Body']
            return None
        except Exception as e:
            logging.error(f"Failed to receive message: {e}")
            return None
