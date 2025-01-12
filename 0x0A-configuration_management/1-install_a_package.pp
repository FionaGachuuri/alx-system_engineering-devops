# This puppet manifest installs flask version 2.1.0 using pip3

# ensuring pip3 is installed
package { 'python3-pip':
	ensure => installed,
}

# install flask version 2.1.0 using pip3 and werkzeug version 2.1.1
exec {'install_flask_and_werkzeug':
	command => '/usr/bin/pip3 install flask==2.1.0 werkzeug==2.1.1',
	path => [ '/usr/bin', 'usr/local/bin'],
	unless => '/usr/bin/pip3 show flask | grep Version | grep 2.1.0 && /usr/bin/pip3 show werkzeug | grep Version | grep 2.1.1',
	environment => ['Home=/root', 'PATH=/usr/bin:/usr/local/bin'],
}
