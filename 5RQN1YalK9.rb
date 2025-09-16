# Chef recipe to create a user
# File name: 5RQN1YalK9.rb

# Create a new user named 'myuser'
user 'myuser' do
  comment 'My User'
  uid 1001
  gid 1001
  home '/home/myuser'
  shell '/bin/bash'
  password '$1$xyz$wtfp9GgaXvMQ9zy0UicK9.' # Example encrypted password
  action :create
end

# Create the user's home directory
directory '/home/myuser' do
  owner 'myuser'
  group 'myuser'
  mode '0755'
  action :create
end