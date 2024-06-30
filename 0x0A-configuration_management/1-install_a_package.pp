# Install a specific version of flask (2.1.0)
package { 'python3-pip':
  ensure => installed,
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

# Install werkzeug requirement
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
  require  => Package['Flask'],
}
