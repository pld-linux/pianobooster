Summary:	Piano Teacher
Summary(pl.UTF-8):	Nauka gry na pianinie
Name:		pianobooster
Version:	0.6.4
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/pianobooster/%{name}-src-%{version}.tar.gz
# Source0-md5:	af1bb513c93ac7b1c8cc919b60146d1c
Patch0:		%{name}-desktop.patch
URL:		http://pianobooster.sourceforge.net/
BuildRequires:	cmake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PianoBooster is a fun way of playing along with a musical
accompaniment and at the same time learning the basics of reading
musical notation. The difference between playing along to a CD or a
standard midi file is that PianoBooster listens and follows what you
are playing on a midi piano keyboard.

%description -l pl.UTF-8
PianoBooster pozwala na granie muzyki z akompaniamentem, a przy okazji
uczy podstaw odczytu notatcji muzycznej. W odróżnieniu od odtwarzania
muzyki na odtwarzaczu CD lub zwykłego pliki midi, PianoBooster reaguje
na grę użytkownika korzystającego z muzycznej klawiatury midi.

%prep
%setup -q -n %{name}-src-%{version}
%patch0 -p1

%build
cd build
%cmake ../src \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64
%endif

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt
%attr(755,root,root) %{_bindir}/pianobooster
%{_desktopdir}/pianobooster.desktop
%{_pixmapsdir}/pianobooster.png