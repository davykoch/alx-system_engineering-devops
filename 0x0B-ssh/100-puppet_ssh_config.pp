# 100-puppet_ssh_config.pp

file { '/etc/ssh/ssh_config':
  ensure  => present,
  content => "PasswordAuthentication no\nIdentityFile ~/.ssh/school\n",
}

augeas { 'Turn off passwd auth':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set Host/*/#comment[.="*"]/PasswordAuthentication no',
  ],
}

augeas { 'Declare identity file':
  context => '/files/etc/ssh/ssh_config',
  changes => [
    'set Host/*/#comment[.="*"]/IdentityFile ~/.ssh/school',
  ],
}
