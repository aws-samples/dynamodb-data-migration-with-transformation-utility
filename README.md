# Private Application with Custom Domain Name

This utility helps in migrating dynamodb table data from one table to another with transformations. This utility script needs to be executed in an EC2 instance (preferably memory intensive)

## Components
1. Ability to migrate data to a new table (same region, cross region)
2. Add transformation during migration
3. Resume capability at file level

## Deployment
1. Spin an EC2 instance in target region
2. unzip all the DynamoDB Json files in the EC2 instance within a directory
3. run the script

### Prerequisites

dependent python library installation -- requirements.txt

### Steps
1. unzip *.gz
2. 


### Clean Up

Delete the CloudFormation stack on AWS console. The default stack name is **PrivateWebApp**. Also, there are two Amazon S3 buckets (for static website and access log) retained with names beginning with **privatewebapp**. You can delete them manually.

## Limitations

- There is a 10 MB limit for static files served by API Gateway. Refer to [API Gateway quotas for configuring and running a REST API](https://docs.aws.amazon.com/apigateway/latest/developerguide/limits.html#api-gateway-execution-service-limits-table) for the maximum payload size of API Gateway.

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
