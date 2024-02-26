# 100-puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => template('ssh_config.erb'),
}

file { '/etc/ssh/sshd_config':
  ensure  => present,
  content => template('sshd_config.erb'),
}
