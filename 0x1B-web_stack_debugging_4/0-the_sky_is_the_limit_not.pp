# This manifest updates the Nginx configuration to increase the open limit from 15 to 4096 and then restarts Nginx.
exec { 'nginx fix':
  onlyif   => 'test -e /etc/default/nginx',
  command  => "sed -i 's/-n 15/-n 4096/g' /etc/default/nginx",
  provider => 'shell',
  notify   => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}
