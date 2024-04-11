# Puppet manifest to fix Apache 500 error by setting correct permissions on the document root directory

exec { 'fix-apache-permissions':
  command => '/bin/chown -R www-data:www-data /var/www/html',
  path    => ['/bin', '/usr/bin'],
  unless  => '/bin/stat -c "%U:%G" /var/www/html | /bin/grep www-data:www-data',
}
