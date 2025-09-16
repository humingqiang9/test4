# Chef Recipe to Install a Package
# This recipe installs the 'curl' package

package 'curl' do
  action :install
end

# Alternative syntax:
# package 'curl'