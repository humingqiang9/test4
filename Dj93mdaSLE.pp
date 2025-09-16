# Puppet manifest to install Apache
# File name: Dj93mdaSLE.pp

class apache_install {
  package { 'httpd':
    ensure => installed,
  }

  service { 'httpd':
    ensure => running,
    enable => true,
    require => Package['httpd'],
  }
}

# Apply the class
include apache_install