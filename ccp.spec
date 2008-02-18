%define	name	ccp
%define	version 0.4.1
%define rel	1
%define	release	%mkrel %rel

Name:		%{name} 
Summary:	Program that reads configuration files and upgrades them
Version:	%{version} 
Release:	%{release} 
Source0:	%{name}-%{version}.tar.bz2
URL:		http://ccp.nongnu.org/
Group:		System/Configuration/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
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
%setup -q
# We want the tests to succeed. A release shouldn't have failing tests
# but better safe than sorry
if ! ./testsuite/ccp-testsuite ; then exit 1;fi

%install
rm -rf $RPM_BUILD_ROOT
mkdir -vp $RPM_BUILD_ROOT%_bindir/ $RPM_BUILD_ROOT%_mandir/man1/ $RPM_BUILD_ROOT%_datadir/ccp/
install -v -m755 ccp  $RPM_BUILD_ROOT%_bindir/
install -v -m644 ccp.1 $RPM_BUILD_ROOT%_mandir/man1/
cp -vr conftypes $RPM_BUILD_ROOT%_datadir/ccp/

%clean 
rm -rf $RPM_BUILD_ROOT 

%files 
%defattr(-,root,root)
%doc TODO version AUTHORS
%_bindir/%name
%_mandir/*/*
%_datadir/%name

