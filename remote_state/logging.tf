
resource "aws_s3_bucket" "logging" {
  bucket = "yishaitamir-logging"

  versioning {
    enabled = true
  }

  lifecycle {
    prevent_destroy = true
  }
}