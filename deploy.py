import os
import mimetypes
import boto3
from botocore.exceptions import ClientError

# ============================================================
# AWS CONFIGURATION
# ============================================================

AWS_REGION = "ap-south-1"

BUCKET_NAME = "yashodhan-boto3-website-141538081684-826"

WEBSITE_FOLDER = "website"


# ============================================================
# CREATE S3 CLIENT
# ============================================================

s3 = boto3.client(
    "s3",
    region_name=AWS_REGION
)


# ============================================================
# CREATE S3 BUCKET
# ============================================================

def create_bucket():
    print("\n[1] Creating S3 bucket...")

    try:
        if AWS_REGION == "us-east-1":
            s3.create_bucket(
                Bucket=BUCKET_NAME
            )
        else:
            s3.create_bucket(
                Bucket=BUCKET_NAME,
                CreateBucketConfiguration={
                    "LocationConstraint": AWS_REGION
                }
            )

        print(f"SUCCESS: Bucket '{BUCKET_NAME}' created.")

    except ClientError as e:
        error_code = e.response["Error"]["Code"]

        if error_code in ["BucketAlreadyOwnedByYou"]:
            print(f"Bucket already exists and belongs to you: {BUCKET_NAME}")

        elif error_code in ["BucketAlreadyExists"]:
            print("ERROR: Bucket name is already used by another AWS account.")
            print("Change BUCKET_NAME in deploy.py and run again.")
            raise

        else:
            print("ERROR while creating bucket:")
            print(e)
            raise


# ============================================================
# CONFIGURE STATIC WEBSITE
# ============================================================

def configure_website():

    print("\n[2] Configuring S3 static website hosting...")

    try:
        s3.put_bucket_website(
            Bucket=BUCKET_NAME,
            WebsiteConfiguration={
                "IndexDocument": {
                    "Suffix": "index.html"
                }
            }
        )

        print("SUCCESS: Static website hosting configured.")

    except ClientError as e:
        print("ERROR while configuring website:")
        print(e)
        raise


# ============================================================
# DISABLE BLOCK PUBLIC ACCESS
# ============================================================

def configure_public_access():

    print("\n[3] Configuring public access settings...")

    try:
        s3.put_public_access_block(
            Bucket=BUCKET_NAME,
            PublicAccessBlockConfiguration={
                "BlockPublicAcls": False,
                "IgnorePublicAcls": False,
                "BlockPublicPolicy": False,
                "RestrictPublicBuckets": False
            }
        )

        print("SUCCESS: Public access block settings updated.")

    except ClientError as e:
        print("ERROR while configuring public access:")
        print(e)
        raise


# ============================================================
# CREATE BUCKET POLICY
# ============================================================

def create_bucket_policy():

    print("\n[4] Creating bucket policy...")

    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadForWebsite",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{BUCKET_NAME}/*"
            }
        ]
    }

    import json

    try:
        s3.put_bucket_policy(
            Bucket=BUCKET_NAME,
            Policy=json.dumps(policy)
        )

        print("SUCCESS: Bucket policy created.")

    except ClientError as e:
        print("ERROR while creating bucket policy:")
        print(e)
        raise


# ============================================================
# UPLOAD WEBSITE FILES
# ============================================================

def upload_website():

    print("\n[5] Uploading website files...")

    for root, directories, files in os.walk(WEBSITE_FOLDER):

        for filename in files:

            local_path = os.path.join(
                root,
                filename
            )

            relative_path = os.path.relpath(
                local_path,
                WEBSITE_FOLDER
            )

            s3_key = relative_path.replace("\\", "/")

            content_type, _ = mimetypes.guess_type(
                local_path
            )

            if content_type is None:
                content_type = "application/octet-stream"

            print(f"Uploading: {s3_key}")

            try:

                s3.upload_file(
                    local_path,
                    BUCKET_NAME,
                    s3_key,
                    ExtraArgs={
                        "ContentType": content_type
                    }
                )

                print(f"Uploaded successfully: {s3_key}")

            except ClientError as e:

                print(
                    f"ERROR uploading {s3_key}: {e}"
                )

                raise

    print("SUCCESS: All website files uploaded.")


# ============================================================
# DISPLAY WEBSITE INFORMATION
# ============================================================

def display_website_info():

    website_endpoint = (
        f"http://{BUCKET_NAME}.s3-website-"
        f"{AWS_REGION}.amazonaws.com"
    )

    print("\n" + "=" * 60)
    print("DEPLOYMENT COMPLETED SUCCESSFULLY")
    print("=" * 60)

    print(f"\nS3 Bucket:")
    print(BUCKET_NAME)

    print(f"\nAWS Region:")
    print(AWS_REGION)

    print("\nWebsite URL:")
    print(website_endpoint)

    print("\nOpen this URL in your browser.")
    print("=" * 60)


# ============================================================
# MAIN PROGRAM
# ============================================================

def main():

    print("\n")
    print("=" * 60)
    print(" AUTOMATED S3 STATIC WEBSITE DEPLOYMENT")
    print(" Python + boto3 + Amazon S3")
    print("=" * 60)

    create_bucket()

    configure_website()

    configure_public_access()

    create_bucket_policy()

    upload_website()

    display_website_info()


if __name__ == "__main__":
    main()