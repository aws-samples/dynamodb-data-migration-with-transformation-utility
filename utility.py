import json
import boto3
from multiprocessing import Pool
import datetime
from os import listdir, makedirs
from os.path import isfile, join, exists
import time

st = datetime.datetime.now()

print(st)

region = "ap-south-1"
target_table = "parts"
files_path = "<PATH-TO-UNZIPPED-DATA-FILES>"
output_dir = "<OUTPUT-FOLDER-FOR_RESUME>"
back_off = 2  # seconds - back off time for retry

client = boto3.client('dynamodb', region_name=region)
NUM_PROCESSES = 5  # alter this based on the number of parallel threads you want to run
batch_size = 25  # no of items to write in a single batch, max 25


def modify_rec(record):
    record = json.loads(record)
    # comment next 4 files and add your own transformation
    val = record['Item']['fa_partition_key']['S']
    record['Item']['fa_partition_key']['S'] = f'p_{val}'
    record['Item']['sk'] = {}
    record['Item']['sk']['S'] = record['Item']['fa_sort_key']['S']
    return {'PutRequest': record}


def parallel_modify(batches, num_processes=NUM_PROCESSES):
    with Pool(processes=num_processes) as pool:
        results = pool.map(modify_rec, batches)
    return results


def batch_json(json_array, batch_size=25):
    batches = []
    batch = []
    for item in json_array:
        batch.append(item)
        if len(batch) == batch_size:
            batches.append(batch)
            batch = []
    # Add the remaining items to the last batch (if any)
    if batch:
        batches.append(batch)
    return batches


def batch_write_items(data_chunk):
    resp = client.batch_write_item(RequestItems={target_table: data_chunk})
    if target_table in resp['UnprocessedItems']:
        return resp['UnprocessedItems'][target_table]
    else:
        return 0


def parallel_process(batches, num_processes=NUM_PROCESSES):
    with Pool(processes=num_processes) as pool:
        results = pool.map(batch_write_items, batches)
    return results


def retry_mechanism(recs):
    batches = batch_json(recs, batch_size)
    unfunished = []
    for batch in batches:
        resp = batch_write_items(batch)
        if resp != 0:
            unfunished.extend(resp)
    return unfunished


def create_or_update_resume(file_name):
    with open(f"{output_dir}/resume.txt", "a") as file:
        file.write(file_name + "\n")


def main():
    isExist = exists(output_dir)
    if not isExist:
        # Create a new directory because it does not exist
        makedirs(output_dir)
        print("The new directory is created!")
        files = []
    else:
        with open(f"{output_dir}/resume.txt", "r") as file:
            files = [line.strip() for line in file]
            print("Previously completed files : ",files)
    try:
        onlyfiles = [f"{files_path}/{f}" for f in listdir(files_path) if isfile(join(files_path, f))]
        setResume = set(files)
        setAll = set(onlyfiles)
        resume_jobs = setAll.difference(setResume)
        dat = []
        for file in resume_jobs:
            with open(file, "rb") as fp:
                dat.extend(fp.readlines())
            print("No of records in {} : {}".format(file, len(dat)))
            cl_data = parallel_modify(dat)
            batches = batch_json(cl_data, batch_size)
            sk = parallel_process(batches)
            unfinised_records = [rec[0] for rec in sk if rec != 0]
            print("No of failed records: ", len(unfinised_records))
            unfinished = retry_mechanism(unfinised_records)
            cnt = 1
            while len(unfinished) != 0:
                unfinished = retry_mechanism(unfinished)
                print(f"Found unfinished records: {len(unfinished)}")
                time.sleep(cnt * back_off)
                cnt += 1
                if cnt > 30:
                    cnt = 1
            create_or_update_resume(file)
            print("committed file:", file)
        print(datetime.datetime.now())
        print(datetime.datetime.now() - st)
    except Exception as e:
        print(e)
        # send notification


main()
