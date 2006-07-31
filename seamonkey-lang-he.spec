%define	_lang	he
%define	_reg	IL
%define _lare	%{_lang}-%{_reg}
Summary:	Hebraic resources for SeaMonkey
Summary(pl):	Hebrajskie pliki jêzykowe dla SeaMonkeya
Name:		seamonkey-lang-%{_lang}
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ftp.mozilla.org/pub/mozilla.org/seamonkey/releases/%{version}/contrib-localized/seamonkey-%{version}.%{_lare}.langpack.xpi
# Source0-md5:	148845cbd46a51b7741dd975c4f6f2a4
Source1:	gen-installed-chrome.sh
URL:		http://www.mozilla.org/projects/seamonkey/
BuildRequires:	unzip
BuildRequires:	util-linux
Requires(post,postun):	seamonkey >= %{version}
Requires(post,postun):	textutils
Requires:	seamonkey >= %{version}
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_chromedir	%{_datadir}/seamonkey/chrome

%description
Hebraic resources for SeaMonkey.

%description -l pl
Hebrajskie pliki jêzykowe dla SeaMonkeya.

%prep
%setup -q -c
install %{SOURCE1} .
./gen-installed-chrome.sh locale bin/chrome/{%{_reg},%{_lare},%{_lang}-unix}.jar \
	> lang-%{_lang}-installed-chrome.txt

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install bin/chrome/{%{_reg},%{_lare},%{_lang}-unix}.jar $RPM_BUILD_ROOT%{_chromedir}
install lang-%{_lang}-installed-chrome.txt $RPM_BUILD_ROOT%{_chromedir}
cp -r bin/{searchplugins,defaults} $RPM_BUILD_ROOT%{_datadir}/seamonkey

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{_sbindir}/seamonkey-chrome+xpcom-generate

%postun
%{_sbindir}/seamonkey-chrome+xpcom-generate

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_reg}.jar
%{_chromedir}/%{_lare}.jar
%{_chromedir}/%{_lang}-unix.jar
%{_chromedir}/lang-%{_lang}-installed-chrome.txt
%{_datadir}/seamonkey/searchplugins/*
%{_datadir}/seamonkey/defaults/messenger/%{_reg}
%{_datadir}/seamonkey/defaults/profile/%{_reg}
