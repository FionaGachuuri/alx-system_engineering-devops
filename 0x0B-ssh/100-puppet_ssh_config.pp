#include stdlib

file_line { 'Turn off password authentication':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => 'PasswordAuthentication no';

  'key_location':
ensure => present,
path   => '/etc/ssh/ssh_config',
line   => '	IdentityFile ~/.ssh/school'
}
