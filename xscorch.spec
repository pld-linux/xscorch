Summary:	Xscorch - clone of the classic DOS game "Scorched Earth"
Name:		xscorch
Version:	0.1.5
Release:	1
License:	GPL
Group:		X11/Games
Group(pl):	X11/Gry
Source0:	http://velius.chaos2.org/xscorch/%{name}-%{version}.tar.gz
Source1:	xscorch.png
Source2:	xscorch.desktop
Patch0:		xscorch-DESTDIR.patch
Icon:		xscorch.xpm
URL:		http://velius.chaos2.org/xscorch/
BuildRequires:	gtk+-devel
BuildRequires:	xpm-devel
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xscorch is a clone of the classic DOS game, "Scorched Earth". The
basic goal is to annihilate enemy tanks using overpowered guns :).
Basically, you buy weapons, you target the enemy by adjusting the
angle of your turret and firing power, and you hope to destroy their
tank before they destroy yours.

We cloned this game in Linux because we were bored, and happen to be
great fans of the original game. The game currently has enough
features to make it playable: human and AI gameplay, some destructive
weapons, and shields. Currently, accessories other than shields have
not been implemented.

%prep
%setup -q
%patch -p1

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/pixmaps,%{_applnkdir}/Games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS AUTHORS ChangeLog TODO \
	$RPM_BUILD_ROOT%{_mandir}/man6/*

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/xscorch
%{_applnkdir}/Games/*
%{_datadir}/pixmaps/*
