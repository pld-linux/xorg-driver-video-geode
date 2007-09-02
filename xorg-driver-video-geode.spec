Summary:	X.org video driver for AMD Geode integrated graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla zintegrowanych układów graficznych AMD Geode
Name:		xorg-driver-video-amd
Version:	2.7.7.0
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-amd-%{version}.tar.bz2
# Source0-md5:	650a8870a1a6844114e8d025b3784763
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xf86dgaproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.3.0.0
Requires:	xorg-xserver-server >= 1.3.0.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for AMD Geode GX and LX integrated graphics
chipsets.

%description -l pl.UTF-8
Sterownik obrazu X.org dla zintegrowanych układów graficznych AMD
Geode GX and LX.

%prep
%setup -q -n xf86-video-amd-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README ChangeLog TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/amd_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ztv_drv.so
