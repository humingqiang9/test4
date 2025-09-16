# Chef recipe to create a user
# File name: sYKaopZ7PN.rb

# Create a new user named 'newuser'
user 'newuser' do
  comment 'New User'
  uid 1001
  gid 1001
  home '/home/newuser'
  shell '/bin/bash'
  password '$1$xyz$w5Qk5zV5VzVzVzVzVzVzV.' # Example encrypted password
  action :create
end

# Create the user's home directory
directory '/home/newuser' do
  owner 'newuser'
  group 'newuser'
  mode '0755'
  action :create
end