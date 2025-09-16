resource "aws_instance" "example" {
  ami           = "ami-0c55b159cbfafe1d0" # Amazon Linux 2 AMI (HVM) - Kernel 5.10, SSD Volume Type
  instance_type = "t2.micro"
  key_name      = "my-key-pair"

  tags = {
    Name = "MyEC2Instance"
  }
}