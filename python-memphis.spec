Summary: Python bindings for the Memphis maps renderer
Name: python-memphis
Version: 0.2.1
Release: 6
Source0: pymemphis-mainline-master.tar.gz
Patch0: pymemphis-automake-1.13.patch
License: GPLv2+
Group: Development/Python
Url: http://gitorious.net/pymemphis
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
%apply_patches
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


%changelog
* Sun Apr 10 2011 Funda Wang <fwang@mandriva.org> 0.2.1-4mdv2011.0
+ Revision: 652196
- rebuild

* Sat Apr 09 2011 Funda Wang <fwang@mandriva.org> 0.2.1-3
+ Revision: 652108
- link iwth libpython

* Thu Nov 04 2010 Götz Waschk <waschk@mandriva.org> 0.2.1-2mdv2011.0
+ Revision: 593363
- rebuild for new python 2.7

* Wed Aug 04 2010 Götz Waschk <waschk@mandriva.org> 0.2.1-1mdv2011.0
+ Revision: 565771
- import python-memphis


