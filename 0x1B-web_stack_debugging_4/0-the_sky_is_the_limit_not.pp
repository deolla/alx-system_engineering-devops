# This manuscript increases the amount of traffic an Nginx server can handle

file { 'resolve-request':
  ensure  => 'file',
  path    => '/etc/default/nginx',
  content => inline_template('<%= File.read("/etc/default/nginx").gsub(/15/, "4096") %>'),
}

# Start/Restart Nginx
-> exec { 'nginx-restart':
  command => 'sudo nginx restart',
  path    => '/etc/init.d/',
}
