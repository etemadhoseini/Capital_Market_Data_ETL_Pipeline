
# Capital Market ETL Pipeline

This repository contains a robust Python-based ETL (Extract, Transform, Load) pipeline designed to process capital market data. The project leverages AWS S3 for storage, implements clean coding practices, and adheres to software development principles such as object-oriented programming and comprehensive testing.

## Project Overview

The Capital Market ETL Pipeline automates the process of extracting data from various sources, transforming it into a usable format, and loading it into a target system. It uses modern tools and methodologies to ensure efficient data processing and management.

## Table of Contents

- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Technologies and Tools](#technologies-and-tools)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Key Features

- **Data Extraction**: Fetches source data from AWS S3 and validates it using Jupyter Notebook.
- **Data Transformation**: Implements both functional and object-oriented programming techniques for data processing.
- **Data Loading**: Efficiently loads processed data into the target S3 bucket.
- **Meta Data Management**: Maintains a meta file to track processed data dates.
- **Logging**: Comprehensive logging throughout the process for traceability and debugging.
- **Testing**: Includes unit and integration tests to ensure reliability and maintainability.
- **Containerization**: Docker is utilized for packaging and deploying the application in a controlled environment.

## Technologies and Tools

- **Python**: Main programming language for building the ETL pipeline.
- **Pandas**: Data manipulation and analysis library.
- **Boto3**: AWS SDK for Python to interact with S3.
- **PyArrow**: For handling Parquet file formats.
- **Pipenv**: Dependency management tool.
- **Docker**: Containerization technology.
- **Jupyter Notebook**: For data exploration and analysis.
- **Moto**: Library for mocking AWS services in tests.

## Project Structure

```
.
├── capital_market
│   └── configs
│       └── capital_market_etl_config.yml
│   ├── common
│   │   ├── constants.py
│   │   ├── custom_exceptions.py
│   │   ├── s3.py
│   │   └── meta_process.py
│   └── transformers
│       └── capital_market_transformer.py
├── tests
│   ├── common
│   │   ├── test_meta_process.py
│   │   ├── test_s3.py
│   ├── integration_test
│   │   ├── test_int_capital_market_transformer.py
│   └── transformers
│       └── test_capital_market_transformer.py
├── Dockerfile
├── Pipfile
├── Pipfile.lock
└── run.py
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/etemadhoseini/Capital_Market_Data_ETL_Pipeline.git
   cd Capital_Market_Data_ETL_Pipeline
   ```

2. Build the Docker image:
   ```bash
   docker build -t capital_market_etl .
   ```

3. Install the necessary packages using Pipenv:
   ```bash
   pipenv install
   ```

## Usage

To run the Capital Market ETL job, use the following command, replacing `capital_market_etl_config.yml` with your configuration file:

```bash
python run.py capital_market_etl_config.yml
```

### Configuration

The `capital_market_etl_config.yml` file contains configurations for:

- **S3**: AWS access keys, bucket names, and endpoints.
- **Source**: Source data extraction settings.
- **Target**: Target data loading settings.
- **Meta**: Meta file management settings.
- **Logging**: Logging configuration.

### Example Configuration

Here’s a snippet of the `capital_market_etl_config.yml` file:

```yaml
s3:
  access_key: 'YOUR_ACCESS_KEY'
  secret_key: 'YOUR_SECRET_KEY'
  src_endpoint_url: 'https://s3.eu-north-1.amazonaws.com'
  src_bucket: 'capital-market-data'
  trg_endpoint_url: 'https://s3.eu-north-1.amazonaws.com'
  trg_bucket: 'capital-market-report'

source:
  src_first_extract_date: '2022-12-25'
  src_columns: ['ISIN', 'Mnemonic', 'Date', 'Time', 'StartPrice', 'EndPrice', 'MinPrice', 'MaxPrice', 'TradedVolume']
```

## Testing

The project includes unit tests and integration tests using the `unittest` framework. To run the tests, you can execute:

```bash
pytest tests/
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](assets\LICENCE) file for more details.

## Contact

For any inquiries, please reach out to:

- **Amir Hosein Etemad Hoseini**: [etemadhoseini@gmail.com](mailto:etemadhoseini@gmail.com)
- **LinkedIn**: [Etemad Hoseini](https://www.linkedin.com/in/etemadhoseini/)

---

**Happy coding! 🎉**
