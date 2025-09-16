provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "example_bucket" {
  bucket = "my-unique-example-bucket-12345"

  tags = {
    Name        = "ExampleBucket"
    Environment = "Dev"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.example_bucket.bucket
}

output "bucket_arn" {
  value = aws_s3_bucket.example_bucket.arn
}