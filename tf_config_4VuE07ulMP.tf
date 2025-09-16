# Terraform configuration to create an AWS S3 bucket

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.0"
    }
  }
}

provider "aws" {
  region = "us-west-2"
}

resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = "my-unique-example-bucket-${random_id.bucket_suffix.hex}"

  tags = {
    Name        = "ExampleBucket"
    Environment = "Development"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.example_bucket.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.example_bucket.arn
}