# Resolve traffic in Nginx server 

file { 'resolve-request':
  ensure  => 'file',
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
}

# Start/Restart Nginx
-> exec { 'nginx-restart':
  command => 'nginx restart',
  path    => '/etc/init.d/',
}
