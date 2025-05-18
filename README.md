# Scrapy Project with Docker

This repository contains a Scrapy project set up with Docker and Docker Compose for a containerized Python environment.

## Project Structure

```
.
├── docker-compose.yml
└── scraper/
    ├── docker/
    │   └── Dockerfile
    ├── requirements.txt
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

   By default, the container will run with the same user ID and group ID as your host user to avoid permission issues.
   If you need to specify different IDs, you can do so by setting the `UID` and `GID` environment variables:
   ```
   UID=$(id -u) GID=$(id -g) docker-compose up -d
   ```

3. Access the container shell:
   ```
   docker-compose exec scraper bash
   ```

4. Run the example spider:
   ```
   ./entry.py
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
./entry.py
```

By default, the entry.py script is now configured to run the LinkFollowerSpider, which crawls a website by following all
links. You can also run the original example spider by specifying it:

```
./entry.py --spider=example
```

### Using the LinkFollowerSpider

The LinkFollowerSpider is designed to crawl websites by extracting all `<a>` tags and following their links. It has the
following features:

- Extracts all links from each page
- Follows links to crawl through all pages of the site
- Limits crawl depth to prevent infinite crawling
- Filters out duplicate URLs
- Avoids following fragment links (#) and javascript links

You can customize the spider's behavior using command-line arguments:

```
# Run with custom start URL and allowed domain
./entry.py --start-urls=https://example.org --allowed-domains=example.org

# Run with custom depth limit
./entry.py --settings=DEPTH_LIMIT=5

# Run the example spider instead
./entry.py --spider=example

# Export data to a file
./entry.py -o output.json -t json
```

### Available Command-Line Options

The entry.py script supports the following command-line options:

- `--spider`: Spider to run (default: link_follower)
- `--start-urls`: Comma-separated list of start URLs
- `--allowed-domains`: Comma-separated list of allowed domains
- `--settings`: Additional settings in the format NAME=VALUE (can be used multiple times)
- `-o, --output`: Output file (e.g., output.json)
- `-t, --output-format`: Output format (e.g., json, csv, xml)

You can also modify the entry.py file directly to customize the spider's behavior:

```python
# In entry.py
run_spider(
   start_urls=["https://example.org"],
   allowed_domains=["example.org"],
   custom_settings={'DEPTH_LIMIT': 5}
)
```

## Exporting Data

To export data to a file when using the entry.py script, you'll need to modify the script to include output options.
Alternatively, you can still use the traditional Scrapy command with the `-o` option:

```
scrapy crawl example -o output.json
```

Supported formats include JSON, CSV, XML, and more.

## Customizing the Project

- Edit `scraper/scraper/settings.py` to configure Scrapy settings
- Create item classes in `scraper/scraper/items.py`
- Implement item pipelines in `scraper/scraper/pipelines.py`
- Add middleware in `scraper/scraper/middlewares.py`
