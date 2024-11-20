# AWS Lambda Image Resizer

## Overview

The **AWS Lambda Image Resizer** is a serverless application that automatically resizes images uploaded to an S3 bucket. The resized images are saved to a designated output S3 bucket. 

---

## Features

- **Automatic Resizing**: Resizes images to a fixed resolution (e.g., 300x300 pixels).
- **S3 Integration**: Processes images from an input bucket and saves resized images to an output bucket.
- **Customizable Dimensions**: Width and height can be adjusted in the code.

---

## Workflow

1. Upload an image to the input S3 bucket.
2. AWS S3 triggers the Lambda function.
3. Lambda resizes the image.
4. Resized image is saved to the output bucket.

---

## Prerequisites

1. **AWS Account**: With access to Lambda and S3.
2. **Python 3.x Runtime**: The function uses Python with the `Pillow` library.
3. **Input and Output Buckets**: Two S3 buckets for input and output images.
4. **IAM Role**: Permissions for:
   - `s3:GetObject`
   - `s3:PutObject`

---

## Setup Instructions

### Step 1: Prepare the Environment

1. Create a project directory:
   ```bash
   mkdir aws.lambda.image.resizer
   cd aws.lambda.image.resizer
