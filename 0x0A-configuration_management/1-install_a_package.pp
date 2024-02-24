# Puppet Manifest: Install Flask from pip3

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.0.0',
  provider => 'pip3',
}
