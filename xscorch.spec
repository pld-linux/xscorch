Summary:	Xscorch - clone of the classic DOS game "Scorched Earth"
Summary(pl):	Xscorch - klon klasycznej gry "Scorched Earth"
Name:		xscorch
Version:	0.1.14
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://velius.chaos2.org/xscorch/%{name}-%{version}.tar.gz
Source1:	%{name}.png
Source2:	%{name}.desktop
Icon:		xscorch.xpm
URL:		http://velius.chaos2.org/xscorch/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Xscorch is a clone of the classic DOS game, "Scorched Earth". The
basic goal is to annihilate enemy tanks using overpowered guns :).
Basically, you buy weapons, you target the enemy by adjusting the
angle of your turret and firing power, and you hope to destroy their
tank before they destroy yours.

%description -l pl
Xscorch to klon klasycznej gry "Scorched Earth". Celem gry jest
zniszczenie czo�g�w przeciwnik�w przy pomocy naprawd� mocnych broni
:-). Po prostu kupujesz bro�, celujesz do przeciwnika ustawiaj�c k�t
podniesienia lufy oraz si�� strza�u i masz nadziej�, �e zniszczysz ich
czo�gi, zanim oni zniszcz� tw�j.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--enable-network
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/pixmaps,%{_applnkdir}/Games}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps
install %{SOURCE2} $RPM_BUILD_ROOT%{_applnkdir}/Games

gzip -9nf README NEWS AUTHORS ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/xscorch
%{_applnkdir}/Games/*
%{_pixmapsdir}/*
