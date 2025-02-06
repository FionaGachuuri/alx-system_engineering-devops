# Puppet script to install and configure Nginx with a redirect and custom index page

# Install Nginx
package { 'nginx':
  ensure => installed,
}

# Ensure Nginx is running and enabled on boot
service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

# Modify the default Nginx configuration to add a redirect
file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  require => Package['nginx'],
  notify  => Service['nginx'],
}

# Ensure the symlink exists in sites-enabled
file { '/etc/nginx/sites-enabled/default':
  ensure => link,
  target => '/etc/nginx/sites-available/default',
  require => File['/etc/nginx/sites-available/default'],
  notify => Service['nginx'],
}

# Create a custom index.html file
file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx'],
}
