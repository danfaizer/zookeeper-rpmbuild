This repo contains spec and source files to create zookeeper rpm package.

Required packages to generate rpm:

	yum install -y rpm-build rpmdevtools

To generate the RPMs:

	rpmbuild -ba SPECS/zookeeper.spec

To install the generated RPM package:

	rpm -Uvh RPMS/noarch/zookeeper-3.4.6-0.noarch.rpm

TO-DO:
- Check JVM dependency
- Setup zookeeper user/group to run the service
- Develop uninstall process	
