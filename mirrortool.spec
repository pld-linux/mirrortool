
#%include	/usr/lib/rpm/macros.python

Summary:	Mirrors management tool
Summary(pl):	Narzêdzie do zarz±dzania mirrorami
Name:		mirrortool
Version:	0.1
Release:	2
License:	GPL
Source0:	http://team.pld.org.pl/~mis/download/%{name}-%{version}.tar.gz
Group:		Applications/System
Requires:	python >= 2.0
Requires:	python-modules
BuildRequires:	python-devel >= 1.5.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program takes list of mirror sites from MIRRORS[.gz] file and allows
to processing it by extension modules. Available modules: 

* mod_poldek - module to configure poldek (http://poldek.pld.org.pl/)
  sources
* mod_xml_pldoc - module to generate PLD-Guide 
  (http://cvs.pld.org.pl/PLD-Guide/) document with list of PLD mirrors
* mod_html  - module to generate simple HTML document

%description -l pl
Program pobiera listê serwerów lustrzanych z pliku MIRRORS[.gz] i
pozwala na jej przetworzenie przez zewnêtrzne modu³y. Dostêpne modu³y:

* mod_poldek - modu³ do konfiguracji poldka
  (http://poldek.pld.org.pl/)
* mod_xml_pldoc - modu³ do generowania dokumentu PLD-Guide
  (http://cvs.pld.org.pl/PLD-Guide/) z list± mirrorów PLD
* mod_html - modu³ do generowania prostego dokumentu HTML.

%prep
%setup -q

%build
# distribute in source form cause to program alpha stage --
# sources are easier to read and fix.
#%{py_comp} .

# while waiting for http://ftp.pld.org.pl/MIRRORS.gz...
perl -pi -e 's|^\s*url\s*=.+|url = http://team.pld.org.pl/~mis/pld/MIRRORS.gz|' %{name}.conf

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf MIRRORS README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{_sysconfdir}/%{name}.conf
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/*.sh
%attr(644,root,root) %{_libdir}/%{name}/*.py*
