Summary:	ROXTerm is a terminal emulator
Summary(hu.UTF-8):	ROXTerm egy terminál emulátor
Summary(pl.UTF-8):	Emulator terminala
Name:		roxterm
Version:	1.13.0
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/roxterm/%{name}-%{version}.tar.gz
# Source0-md5:	5ec0918781d113181afccf454dbff236
URL:		http://roxterm.sourceforge.net
BuildRequires:	dbus-glib-devel
BuildRequires:	libglade2-devel
BuildRequires:	readline-devel
BuildRequires:	vte-devel
Requires:	dbus
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ROXTerm is a terminal emulator intended to provide similar features to
gnome-terminal, based on the same VTE library, but with a smaller
footprint and quicker start-up time. It achieves this by not using the
Gnome libraries and by using a separate applet to provide the
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
do gnome-terminal, bazować na tej samej bibliotece VTE, ale być
mniejszy i szybciej się uruchamiać. Cel ten został osiągnięty, dzięki
temu, że ROXTerm nie używa bibliotek Gnome i uzywa osobnego applteu do
konfiguracji GUI. ROXTerm - jak nazwa wskazuje - może być używany jako
aplikacja ROX. Może być równiez używany z dowolnym innym środowiskiem
X.

%prep
%setup -q

%build
%configure \
	--docdir=%{_docdir}/%{name}-%{version} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_docdir}/%{name} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

%find_lang %{name}.lang

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/roxterm.desktop
%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/*
%{_iconsdir}/hicolor/scalable/apps/roxterm.svg
