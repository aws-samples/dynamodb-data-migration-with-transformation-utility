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

Delete the EC2 instance once the record count matches post migration

## Limitations

- This utility can resume at a file level and not at a record level, make sure in execptions you have the capability to handle this

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
