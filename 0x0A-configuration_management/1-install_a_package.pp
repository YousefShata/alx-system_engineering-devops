# Install Flask version 2.1.0 using pip3
package { 'flask':
provider => 'pip3',
ensure   => '2.1.0'
}
