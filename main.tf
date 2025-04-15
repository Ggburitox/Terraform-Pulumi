provider "aws" {
  region = "us-east-1"
}

resource "aws_instance" "MC-Terraform" {
  ami           = "ami-022ce79dc9cabea0c"
  instance_type = "t2.micro"
  key_name      = "vockey"

  root_block_device {
    volume_size = 20
  }

  vpc_security_group_ids = [aws_security_group.vm_sg.id]

  tags = {
    Name = "MV-Terraform"
  }
}

resource "aws_security_group" "vm_sg" {
  name        = "vm_sg"
  description = "Permite SSH y HTTP"

  ingress {
    description = "SSH"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
