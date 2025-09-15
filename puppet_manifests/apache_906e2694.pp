# Apache Installation Manifest
# This manifest installs and starts the Apache web server

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

# Apply the apache_install class
include apache_install