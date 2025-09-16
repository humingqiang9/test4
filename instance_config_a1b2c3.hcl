variable "example_instance_type" {
  description = "The instance type for the EC2 instance"
  type        = string
  default     = "t3.micro"
  
  validation {
    condition     = contains(["t3.micro", "t3.small", "t3.medium"], var.example_instance_type)
    error_message = "Instance type must be one of t3.micro, t3.small, or t3.medium."
  }
}