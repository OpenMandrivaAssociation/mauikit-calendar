%define libname %mklibname MauiKitCalendar
%define devname %mklibname -d MauiKitCalendar

Name:		mauikit-calendar
Version:	4.0.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Calendar support components for Maui applications
Url:		https://mauikit.org/
Source0:	https://invent.kde.org/maui/mauikit-calendar/-/archive/%{?snapshot:master/mauikit-calendar-master.tar.bz2#/mauikit-calendar-%{snapshot}.tar.bz2}%{!?snapshot:v%{version}/mauikit-calendar-v%{version}.tar.bz2}


License:	LGPL-2.1-or-later, CC0 1.0, BSD-2-Clause
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:  cmake(MauiKit4)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6Sql)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(KF6I18n)
BuildRequires:	cmake(KF6Notifications)
BuildRequires:	cmake(KF6Config)
BuildRequires:	cmake(KF6Service)
BuildRequires:	cmake(KF6KIO)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6ConfigWidgets)
#BuildRequires:	cmake(KDecoration2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Declarative)
#BuildRequires:	cmake(KF6Plasma)
#BuildRequires:	cmake(KF5PlasmaQuick)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(KF6WindowSystem)
#BuildRequires:  akonadi-devel
#BuildRequires:  cmake(KF6AkonadiMime)
BuildRequires:  cmake(KPim6AkonadiCalendar)
#BuildRequires:  cmake(KPim6AkonadiContact)
BuildRequires:  cmake(KPim6CalendarSupport)
BuildRequires:  cmake(KPim6CalendarUtils)
BuildRequires:  cmake(KF6CalendarCore)
#BuildRequires:  cmake(KF5EventViews)
BuildRequires:  cmake(KF6Contacts)
BuildRequires:	cmake(Git)
BuildRequires:	cmake(KF6SyntaxHighlighting)
BuildRequires:	cmake(KF6Attica)
BuildRequires:	cmake(Qt6)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6WebEngineCore)


BuildRequires: plasma6-akonadi-calendar

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

%files -n %{libname}
%{_libdir}/libMauiKitCalendar4.so*
%{_libdir}/qt6/qml/org/mauikit/calendar

%package -n %{devname}
Summary:	Development files for mauikit-calendar
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}

%description -n %{devname}
Calendar support with multiple time and date-related controls.

Kit for developing MAUI Apps.
MauiKit is a set of utilities and "templated" controls based on Kirigami and QCC2 that follow the ongoing work on the Maui HIG.
It let you quickly create a Maui application and access utilities and widgets shared among the other Maui apps.

%files -n %{devname}
%{_includedir}/MauiKit4/Calendar
%{_libdir}/cmake/MauiKitCalendar4

%prep
%autosetup -p1 -n %{name}-%{?snapshot:master}%{!?snapshot:v%{version}}
%cmake_kde5

%build
%ninja_build -C build

%install
%ninja_install -C build
%find_lang mauikitcalendar

%files -f mauikitcalendar.lang
