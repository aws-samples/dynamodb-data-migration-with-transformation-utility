# dynamodb data migration with transformation utility
This utility presents a cost-effective approach in migrating dynamodb table data from one table to another with transformations. While there are ways to achieve this via [Glue]([https://link-url-here.org](https://aws.amazon.com/blogs/big-data/accelerate-amazon-dynamodb-data-access-in-aws-glue-jobs-using-the-new-aws-glue-dynamodb-elt-connector/)), this utility would be useful if the end user does not have glue knowledge or if the JSON structure is nested and of high complexity. 

This utility script needs to be executed in an EC2 instance (preferably memory intensive)

## Functions
1. Ability to migrate data to a new table (same region, cross region)
2. Add transformation during migration
3. Resume capability at file level

## Deployment
1. Spin an EC2 instance in target region
2. unzip all the DynamoDB Json files in the EC2 instance within a directory
3. run the script


### Steps
1. Export Dynamodb table in JSON format.  
2. copy all the Dynamodb Json files to Ec2 local volume
3. unzip *.gz in a single directory
4. edit utility.py file and change the parameters, eg: Dynamodb table name, no of threads
5. Execute the script , Usage: python3 utility.py


### Clean Up

Delete the EC2 instance once the record count matches post migration

## Limitations

- This utility can resume at a file level and not at a record level, make sure in execptions you have the capability to handle this

## Security

See [CONTRIBUTING](CONTRIBUTING.md#security-issue-notifications) for more information.

## License

This library is licensed under the MIT-0 License. See the LICENSE file.
