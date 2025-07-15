Summary:	Piano Teacher
Summary(pl.UTF-8):	Nauka gry na pianinie
Name:		pianobooster
Version:	0.6.4b
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://downloads.sourceforge.net/pianobooster/%{name}-src-%{version}.tar.gz
# Source0-md5:	4c1c34a4b763e6108aa9668be7890696
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-CMakeLists.patch
URL:		http://pianobooster.sourceforge.net/
BuildRequires:	QtCore-devel
BuildRequires:	QtGui-devel
BuildRequires:	QtOpenGL-devel
BuildRequires:	QtXml-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	cmake
BuildRequires:	libstdc++-devel
BuildRequires:	qt4-build
BuildRequires:	qt4-qmake
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
%patch -P0 -p1
%patch -P1 -p0

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
