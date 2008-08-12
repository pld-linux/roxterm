Summary:	ROXTerm is a terminal emulator
Summary(hu.UTF-8):	ROXTerm egy terminál emulátor
Name:		roxterm
Version:	1.12.2
Release:	0.1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/roxterm/%{name}-%{version}.tar.gz
# Source0-md5:	bb7e30d19d42b24bc49ad403fcde9058
URL:		http://roxterm.sourceforge.net
BuildRequires:	dbus-glib-devel
BuildRequires:	libglade2-devel
BuildRequires:	readline-devel
BuildRequires:	vte-devel
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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
