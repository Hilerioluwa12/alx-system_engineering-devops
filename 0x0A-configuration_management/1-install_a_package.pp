# install puppet-lint using a command
package { 'flask /bin/pip3':
  ensure   => '2.1.0',
  provider => 'gem',
}
