Summary:	Program that reads configuration files and upgrades them
Name:		ccp
Version:	0.4.1
Release:	26
Group:		System/Configuration/Other
License:	GPL
Url:		https://random.zerodogg.org/ccp/
Source0:	http://download.savannah.nongnu.org/releases/ccp/%{name}-%{version}.tar.bz2
BuildArch:	noarch

%description
CCP is a program that reads configuration files and upgrades them.

It takes a oldfile (typically the old configuration file currently in
use) and a newfile (typically the default new configuration  file)  and
optionally a template (a file which tells ccp how the generated
configuration file should look like. It is generated on-the-fly if a template
isn't supplied, so it is usually not needed). CCP first reads all the
configuration options and values in the new file, then in the old file,
then it either generates the template or reads the supplied template
file, finally it merges the files into one - creating a new 
configuration file that has the changes that was made to the old file
but also the new options that is included in the new file.

CCP is completely independent of the program that created the 
configuration  file, and can be used for many different purposes. For
instance it can be used to merge changes between an old  user-edited 
configuration file and a .rpmnew file generated by rpm when a
rpm was upgraded.

CCP currently supports:
key = value configs (--type keyvalue)
and ini configs (--type ini)

%prep
%autosetup -p1
# We want the tests to succeed. A release shouldn't have failing tests
# but better safe than sorry
if ! ./testsuite/ccp-testsuite ; then exit 1;fi

%install
mkdir -vp %{buildroot}%{_bindir}/ %{buildroot}%{_mandir}/man1/ %{buildroot}%{_datadir}/ccp/
install -v -m755 ccp  %{buildroot}%{_bindir}/
install -v -m644 ccp.1 %{buildroot}%{_mandir}/man1/
cp -vr conftypes %{buildroot}%{_datadir}/ccp/

%files 
%doc TODO version AUTHORS
%{_bindir}/%{name}
%doc %{_mandir}/*/*
%{_datadir}/%{name}
