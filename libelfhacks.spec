%define major 0
%define libname %mklibname elfhacks %{major}
%define devname %mklibname elfhacks -d

Summary:	elfhacks application interface
Name:		libelfhacks
Version:	0.4.1
Release:	2
License:	MIT
Group:		System/Libraries
Url:		https://github.com/ienorand/elfhacks
Source0:	https://nodeload.github.com/ienorand/elfhacks/zipball/%{name}-%{version}.tar.bz2
BuildRequires:	cmake

%description
Various ELF run-time hacks.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries
Conflicts:	%{name} < 0.4.1-2
Obsoletes:	%{name} < 0.4.1-2

%description -n %{libname}
Shared library for %{name}.

%files -n %{libname}
%{_libdir}/libelfhacks.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 0.4.1-2

%description -n %{devname}
This package contains libraries and header files for developing applications
that use %{name}.

%files -n %{devname}
%{_includedir}/*
%{_libdir}/libelfhacks.so

#----------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake -DMLIBDIR=%{_libdir}
%make

%install
%makeinstall_std -C build

