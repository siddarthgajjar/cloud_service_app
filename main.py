import logging
from api_client.api_client import APIClient
from message_queue.message_queue import SQSMessageQueue
from business_logic.business_logic import BusinessLogic
from config.config import get_config

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

def main():
    setup_logging()



    config = get_config()
    api_client = APIClient(config['API_URL'])
    message_queue = SQSMessageQueue(config['AWS_ACCESS_KEY_ID'],
                                    config['AWS_SECRET_ACCESS_KEY'],
                                    config['AWS_REGION'],
                                    config['SQS_QUEUE_NAME'])
    business_logic = BusinessLogic(api_client, message_queue)
    business_logic.process_data()

if __name__ == "__main__":
    main()
