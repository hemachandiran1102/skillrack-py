import json
import boto3
database_name = "postgres"
db_cluster_arn = "arn:aws:rds:ap-south-1:666889948617:cluster:test-serveless2"
db_credentials_secrets_store_arn = "arn:aws:secretsmanager:ap-south-1:666889948617:secret:rds!cluster-decb107a-fcc1-4930-8d5f-29133bd84ebc-O2BV7n"
rds_client = boto3.client('rds-data',region_name='ap-south-1')
data_insert = rds_client.execute_statement(
            secretArn=db_credentials_secrets_store_arn,
            database=database_name,
            resourceArn=db_cluster_arn,
            sql=postgres_insert_query, 
            parameters =sql_parameters )