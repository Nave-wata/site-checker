# Scrapy Project with Docker

This repository contains a Scrapy project set up with Docker and Docker Compose for a containerized Python environment.

## Project Structure

```
.
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── scraper/
    ├── scrapy.cfg
    └── scraper/
        ├── __init__.py
        ├── items.py
        ├── middlewares.py
        ├── pipelines.py
        ├── settings.py
        └── spiders/
            ├── __init__.py
            └── example_spider.py
```

## Requirements

- Docker
- Docker Compose

## Getting Started

1. Clone this repository:
   ```
   git clone <repository-url>
   cd <repository-directory>
   ```

2. Build and start the Docker container:
   ```
   docker-compose up -d
   ```

3. Access the container shell:
   ```
   docker-compose exec scraper bash
   ```

4. Run the example spider:
   ```
   scrapy crawl example
   ```

Alternatively, you can uncomment the command line in `docker-compose.yml` to run the spider directly when starting the container.

## Creating a New Spider

1. Access the container shell:
   ```
   docker-compose exec scraper bash
   ```

2. Create a new spider:
   ```
   scrapy genspider <spider-name> <domain>
   ```

3. Edit the spider file in `scraper/scraper/spiders/<spider-name>.py`

## Running Spiders

```
scrapy crawl <spider-name>
```

## Exporting Data

To export data to a file, use the `-o` option:

```
scrapy crawl <spider-name> -o output.json
```

Supported formats include JSON, CSV, XML, and more.

## Customizing the Project

- Edit `scraper/scraper/settings.py` to configure Scrapy settings
- Create item classes in `scraper/scraper/items.py`
- Implement item pipelines in `scraper/scraper/pipelines.py`
- Add middleware in `scraper/scraper/middlewares.py`
