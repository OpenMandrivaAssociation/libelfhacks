%define develname %mklibname -d elfhacks
%define name            libelfhacks 
%define release		1
%define version         0.4.1
Name:			%{name}
Version:		%{version}
Release:		%{release}
Summary:		elfhacks application interface
License:		MIT
Group:			System/Libraries
URL:			https://github.com/ienorand/elfhacks
Source0:		https://nodeload.github.com/ienorand/elfhacks/zipball/libelfhacks-0.4.1.tar.bz2
ExclusiveArch:		i586 x86_64
BuildRequires:		cmake
BuildRequires:		gcc 
BuildRequires:		gcc-c++ 
BuildRequires:		make


%description	
Various ELF run-time hacks.

%prep  
%setup -q -n %{name}-%{version}

%build 
cmake -D CMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT .
%make

%install 
%makeinstall
mkdir $RPM_BUILD_ROOT/usr
mv $RPM_BUILD_ROOT/include $RPM_BUILD_ROOT%{_includedir}

%ifarch x86_64
mv $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/usr/lib64
%else
mv $RPM_BUILD_ROOT/lib $RPM_BUILD_ROOT/usr/lib
%endif 


%package -n %{name}
Summary: Shared library for %{name}
Group: System/Libraries

%description -n %{name}
Shared library for %{name}

%files -n %{name}
%defattr(0755,root,root)
%{_libdir}/libelfhacks*
#------------------

%package -n %{develname}
Summary: Development files for %{name}
Provides: %{name}-devel = %{version}-%{release}
Requires: %{name} = %{version}-%{release}

%description -n %{develname}
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%files -n %{develname}
%{_includedir}/*

