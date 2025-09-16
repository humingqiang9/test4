# Chef recipe to create a user
# Filename: nP4WGQ4UEw.rb

# Create a new user named 'myuser'
user 'myuser' do
  comment 'My Custom User'
  uid 1001
  gid 1001
  home '/home/myuser'
  shell '/bin/bash'
  password '$1$xyz$wvVz5W6SHdNvM8hVJ3N6l0' # Example encrypted password
  action :create
end

# Create the user's home directory
directory '/home/myuser' do
  owner 'myuser'
  group 'myuser'
  mode '0755'
  action :create
end