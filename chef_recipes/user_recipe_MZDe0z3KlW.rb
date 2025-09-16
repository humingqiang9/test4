# Chef recipe to create a user
user 'testuser' do
  comment 'Test User'
  uid 1001
  gid 1001
  home '/home/testuser'
  shell '/bin/bash'
  password '$1$xyz$wz3vEjaN4v/Z19gRt/pDy1' # This is a placeholder password
  action :create
end