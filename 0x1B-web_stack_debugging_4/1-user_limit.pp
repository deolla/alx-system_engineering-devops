# Resolve huge amount or request

exec {'os-config':
  command => "sed -i '/holberton hard/s/5/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}

exec { 'os-config1':
  command => "sed -i '/holberton soft/s/4/50000/' /etc/security/limits.conf",
  path    => '/usr/local/bin/:/bin/'
}
