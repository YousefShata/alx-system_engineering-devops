#config

file { '/root/.ssh/config':
ensure  => 'present',
content => "
Host 54.160.106.244
	IdentityFile /root/.ssh/school
	PreferredAuthentications publickey
	PasswordAuthentication no
",
}
