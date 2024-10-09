"""Running the Capital Market ETL application"""
import argparse
import logging
import logging.config

import yaml

from capital_market.common.s3 import S3BucketConnector
from capital_market.transformers.capital_market_transformer import CapitalMarketETL, CapitalMarketSourceConfig, CapitalMarketTargetConfig


def main():
    """
      entry point to run the capital market ETL job
    """
    # Parsing YAML file
    parser = argparse.ArgumentParser(description='Run the Capital Market ETL job.')
    parser.add_argument('config', help='A configuration file in YAML format.')
    args = parser.parse_args()
    config = yaml.safe_load(open(args.config))

    # configure logging
    log_config = config['logging']
    logging.config.dictConfig(log_config)
    logger = logging.getLogger(__name__)
    # reading s3 configuration
    s3_config = config['s3']
    # creating the S3BucketConnector class instances for source and target
    s3_bucket_src = S3BucketConnector(access_key=s3_config['access_key'],
                                      secret_key=s3_config['secret_key'],
                                      endpoint_url=s3_config['src_endpoint_url'],
                                      bucket=s3_config['src_bucket'])
    s3_bucket_trg = S3BucketConnector(access_key=s3_config['access_key'],
                                      secret_key=s3_config['secret_key'],
                                      endpoint_url=s3_config['trg_endpoint_url'],
                                      bucket=s3_config['trg_bucket'])
    # reading source configuration
    source_config = CapitalMarketSourceConfig(**config['source'])
    # reading target configuration
    target_config = CapitalMarketTargetConfig(**config['target'])
    # reading meta file configuration
    meta_config = config['meta']
    # creating CapitalMarketETL class instance
    logger.info('Capital Market ETL job started')
    capital_market_etl = CapitalMarketETL(s3_bucket_src, s3_bucket_trg,
                         meta_config['meta_key'], source_config, target_config)
    # running etl job for capital market report
    capital_market_etl.etl_report()
    logger.info('Capital Market ETL job finished.')


if __name__ == '__main__':
    main()