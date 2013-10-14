Summary:	X.org video driver for AMD Geode integrated graphics chipsets
Summary(pl.UTF-8):	Sterownik obrazu X.org dla zintegrowanych układów graficznych AMD Geode
Name:		xorg-driver-video-geode
Version:	2.11.15
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-video-geode-%{version}.tar.bz2
# Source0-md5:	7dafd19e274c771539b6d4d459423ccf
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-lib-libpciaccess-devel >= 0.8.0
BuildRequires:	xorg-proto-fontsproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-proto-renderproto-devel
BuildRequires:	xorg-proto-videoproto-devel
BuildRequires:	xorg-proto-xextproto-devel >= 7.0.99.1
BuildRequires:	xorg-util-util-macros >= 1.4
BuildRequires:	xorg-xserver-server-devel >= 1.3.0.0
%{?requires_xorg_xserver_videodrv}
Requires:	xorg-xserver-server >= 1.3.0.0
Provides:	xorg-driver-video
Obsoletes:	xorg-driver-video-amd < 2.8.0
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org video driver for AMD Geode GX (GX2) and LX (GX3) integrated
graphics chipsets.

Note: currently this driver doesn't support Geode GX1 chips by Cyrix
  and NSC.
- NSC Geode (GX2/SCx200/SC1400) chips are supported by
  xorg-driver-video-nsc driver,
- Cyrix Geode MediaGX (GX1) chips are supported by
  xorg-driver-video-cyrix driver.

%description -l pl.UTF-8
Sterownik obrazu X.org dla zintegrowanych układów graficznych AMD
Geode GX (GX2) i LX (GX3).

Uwaga: aktualnie ten sterownik nie obsługuje układów Geode GX1
produkowanych przez firmy Cyrix i NSC. Układy:
- NSC Geode (GX2/SCx200/SC1400) są obsługiwane przez sterownik
  xorg-driver-video-nsc,
- Cyrix Geode MediaGX (GX1) są obsługiwane przez sterownik
  xorg-driver-video-cyrix.

%prep
%setup -q -n xf86-video-geode-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/drivers/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/geode_drv.so
%attr(755,root,root) %{_libdir}/xorg/modules/drivers/ztv_drv.so
