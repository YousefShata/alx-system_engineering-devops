#config

file { '~/.ssh/config':
ensure  => present,
content => "
Host 54.160.106.244
	IdentityFile ~/.ssh/school
	PreferredAuthentications publickey
	PasswordAuthentication no
",
}
