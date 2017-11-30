Summary: high-availability-dcache
Name: high-availability-dcache
Version: 1.0.0
Release: 1
License: GPL
Group: System Environment/Daemons
URL: http://rpm.org/
#Source0: ftp://rpm.org/%{name}_%{version}.source.tar.gz
Source0: %{name}-%{version}.tar.gz
#BuildPreReq: python
BuildRoot: %{_tmppath}/%{name}-%{version}-root


######################################################################
#
#
# Preamble
#
# Macro definitions
%define _prefix         /usr
%define _sysconfdir     /etc
%define _profile_dir    /etc/profile.d

%description
high-availability-dcache

%prep
%setup -q -n %{name}-%{version}
#./configure --prefix=%{_prefix}

%build
make

%install
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make install DESTDIR=${RPM_BUILD_ROOT}

[ "$RPM_BUILD_ROOT" != "/" ] && mkdir -p ${RPM_BUILD_ROOT}/%{_profile_dir}
cp bin/thisroot.sh ${RPM_BUILD_ROOT}/%{_profile_dir}/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_prefix}
%{_sysconfdir}
%{_profile_dir}
