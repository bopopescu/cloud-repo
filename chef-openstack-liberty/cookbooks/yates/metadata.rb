name             'yates'
maintainer       'rafael'
maintainer_email 'rsuarez@uchicago.edu'
license          'Apache 2.0'
description      'Deploys nodes via PXE and Chef'
long_description IO.read(File.join(File.dirname(__FILE__), 'README.md'))
version          '0.3.0'
depends          'tftp'
depends          'chef-lighttpd'