
%define		_plug_name	epic
%define		_rel_ver	0.6.13
%define		_rel_date	20070808

Summary:	EPIC - Eclipse Perl Integration
Summary(pl.UTF-8):	EPIC - wtyczka do środowiska Eclipse ułatwiająca programowanie w Perlu
Name:		eclipse-plugin-%{_plug_name}
Version:	%{_rel_ver}
Release:	1
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/e-p-i-c/org.%{_plug_name}.updatesite_%{version}_%{_rel_date}.zip
# Source0-md5:	8f1d7fa06c276084bba71ca4187e86f1
URL:		http://www.epic-ide.org/
BuildRequires:	unzip
Requires:	eclipse >= 3.1
ExclusiveArch:	%{ix86} ppc ia64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_eclipse_arch	%(echo %{_target_cpu} | sed 's/i.86/x86/;s/athlon/x86/;s/pentium./x86/')
%define		_eclipsedir  	%{_libdir}/eclipse

%description
EPIC is an opensource Perl IDE for the Eclipse platform. Features
supported are syntax highlighting, on the fly syntax check, content
assist, perldoc support, source formatter, templating support and a
Perl debugger. A regular expression plugin and support for the eSpell
spellchecker are also available.

%description -l pl.UTF-8
EPIC to opensource'owe IDE dla Perla zbudowane na bazie środowiska
Eclipse. Oferuje podświetlanie składni, sprawdzanie poprawności
podczas pisania, wsparcie dla stosowania szablonów oraz debugger
Perla. Zawiera także wtyczkę do obsługi wyrażeń regularnych oraz
wsparcie dla eSpella.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_eclipsedir}/{features,plugins}

cp -r org.epic.updatesite/plugins/* $RPM_BUILD_ROOT%{_eclipsedir}/plugins
cp -r org.epic.updatesite/features/* $RPM_BUILD_ROOT%{_eclipsedir}/features

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_eclipsedir}/features
%{_eclipsedir}/features/org.epic.*.jar
%dir %{_eclipsedir}/plugins
%{_eclipsedir}/plugins/org.epic.*.jar
