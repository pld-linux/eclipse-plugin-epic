
%define		_plug_name	epic
%define		_rel_ver	0.3.0
%define		_rel_date	20040711

Summary:	EPIC - Eclipse Perl Integration
Summary(pl):	EPIC - wtyczka do ¶rodowiska Eclipse u³atwiaj±ca programowanie w Perlu
Name:		eclipse-plugin-%{_plug_name}
Version:	%{_rel_ver}
Release:	0.1
License:	CPL v1.0
Group:		Development/Languages
Source0:	http://dl.sourceforge.net/e-p-i-c/org.%{_plug_name}.updatesite_%{version}_%{_rel_date}.zip
# Source0-md5:	5ab8b866c599bd41f8dcb57564d5bc2d
URL:		http://e-p-i-c.sourceforge.net/
BuildRequires:	unzip
Requires:	eclipse >= 3.0
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

%description -l pl
EPIC to opensource'owe IDE dla Perla zbudowane na bazie ¶rodowiska
Eclipse. Oferuje pod¶wietlanie sk³adni, sprawdzanie poprawno¶ci
podczas pisania, wsparcie dla stosowania szablonów oraz debugger
Perla. Zawiera tak¿e wtyczkê do obs³ugi wyra¿eñ regularnych oraz
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
