# Chef recipe to create a user
# File name: create_user_$(openssl rand -hex 4).rb

# Create a system user
user 'my_app_user' do
  comment 'Application User'
  uid 1001
  gid 1001
  home '/home/my_app_user'
  shell '/bin/bash'
  password '$1$xyz$wB45A9sZvT2Bq3mR65s8e1' # Example encrypted password
  action :create
end

# Create the user's home directory
directory '/home/my_app_user' do
  owner 'my_app_user'
  group 'my_app_user'
  mode '0755'
  action :create
end