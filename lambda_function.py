import boto3
from PIL import Image
import io
import os

s3 = boto3.client("s3")

def resize_image(image_data, width, height):
    with Image.open(io.BytesIO(image_data)) as img:
        img = img.convert("RGB")
        img = img.resize((width, height))
        buffer = io.BytesIO()
        img.save(buffer, "JPEG")
        buffer.seek(0)
        return buffer

def lambda_handler(event, context):
    try:
        # Log the event
        print("Event received:", event)

        for record in event["Records"]:
            bucket_name = record["s3"]["bucket"]["name"]
            object_key = record["s3"]["object"]["key"]

            # Download the image from S3
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            image_data = response["Body"].read()

            # Resize the image
            resized_image = resize_image(image_data, width=300, height=300)

            # Define the output bucket and key
            output_bucket = os.environ.get("OUTPUT_BUCKET")
            output_key = f"resized-{object_key}"

            # Upload the resized image
            s3.put_object(
                Bucket=output_bucket,
                Key=output_key,
                Body=resized_image,
                ContentType="image/jpeg"
            )

            print(f"Resized image uploaded to {output_bucket}/{output_key}")

        return {
            "statusCode": 200,
            "body": "Image resizing completed successfully."
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            "statusCode": 500,
            "body": f"Error resizing image: {str(e)}"
        }
