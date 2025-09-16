variable "example_instance_type" {
  description = "The instance type for the EC2 instance"
  type        = string
  default     = "t3.micro"
  
  validation {
    condition     = length(var.example_instance_type) > 0
    error_message = "Instance type must not be empty."
  }
}