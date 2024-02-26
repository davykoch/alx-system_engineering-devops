# 100-puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => present,
}

augeas { 'Turn off passwd auth':
  context => '/files/etc/ssh/ssh_config',
  changes => 'set PasswordAuthentication no',
}

augeas { 'Declare identity file':
  context => '/files/etc/ssh/ssh_config',
  changes => 'set IdentityFile ~/.ssh/school',
}
