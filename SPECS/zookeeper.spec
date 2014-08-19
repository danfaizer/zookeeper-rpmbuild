Name: zookeeper
Version: 3.4.6
AutoReqProv: no
Release: 0
Summary: Zookeeper is a highly reliable distributed coordination service.
License: Apache 2.0
Group: Applications/Internet
Source0: zookeeper-3.4.6.tar.gz
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-root
Provides: zookeeper
Requires(post): /usr/sbin/useradd
%description
ZooKeeper is a centralized service for maintaining configuration information, naming, providing distributed synchronization, and providing group services. All of these kinds of services are used in some form or another by distributed applications. Each time they are implemented there is a lot of work that goes into fixing the bugs and race conditions that are inevitable. Because of the difficulty of implementing these kinds of services, applications initially usually skimp on them ,which make them brittle in the presence of change and difficult to manage. Even when done correctly, different implementations of these services lead to management complexity when the applications are deployed.
%prep
%build
%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/opt/zookeeper
mkdir -p $RPM_BUILD_ROOT/etc/init.d
mkdir -p %{_localstatedir}/lib/zookeeper
tar xfz $RPM_SOURCE_DIR/zookeeper-%{version}.tar.gz
cp -r $RPM_BUILD_DIR/zookeeper-%{version}/* $RPM_BUILD_ROOT/opt/zookeeper
%pre
# TO-DO : Start service with zookeeper user
#getent group zookeeper >/dev/null || groupadd -r zookeeper
#getent passwd zookeeper >/dev/null || useradd -r -g zookeeper -d / -s /sbin/nologin zookeeper
%preun
# TO-DO : Uninstall steps : Remove init.d script, stop service and clean
%clean
rm -rf $RPM_BUILD_ROOT
%post
ln -sf /opt/zookeeper/bin/zkServer.sh %{_sysconfdir}/init.d/zookeeper
/sbin/chkconfig zookeeper on

%files
%defattr(-,root,root,-)
/opt/zookeeper

%changelog
* Tue Aug 19 2014 - daniel.beneyto at abiquo dot com
- Initial release.