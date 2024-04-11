# Puppet manifest to fix Apache 500 error by correcting a misconfigured PHP module

package { 'php':
  ensure => 'installed',
}

file { '/etc/apache2/mods-available/php7.0.conf':
  ensure  => 'file',
  content => '# This file is intentionally left blank',
  notify  => Service['apache2'],
}

service { 'apache2':
  ensure  => 'running',
  enable  => true,
  require => Package['php'],
}
