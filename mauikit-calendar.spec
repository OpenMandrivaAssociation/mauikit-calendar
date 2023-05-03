%define libname %mklibname mauikit-calendar
%define devname %mklibname -d mauikit-calendar

Name:		mauikit-calendar
Version:	1.0.1
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Calendar support components for Maui applications
Url:		http://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-calendar/-/archive/%{?snapshot:master/mauikit-calendar-master.tar.bz2#/mauikit-calendar-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-calendar-v%{version}.tar.bz2}

License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit)
BuildRequires:	cmake(Qt5Qml)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Notifications)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5ConfigWidgets)
BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5Plasma)
BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(KF5WindowSystem)
BuildRequires:  cmake(KF5Akonadi)
BuildRequires:  cmake(KF5AkonadiCalendar)
BuildRequires:  cmake(KF5AkonadiContact)
BuildRequires:  cmake(KF5CalendarSupport)
BuildRequires:  cmake(KF5CalendarCore)
BuildRequires:  cmake(KF5EventViews)
BuildRequires:  cmake(KF5Contacts)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF5SyntaxHighlighting)
BuildRequires:	cmake(KF5Attica)
BuildRequires:	cmake(Qt5)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5WebEngine)
BuildRequires:	qt5-qtgraphicaleffects
BuildRequires:	qt5-qtdeclarative
BuildRequires:	qt5-qtquickcontrols2
Requires:	qt5-qtquickcontrols2
Requires:	qt5-qtgraphicaleffects
Requires:	%{libname} = %{EVRD}

%description
Calendar support with multiple time and date-related controls.

Kit for developing MAUI Apps.
MauiKit is a set of utilities and "templated" controls based on Kirigami and QCC2 that follow the ongoing work on the Maui HIG.
It let you quickly create a Maui application and access utilities and widgets shared among the other Maui apps.


%package -n %{libname}
Summary:	Shared library for MauiKit Calendar
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libname}
Calendar support with multiple time and date-related controls.

Kit for developing MAUI Apps.
MauiKit is a set of utilities and "templated" controls based on Kirigami and QCC2 that follow the ongoing work on the Maui HIG.
It let you quickly create a Maui application and access utilities and widgets shared among the other Maui apps.

%package -n %{devname}
Summary:	Development files for mauikit-calendar
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Calendar support with multiple time and date-related controls.

Kit for developing MAUI Apps.
MauiKit is a set of utilities and "templated" controls based on Kirigami and QCC2 that follow the ongoing work on the Maui HIG.
It let you quickly create a Maui application and access utilities and widgets shared among the other Maui apps.


%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files