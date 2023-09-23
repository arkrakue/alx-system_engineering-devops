# Manifest to kill a process killmenow

exec { 'kill_killmenow_process':
  command  => 'pkill killmenow',
  path     => '/usr/bin:/usr/sbin:/bin:/sbin',
  onlyif   => 'pgrep killmenow',
  provider => shell,
}
