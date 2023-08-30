#puppet test file

file_line { 'password_change':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}

file_line { 'identify_file':
  ensure  => present,
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/school',
  replace => true,
}
