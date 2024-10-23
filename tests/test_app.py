import unittest
from unittest.mock import Mock, patch
from api_client.api_client import APIClient
from message_queue.message_queue import SQSMessageQueue
from business_logic.business_logic import BusinessLogic
from config.config import get_config

class TestBusinessLogic(unittest.TestCase):
    def setUp(self):
        # Mock API client and SQS client
        self.mock_api_client = Mock(spec=APIClient)
        self.mock_sqs_client = Mock(spec=SQSMessageQueue)
        
        # Instantiate BusinessLogic with mocked dependencies
        self.business_logic = BusinessLogic(self.mock_api_client, self.mock_sqs_client)

    @patch('boto3.client')  # Patch boto3.client to prevent real AWS calls
    def test_process_data(self, mock_boto3_client):
        # Mock the API client to return some sample data
        self.mock_api_client.fetch_data.return_value = [
            {
                "userId": 1,
                "id": 1,
                "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
                "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
            }
        ]
        mock_boto3_client.return_value = self.mock_sqs_client

        # Call the method under test
        self.business_logic.process_data()

        # Expected transformed data (as a string, since it's sent as string to SQS)
        expected_message = str([
            {
                'userId': 1,
                'id': 1,
                'title': 'SUNT AUT FACERE REPELLAT PROVIDENT OCCAECATI EXCEPTURI OPTIO REPREHENDERIT',
                'body': 'QUIA ET SUSCIPIT\nSUSCIPIT RECUSANDAE CONSEQUUNTUR EXPEDITA ET CUM\nREPREHENDERIT MOLESTIAE UT UT QUAS TOTAM\nNOSTRUM RERUM EST AUTEM SUNT REM EVENIET ARCHITECTO',
                'processed': True
            }
        ])

        # Verify that send_message was called with the correct, stringified data
        self.mock_sqs_client.send_message.assert_called_once_with(expected_message)

if __name__ == '__main__':
    unittest.main()
