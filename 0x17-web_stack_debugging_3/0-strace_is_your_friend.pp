# Apache not running well on wp-site

$wp_path = '/var/www/html'

exec { 'fix-wordpress':
  command => "sed -i 's/phpp/php/g' ${wp_path}/wp-settings.php && sudo service apache2 restart",
  path    => ['/bin', '/usr/bin', '/usr/sbin'],
}
