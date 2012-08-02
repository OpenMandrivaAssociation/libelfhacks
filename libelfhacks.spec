#
%define name    libelfhacks 

Name:			%{name}
Version:		0.4.1
%define rel		1
Release:		%mkrel %rel
Summary:		elfhacks application interface
License:		MIT-Style
Group:			System/Libraries
URL:			https://github.com/ienorand/elfhacks
BuildRoot:      	%_tmppath/%{name}-%{version}-%{release}-buildroot
Source0:		libelfhacks-0.4.1.tar.bz2
ExclusiveArch:		i586 x86_64
BuildRequires:		cmake
BuildRequires:		gcc gcc-c++ make


%description	
Various ELF run-time hacks.

%prep  
%setup -q -n %{name}-%{version}

%build 
cmake -D CMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT .
%make

%install 
rm -rf $RPM_BUILD_ROOT
%makeinstall
mkdir $RPM_BUILD_ROOT/usr
mv $RPM_BUILD_ROOT/include $RPM_BUILD_ROOT/usr/include
%ifarch i586
mv $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/usr/lib
%endif
%ifarch x86_64
mv $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/usr/lib64
%endif 

%clean
rm -rf $RPM_BUILD_ROOT

%files -n %{name}
%defattr(0755,root,root)
%{_libdir}/libelfhacks*
%{_includedir}/*



%changelog
* Mon Apr 02 2012 Zombie Ryushu <ryushu@mandriva.org> 0.4.1-1mdv2011.0
+ Revision: 788674
- Be more clear what libs to package
- imported package libelfhacks


* Mon Apr 2 2012 codebase7 <codebase7@yahoo.com> - 0.4.1-1.mga1
- initial specfile 

