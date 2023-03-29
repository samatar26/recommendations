resource "aws_s3_bucket" "terraform_state" {
  bucket = "samatar-tf-state"



}

resource "aws_s3_bucket_versioning" "samatar_tf_state_versioning" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}
