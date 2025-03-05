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
