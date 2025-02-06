# automating Nginx configuration using puppet

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => Package['nginx'],
}

file_line { 'add_redirect_rule':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  line   => 'rewrite ^/redirect_me https://www.github.com/FionaGachuuri permanent;',
  match  => '^listen 80 default_server;',
  notify => Service['nginx'],
}

file { '/var/www/html/index.html':
  content => 'Hello World!',
}

service { 'nginx':
  ensure  => running,
  require => Package['nginx'],
}
