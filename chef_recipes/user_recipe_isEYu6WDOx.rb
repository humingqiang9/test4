# Chef recipe to create a user
# File name: user_recipe_isEYu6WDOx.rb

# Create a new user named 'newuser'
user 'newuser' do
  comment 'New User'
  uid 1001
  gid 'users'
  home '/home/newuser'
  shell '/bin/bash'
  password '$1$xyz$encrypted_password_hash' # Example hash, replace with actual encrypted password
  action :create
end