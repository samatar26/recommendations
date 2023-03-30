data "aws_ami" "t2_2xlarge" {
  most_recent = true

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-ebs"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }

  filter {
    name   = "architecture"
    values = ["x86_64"]
  }

  owners = ["amazon"]
}

resource "aws_instance" "recommendations" {
  ami           = data.aws_ami.t2_2xlarge.id
  instance_type = "t2.2xlarge"
}
