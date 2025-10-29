%define plasmaver %(echo %{version} |cut -d. -f1-3)
%define stable %([ "$(echo %{version} |cut -d. -f2)" -ge 80 -o "$(echo %{version} |cut -d. -f3)" -ge 80 ] && echo -n un; echo -n stable)
#define git 20240222
%define gitbranch Plasma/6.0
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")

Summary: Library for scheduling the dark-light cycle
Name: knighttime
Version: 6.5.1
Release: %{?git:0.%{git}.}1
URL: https://kde.org/
License: GPL
Group: System/Libraries
%if 0%{?git:1}
Source0:	https://invent.kde.org/plasma/knighttime/-/archive/%{gitbranch}/knighttime-%{gitbranchd}.tar.bz2#/knighttime-%{git}.tar.bz2
%else
Source0: http://download.kde.org/%{stable}/plasma/%{plasmaver}/knighttime-%{version}.tar.xz
%endif

BuildSystem:	cmake
BuildOption:	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON

BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6GuiTools)
BuildRequires:	cmake(Qt6Positioning)
BuildRequires:	cmake(Qt6DBusTools)
BuildRequires:	cmake(Qt6QmlTools)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6CoreTools)
BuildRequires:	cmake(Qt6Tools)
BuildRequires:	cmake(Qt6ToolsTools)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6DBusAddons)
BuildRequires:	cmake(KF6Holidays)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(Qt6Test)

%description
Library for scheduling the dark-light cycle

%install -a
%libpackages

%files
%{_libdir}/libexec/knighttimed
%{_datadir}/applications/org.kde.knighttimed.desktop
%{_datadir}/dbus-1/interfaces/org.kde.NightTime.xml
%{_datadir}/dbus-1/services/org.kde.NightTime.service
%{_datadir}/qlogging-categories6/knighttime.categories
%{_prefix}/lib/systemd/user/plasma-knighttimed.service
