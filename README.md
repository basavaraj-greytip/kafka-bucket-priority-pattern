# Kafka bucket priority pattern

This repo contains implementation of a bucket priority pattern for prioritizing Kafka messages using Python3.

## Project Structure

The architecture of the project is microservices, namely producers and consumers:

```
├── consuming
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── src
│       ├── stoppable_thread.py
│       ├── message_processing_thread.py
│       └── consumer_thread.py
├── producing
│   ├── main.py
│   ├── config.py
│   ├── requirements.txt
│   ├── Dockerfile
│   └── src
│       ├── stoppable_thread.py
│       ├── message_creating_thread.py
│       └── producer_thread.py
├── docker
│   └── templates.yaml
├── docker-compose-pub-sub.yaml
├── docker-compose.yaml
├── README.md
└── setup_topics.sh
```

A diagram of what the pattern architecture looks like is as follows:

![kafka-bucket-priority drawio](https://user-images.githubusercontent.com/93226646/234657271-f550b2db-dafe-4d2d-9780-4f7530d06165.png)


## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

+ You have a [Ubuntu](https://ubuntu.com/) machine.
+ [Docker](https://docs.docker.com/desktop/install/linux-install/) is installed on your machine.


### Installation

1. Copy repo to your machine and go to the root directory:
   ```bash
   git clone https://github.com/Kyrylo-Ktl/kafka-bucket-priority-pattern && \
   cd kafka-bucket-priority-pattern
   ```

2. Create an environment variables file from example:
   ```bash
   mv .env.example .env
   ```

### Run

1. To get started, start the kafka cluster using the following command:
    ```bash
    docker compose up --build
    ```

2. After that create topics using `setup_topics.sh` script:
   ```bash
   bash setup_topics.sh
   ```

3. And finally start the cluster of producers and consumers:
   ```bash
   docker compose -f docker-compose-pub-sub.yaml up --build
   ```
