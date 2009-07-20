Summary:	ROXTerm - a terminal emulator
Summary(hu.UTF-8):	ROXTerm egy terminál emulátor
Summary(pl.UTF-8):	ROXTerm - emulator terminala
Name:		roxterm
Version:	1.15.2
Release:	2
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/roxterm/%{name}-%{version}.tar.gz
# Source0-md5:	c4988ce844b702a77f3609c623107e53
URL:		http://roxterm.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	dbus-glib-devel >= 0.22
BuildRequires:	gettext-devel
BuildRequires:	gtk+2-devel >= 2:2.6.0
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	vte-devel >= 0.11.11
Requires(post,postun):	gtk+2
Requires:	dbus
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ROXTerm is a terminal emulator intended to provide similar features to
gnome-terminal, based on the same VTE library, but with a smaller
footprint and quicker start-up time. It achieves this by not using the
GNOME libraries and by using a separate applet to provide the
configuration GUI. It can be used as a ROX application, as the name
implies, or in any other X environment.

%description -l hu.UTF-8
ROXTerm egy terminál emulátor, amely hasonló képességekkel bír, mint a
gnome-terminal. VTE alapú, de kisebb és gyorsabban indul. Nem
használja a Gnome könyvtárait és egy konfiguráló GUI-t is biztosít.
Használható ROX alkalmazásként is, mint ahogy a neve mutatatja, vagy
bármely más X környezetben.

%description -l pl.UTF-8
ROXTerm jest emulatorem terminala, który w założeniach ma być podobny
do gnome-terminala, bazować na tej samej bibliotece VTE, ale być
mniejszy i szybciej się uruchamiać. Cel ten został osiągnięty, dzięki
temu, że ROXTerm nie używa bibliotek GNOME, a do graficznego
interfejsu konfiguracyjnego używa osobnego apletu. ROXTerm - jak nazwa
wskazuje - może być używany jako aplikacja ROX. Może być również
używany z dowolnym innym środowiskiem X.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--docdir=%{_docdir}/%{name}-%{version}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_docdir}/%{name} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/roxterm-config
%attr(755,root,root) %{_bindir}/roxterm
%{_datadir}/%{name}
%{_desktopdir}/roxterm.desktop
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/*
%{_iconsdir}/hicolor/scalable/apps/roxterm.svg
