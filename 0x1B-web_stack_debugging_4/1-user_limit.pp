# OS configuration change 
  file { '/etc/security/limits.conf':
    ensure  => file,
    owner   => 'root',
    group   => 'root',
    mode    => '0644',
    content => "holberton soft nofile 4096\nholberton hard nofile 10240",
  }
