# This Puppet manifest installs Flask version 2.1.0 and Werkzeug version 2.1.1 using pip3

# Ensure pip3 is installed
package { 'python3-pip':
  ensure => installed,
}

# Install Flask version 2.1.0 and Werkzeug version 2.1.1 using pip3
exec { 'install_flask_and_werkzeug':
  command     => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.1.1',
  path        => ['/usr/bin', '/usr/local/bin'],
  unless      => '/usr/bin/pip3 show flask | grep Version | grep 2.1.0 && /usr/bin/pip3 show werkzeug | grep Version | grep 2.1.1',
  environment => ['HOME=/root', 'PATH=/usr/bin:/usr/local/bin'],
}
