# This puppet manifest kills a process named killmenow.

exec { 'kill_process_killmenow':
  command => '/usr/bin/pkill killmenow',
  path    => ['/usr/bin', '/bin'],
  onlyif  => '/usr/bin/pgrep killmenow',
}