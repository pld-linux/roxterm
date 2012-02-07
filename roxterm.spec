#
# TODO: why fr and gl locales are not packaged by find_lang macro?
#
# Conditional build:
%bcond_with	gnomecontrol	# register with GNOME as a default terminal application
#
Summary:	ROXTerm - a terminal emulator
Summary(hu.UTF-8):	ROXTerm egy terminál emulátor
Summary(pl.UTF-8):	ROXTerm - emulator terminala
Name:		roxterm
Version:	2.4.2
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://downloads.sourceforge.net/roxterm/%{name}-%{version}.tar.bz2
# Source0-md5:	7c3bb1471f814a8bfdfcf169ad18e425
Patch0:		%{name}-flags.patch
URL:		http://roxterm.sourceforge.net/
BuildRequires:	ImageMagick
BuildRequires:	dbus-devel
BuildRequires:	dbus-glib-devel >= 0.22
BuildRequires:	gettext-devel >= 0.17
BuildRequires:	glib2-devel >= 1:2.16.0
%{?with_gnomecontrol:BuildRequires:	gnome-control-center-devel}
BuildRequires:	gtk+3-devel
BuildRequires:	libglade2-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	po4a
BuildRequires:	python-lockfile
BuildRequires:	rpmbuild(macros) >= 1.311
BuildRequires:	sed >= 4.0
BuildRequires:	vte-devel >= 0.27.0
BuildRequires:	xmlto
BuildRequires:	xorg-lib-libSM-devel
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	hicolor-icon-theme
Requires:	dbus
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
%patch0 -p1

%build
%{__python} mscript.py configure \
	--enable-gtk3 \
	--enable-sm \
	--with%{!?with_gnomecontrol:out}-gnome-default-applications

%{__python} mscript.py build \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__python} mscript.py install \
	PREFIX="%{_prefix}" \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/doc

%find_lang %{name} --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README Help/en Help/es Help/lib
%attr(755,root,root) %{_bindir}/roxterm-config
%attr(755,root,root) %{_bindir}/roxterm
%{_datadir}/%{name}
%{?with_gnomecontrol:%{_datadir}/gnome-control-center/default-apps/roxterm.xml}
%{_desktopdir}/roxterm.desktop
%{_iconsdir}/hicolor/scalable/apps/roxterm.svg
%{_mandir}/man1/roxterm-config.1*
%{_mandir}/man1/roxterm.1*
%lang(es) %{_mandir}/es/man1/roxterm-config.1*
%lang(es) %{_mandir}/es/man1/roxterm.1*
