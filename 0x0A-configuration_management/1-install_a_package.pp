# Define a package resource to install Flask
package { 'install flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
