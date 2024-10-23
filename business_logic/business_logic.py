import logging

class BusinessLogic:
    def __init__(self, api_client, message_queue):
        self.api_client = api_client
        self.message_queue = message_queue

    def process_data(self):
        data = self.api_client.fetch_data()
        if data:
            try:
                transformed_data = self.transform_data(data)
                self.message_queue.send_message(str(transformed_data))
            except Exception as e:
                logging.error(f"Failed to process and send data: {e}")

    @staticmethod
    def transform_data(data):
        try:
            # Example transformation: Convert title and body to uppercase and add a new field
            transformed_data = []
            for item in data:
                transformed_item = {
                    'userId': item['userId'],
                    'id': item['id'],
                    'title': item['title'].upper(),
                    'body': item['body'].upper(),
                    'processed': True  # New field indicating the item was processed
                }
                transformed_data.append(transformed_item)
            return transformed_data
        except Exception as e:
            logging.error(f"Data transformation failed: {e}")
