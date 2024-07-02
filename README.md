# Motionelements_parser


Motionelements_parser is a Python asyncio-based script for fetching and parsing data from the MotionElements website. It retrieves video metadata including URLs for thumbnails and webm format videos based on user-defined search queries.

## Features

- Asynchronous fetching of data using aiohttp for efficient network operations.
- JSON parsing to extract video metadata such as URLs for thumbnails and webm videos.
- Error handling for HTTP errors and missing data fields.
- Modular structure separating configuration `(headers.py)`, main execution `(main.py)`, and data processing `(parser.py)`.


## Prerequisites
Before running Motionelements_parser, ensure you have Python 3.7 or higher installed.


## Installation

1. **Clone the repository from GitHub:**
    ```bash
    git clone https://github.com/your-username/MotionElements_parser.git
    cd Motionelements_parser

2. **Install the required dependencies using pip:**
    ```bash
    pip install -r requirements.txt


## Configuration
Ensure your headers.py file contains the necessary headers and cookies required for accessing the MotionElements API.

## Usage
Run main.py with Python to execute the script. Provide a search query and number of pages to fetch:

    python main.py


*Follow the prompts to enter the search query and number of pages. The script will fetch data from MotionElements, parse the JSON response, and print URLs for thumbnails and webm videos.*

**Example:**

    Enter key-word: 'smile'

**Output:**

    https://v.motionelements.com/v/31505/31495020_a-01.mp4
    ...
