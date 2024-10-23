# Define the Docker image name
IMAGE_NAME = my_app

# Build the Docker image
.PHONY: build
build:
	docker build -t $(IMAGE_NAME) .

# Run the Docker container
.PHONY: run
run:
	docker run -e API_URL=https://jsonplaceholder.typicode.com/posts \
			-e SQS_QUEUE_NAME=queue-name \
			-e AWS_ACCESS_KEY_ID=ACCESS_ID \
			-e AWS_SECRET_ACCESS_KEY=SECRET_ACC_KEY \
			-e AWS_REGION=sqs-region $(IMAGE_NAME)

# Run tests
.PHONY: test
test:
	python -m unittest discover -s tests
