# Chef recipe to create a user
# File: f5qqaoAeX7.rb

# Create a new user
user 'myuser' do
  comment 'My Test User'
  uid 1001
  gid 1001
  home '/home/myuser'
  shell '/bin/bash'
  password '$1$xyz$wB45B2u3PjcRgQ43V7VcD1' # Example encrypted password
  action :create
end

# Create home directory for the user
directory '/home/myuser' do
  owner 'myuser'
  group 'myuser'
  mode '0755'
  action :create
end