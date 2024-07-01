# dynamodb data migration with transformation utility
This utility helps in migrating dynamodb table data from one table to another with transformations. This utility script needs to be executed in an EC2 instance (preferably memory intensive)

## functions
1. Ability to migrate data to a new table (same region, cross region)
2. Add transformation during migration
3. Resume capability at file level

## Deployment
1. Spin an EC2 instance in target region
2. unzip all the DynamoDB Json files in the EC2 instance within a directory
3. run the script


### Steps
1. copy all the Dynamodb Json files to Ec2 local volume
2. unzip *.gz in a single directory
3. Execute the script , Usage: python3 utility.py


### Clean Up

Delete the EC2 instance once the record count matches post migration

## Limitations

- This utility can resume at a file level and not at a record level, make sure in execptions you have the capability to handle this

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
