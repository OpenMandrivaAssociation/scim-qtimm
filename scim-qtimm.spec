%define version	0.9.4
%define release	%mkrel 10

%define libname_orig lib%{name}
%define libname %mklibname %{name} 0

# require a qtimm aware qt library:
%define qt_version 3.3.6-14mdk
%define scim_version	1.4.2
%define skim_version	1.4.1

Name:		scim-qtimm
Summary:	SCIM context plugin for qt-immodule
Version:	%{version}
Release:	%{release}
Group:		System/Internationalization
License:	GPLv2+
URL:		https://sf.net/projects/scim
Source0:	%{name}-%{version}.tar.bz2
Patch0:		scim-qtimm-0.9.4-use-mandriva-qtdir.patch
Patch1:		%{name}-0.9.4-fix-crash.patch
Patch2:		%{name}-0.9.4-keyboard-layout.patch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
Requires:	scim   >= %{scim_version}
Requires:	%{mklibname qt 3} >= %qt_version

BuildRequires:	scim-devel >= %{scim_version}
BuildRequires:	skim-devel >= %{skim_version}
BuildRequires:	qt3-devel  >= %qt_version

Obsoletes:       libscim-qtimm
Provides:        libscim-qtimm

%description
SCIM context plugin for qt-immodule.


%prep
%setup -q
%patch0 -p0
%patch1 -p1
%patch2 -p1

%build
%define __libtoolize /bin/true
%configure2_5x --disable-debug --with-qt-dir=%{qt3dir} --with-qt-libraries=%{qt3lib} --with-qt-includes=%{qt3include}
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# remove unneeded files
rm -f %{buildroot}%{qt3plugins}/inputmethods/*.la
rm -f %{buildroot}%{_libdir}/kde3/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog NEWS README
%{qt3plugins}/inputmethods/*.so
