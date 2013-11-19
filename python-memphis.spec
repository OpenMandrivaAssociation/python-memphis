Summary:	Python bindings for the Memphis maps renderer
Name:		python-memphis
Version:	0.2.1
Release:	6
License:	GPLv2+
Group:		Development/Python
Url:		http://gitorious.net/pymemphis
Source0:	pymemphis-mainline-master.tar.gz
Patch0:		pymemphis-automake-1.13.patch
BuildRequires:	pkgconfig(memphis-0.2)
BuildRequires:	pkgconfig(pycairo)
BuildRequires:	pkgconfig(pygobject-2.0)

%description
Libmemphis is a generic glib/cairo based OSM renderer library. It
draws maps on arbitrary cairo surfaces. PyMemphis provides Python
bindings for this library.

%package devel
Summary:	Python bindings for the Memphis maps renderer
Group:		Development/Python
Requires:	%{name} = %{version}-%{release}

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
%makeinstall_std

%files
%doc AUTHORS README
%{py_platsitedir}/memphis

%files devel
%{_datadir}/pymemphis
%{_libdir}/pkgconfig/pymemphis-0.2.pc

