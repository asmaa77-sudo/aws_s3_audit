# AWS S3 Security Audit Tool

## Overview
A Python-based tool that audits AWS S3 buckets for common security
misconfigurations.

## Why This Project Matters
Public or misconfigured S3 buckets are a major cause of data breaches.
This project helps identify security risks automatically.

## Features
- Checks public access block settings
- Verifies server-side encryption
- Confirms versioning status

## Tech Stack
- Python
- AWS SDK (Boto3)
- AWS S3
- AWS IAM

## How It Works (Step-by-Step)
1. Connects to AWS using IAM credentials
2. Retrieves all S3 buckets
3. Audits each bucket’s security settings
4. Displays results in the terminal

## Setup & Usage
```bash
pip install boto3
python s3_audit.py
