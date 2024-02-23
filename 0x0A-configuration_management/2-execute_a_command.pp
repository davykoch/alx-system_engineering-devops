# Puppet Manifest: Execute pkill to terminate the killmenow process

exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
  path    => '/usr/bin',
  onlyif  => '/usr/bin/pgrep -f killmenow',
}
