# handling more HTTP rquests
exec { 'create-ab-test-script':
  command => "/bin/bash -c 'echo -e \"#!/bin/bash\nab -c 100 -n 2000 -l localhost/\" \
               > /usr/local/bin/ab-test && chmod 0755 /usr/local/bin/ab-test'",
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
  unless  => 'test -f /usr/local/bin/ab-test',
}
