%define name python-memphis
%define version 0.2.1
%define release %mkrel 3

Summary: Python bindings for the Memphis maps renderer
Name: %{name}
Version: %{version}
Release: %{release}
Source0: pymemphis-mainline-master.tar.gz
License: GPLv2+
Group: Development/Python
Url: http://gitorious.net/pymemphis
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: memphis-devel
BuildRequires: python-gobject-devel
BuildRequires: python-cairo-devel

%description
Libmemphis is a generic glib/cairo based OSM renderer library. It
draws maps on arbitrary cairo surfaces. PyMemphis provides Python
bindings for this library.

%package devel
Summary: Python bindings for the Memphis maps renderer
Group: Development/Python
Requires: %name = %version-%release

%description devel
Libmemphis is a generic glib/cairo based OSM renderer library. It
draws maps on arbitrary cairo surfaces. PyMemphis provides Python
bindings for this library.

%prep
%setup -q -n pymemphis-mainline
NOCONFIGURE=1 ./autogen.sh

%build
%configure2_5x
%make LIBS="`python-config --libs`"

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS README
%py_platsitedir/memphis

%files devel
%defattr(-,root,root)
%_datadir/pymemphis
%_libdir/pkgconfig/pymemphis-0.2.pc
