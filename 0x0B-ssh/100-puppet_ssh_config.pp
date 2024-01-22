# puppet_ssh_config.pp

file { '/root/.ssh/config':
  ensure  => 'present',
  content => "
Host 100.25.28.104
  IdentityFile /root/.ssh/school
  PreferredAuthentications publickey
  PasswordAuthentication no",
}
