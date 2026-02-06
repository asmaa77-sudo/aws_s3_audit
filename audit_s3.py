import boto3

s3 = boto3.client('s3')

response = s3.list_buckets()

for bucket in response['Buckets']:
    name = bucket['Name']
    print(f"\nAuditing bucket: {name}")

    try:
        s3.get_public_access_block(Bucket=name)
        print("Public access block: ENABLED")
    except:
        print("Public access block: NOT enabled")

    try:
        s3.get_bucket_encryption(Bucket=name)
        print("Encryption: ENABLED")
    except:
        print("Encryption: NOT enabled")

    versioning = s3.get_bucket_versioning(Bucket=name)
    print("Versioning:", versioning.get("Status", "Disabled"))
