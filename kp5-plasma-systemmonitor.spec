%define		kdeplasmaver	5.24.3
%define		qtver		5.9.0
%define		kpname		plasma-systemmonitor
%define		kf5ver		5.39.0

Summary:	plasma-systemmonitor
Name:		kp5-%{kpname}
Version:	5.24.3
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	982b99a13adc6c36f59974d77608031c
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel >= 5.15.0
BuildRequires:	Qt5Gui-devel >= 5.15.0
BuildRequires:	Qt5Network-devel >= 5.15.0
BuildRequires:	Qt5Qml-devel >= 5.15.2
BuildRequires:	Qt5Quick-devel >= 5.15.0
BuildRequires:	Qt5Widgets-devel >= 5.15.0
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.82
BuildRequires:	kf5-kconfig-devel >= 5.82
BuildRequires:	kf5-kdbusaddons-devel >= 5.82
BuildRequires:	kf5-kdeclarative-devel >= 5.82
BuildRequires:	kf5-kglobalaccel-devel >= 5.82
BuildRequires:	kf5-ki18n-devel >= 5.82
BuildRequires:	kf5-kiconthemes-devel >= 5.82
BuildRequires:	kf5-kio-devel >= 5.82
BuildRequires:	kf5-kitemmodels-devel >= 5.82
BuildRequires:	kf5-knewstuff-devel >= 5.82
BuildRequires:	kf5-kservice-devel >= 5.85.0
BuildRequires:	kp5-libksysguard-devel >= 5.22.5

BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
An application for monitoring system resources.

plasma-systemmonitor provides an interface for monitoring system
sensors, process information and other system resources. It is built
on top of the faces system also used to provide widgets for
plasma-dekstop and makes use of the ksystemstats daemon to provide
sensor information. It allows extensive customisation of pages, so it
can be made to show exactly which data people want to see.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/plasma-systemmonitor
%{_libdir}/qt5/qml/org/kde/ksysguard/page
%{_libdir}/qt5/qml/org/kde/ksysguard/table
%{_desktopdir}/org.kde.plasma-systemmonitor.desktop
%{_datadir}/config.kcfg/systemmonitor.kcfg
%{_datadir}/knsrcfiles/plasma-systemmonitor.knsrc
%{_datadir}/ksysguard/sensorfaces/org.kde.ksysguard.applicationstable
%{_datadir}/ksysguard/sensorfaces/org.kde.ksysguard.processtable
%{_datadir}/plasma-systemmonitor
%dir %{_datadir}/plasma/kinfocenter/externalmodules
%{_datadir}/plasma/kinfocenter/externalmodules/kcm_external_plasma-systemmonitor.desktop
