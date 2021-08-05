terraform {
  backend "s3" {
    bucket         = "yishaitamir-tfstate"
    key            = "yishai"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-lock"
  }
}