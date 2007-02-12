#%include	/usr/lib/rpm/macros.python
Summary:	Mirrors management tool
Summary(pl.UTF-8):   Narzędzie do zarządzania mirrorami
Name:		mirrortool
Version:	0.1
Release:	2
License:	GPL
Group:		Applications/System
Source0:	http://team.pld.org.pl/~mis/download/%{name}-%{version}.tar.gz
# Source0-md5:	4c1c591fb2563dae351d1dae2b7fa77f
BuildRequires:	perl-base
BuildRequires:	python-devel >= 1.5.2
Requires:	python-modules
Requires:	python >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program takes list of mirror sites from MIRRORS[.gz] file and allows
to processing it by extension modules. Available modules:

- mod_poldek - module to configure poldek (http://poldek.pld.org.pl/)
  sources
- mod_xml_pldoc - module to generate PLD-Guide
  (http://cvs.pld.org.pl/PLD-Guide/) document with list of PLD mirrors
- mod_html - module to generate simple HTML document

%description -l pl.UTF-8
Program pobiera listę serwerów lustrzanych z pliku MIRRORS[.gz] i
pozwala na jej przetworzenie przez zewnętrzne moduły. Dostępne moduły:

- mod_poldek - moduł do konfiguracji poldka
  (http://poldek.pld.org.pl/)
- mod_xml_pldoc - moduł do generowania dokumentu PLD-Guide
  (http://cvs.pld.org.pl/PLD-Guide/) z listą mirrorów PLD
- mod_html - moduł do generowania prostego dokumentu HTML.

%prep
%setup -q

%build
# distribute in source form cause to program alpha stage --
# sources are easier to read and fix.
#%%{py_comp} .

# while waiting for http://ftp.pld.org.pl/MIRRORS.gz...
%{__perl} -pi -e 's|^\s*url\s*=.+|url = http://team.pld.org.pl/~mis/pld/MIRRORS.gz|' %{name}.conf

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc MIRRORS README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.sh
%{_libdir}/%{name}/*.py*
