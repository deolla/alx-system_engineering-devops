# Define a package resource to install Flask
package { 'python3-pip':
  ensure => 'installed',
}

# Define an exec resource to install Flask version 2.1.0 using pip3
exec { 'install flask':
  command => 'pip3 install "flask==2.1.0"',
  require => Package['python3-pip'],
}
