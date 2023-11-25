# Install Flask version 2.1.0 using pip3
package { 'Werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
