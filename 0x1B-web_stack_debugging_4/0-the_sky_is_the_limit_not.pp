# Resolve huge amount or request

exec { 'resolve-request':
  command => "sed -i 's/15/4096\' /etc/default/nginx",
  path    => '/usr/local/bin/:/bin/'
}->

exec {'restart-nginx':
  command => 'sudo service nginx restart',
  path    => '/etc/init.d/'
}
