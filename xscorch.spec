Summary:	Xscorch - clone of the classic DOS game "Scorched Earth"
Summary(pl):	Xscorch - klon klasycznej gry "Scorched Earth"
Name:		xscorch
Version:	0.2.0
Release:	1
License:	GPL
Group:		X11/Applications/Games
Source0:	http://chaos2.org/xscorch/%{name}-%{version}.tar.gz
# Source0-md5:	42862dbde1d0ebf87be30f7e04462a66
Source1:	%{name}.png
Source2:	%{name}.desktop
Icon:		xscorch.xpm
URL:		http://chaos2.org/xscorch/
BuildRequires:	automake
BuildRequires:	gtk+2-devel >= 2.2.0
#BuildRequires:	libmikmod-devel >= 3.1.9
BuildRequires:	pkgconfig >= 0.7
BuildRequires:	readline-devel
Requires:	gtk+2 >= 2.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Xscorch is a clone of the classic DOS game, "Scorched Earth". The
basic goal is to annihilate enemy tanks using overpowered guns :).
Basically, you buy weapons, you target the enemy by adjusting the
angle of your turret and firing power, and you hope to destroy their
tank before they destroy yours.

%description -l pl
Xscorch to klon klasycznej gry "Scorched Earth". Celem gry jest
zniszczenie czo³gów przeciwników przy pomocy naprawdê mocnych broni
:-). Po prostu kupujesz broñ, celujesz do przeciwnika ustawiaj±c k±t
podniesienia lufy oraz si³ê strza³u i masz nadziejê, ¿e zniszczysz ich
czo³gi, zanim oni zniszcz± twój.

%prep
%setup -q

%build
cp -f /usr/share/automake/config.sub .
# sound disabled - it's useless (no sound files yet), so there is no
# reason to require libmikmod
%configure \
	--enable-network \
	--disable-sound \
	--without-gtk-12

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man6/*
%{_datadir}/xscorch
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*
