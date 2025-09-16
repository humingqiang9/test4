# Chef recipe to create and manage a user
# This recipe creates a system user with specific attributes

# Create a user named 'appuser'
user 'appuser' do
  comment 'Application User'
  uid 1001
  gid 1001
  home '/home/appuser'
  shell '/bin/bash'
  password '/' # Example encrypted password
  action :create
end

# Create the user's home directory
directory '/home/appuser' do
  owner 'appuser'
  group 'appuser'
  mode '0755'
  action :create
end
