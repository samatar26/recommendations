terraform {
  backend "s3" {
    bucket = "samatar-tf-state"
    key    = "samatar_tf_state.tfstate"
    region = "us-east-1"
  }
}
