# Backend Service Simulation

This project simulates a backend service running as an agent on the cloud. It is designed to scale horizontally and vertically, ensuring robustness, modularity, and high code quality. The application interacts with an external API, processes the data, and queues the result using Amazon SQS.

## Design and Key Components

1. **API Client Module**:
   - `APIClient` class fetches data from an external API using HTTP requests.
   - Simulated interaction with external systems, using placeholder data for testing.

2. **Message Queue Module**:
   - `SQSMessageQueue` class interacts with Amazon SQS.
   - Sends and receives messages to/from a queue.

3. **Business Logic Module**:
   - `BusinessLogic` class processes the fetched data, transforming it before queuing.
   - Handles the main application logic, ensuring scalability and data integrity.

4. **Configuration and Dependency Injection**:
   - Uses environment variables for configuration.
   - Facilitates easy swapping of components and configurations for testing and scaling.

5. **Error Handling and Logging**:
   - Comprehensive error handling across modules.
   - Logging implemented using Python's built-in `logging` module to track operations and errors.

## Scalability Considerations

- **Horizontal Scaling**: Designed to run multiple instances without data conflicts, using Amazon SQS to handle message passing.
- **Vertical Scaling**: Can allocate more resources to handle increased load.
- **Concurrency Control**: SQS manages concurrent access to the queue, preventing race conditions.
- **Modular Architecture**: Clear separation of concerns ensures that each component can be independently scaled and maintained.

## How to Run the Program in a Cloud Environment

### Prerequisites

- Docker installed on your system.
- AWS credentials with appropriate permissions to access SQS.

### Steps to Run

1. **Environment Variables**:
Set the following environment variables for running the application:

- `API_URL`: The URL of the external API.

- `SQS_QUEUE_NAME`: The name of the Amazon SQS queue.

- `AWS_ACCESS_KEY_ID`: AWS access key ID.

- `AWS_SECRET_ACCESS_KEY`: AWS secret access key.

- `AWS_REGION`: The AWS region of SQS queue.

2. **Build the Docker Image**:
  ```shell-script
   make build
  ```
3. **Run the Docker Container**:
  ```shell-script
  make run
  ```

4. **Running Tests**:

  ```shell-script
  make test
  ```


