This repo contains spec and source files to create zookeeper rpm package.

Required packages to generate rpm:

	yum install -y rpm-build rpmdevtools

You may need to modify and customize: ~/.rpmmacros file

To generate the RPMs:

	rpmbuild -ba SPECS/zookeeper.spec

To install the generated RPM package:

	rpm -Uvh RPMS/noarch/zookeeper-3.4.6-0.noarch.rpm


NOTES:

- Source zookeeper.3.4.6.tar.gz file has been slightly modified to allow use zkServer.sh run as init.d script
and conf/zoo.cfg has been preconfigured to allow service run without any manual step.

Used this notes:

- http://positivealex.github.io/blog/posts/how-to-install-zookeeper-as-service-on-centos/	
