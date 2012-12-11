%define		_class		XML
%define		_subclass	XPath
%define		upstream_name	%{_class}_%{_subclass}

%define		_requires_exceptions pear(../XPath.php)

Name:		php-pear-%{upstream_name}
Version:	1.2.4
Release:	%mkrel 5
Summary:	XPath/DOM XML manipulation, maneuvering and query interface
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/XML_XPath/
Source0:	http://pear.php.net/get/%{upstream_name}-%{version}.tgz
Patch0:		XML_XPath-1.2.4-fix-path.patch
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildRequires:	php-pear
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
The PEAR::XML_XPath class provides an XPath/DOM XML manipulation,
maneuvering and query interface.

The class allows for easy manipulation, maneuvering and querying of a
DOMXML tree using both XPath queries and DOM walk functions. It uses
an internal pointer for all methods on which the action is performed.
Results from an DOM/XPath query are returned as an XPath_Result
object, which contains an internal array of DOM nodes and which
extends the common DOM class and hence contains all the DOM functions
from the main object to run on each of the elements in the internal
array. This class tries to hold as close as possible to the DOM
Recommendation. You MUST have the domxml extension to use this class.

The XML_XPath class was inspired by a class maintained by Nigel
Swinson called phpxpath. The phpxpath class does not rely on PHP
xmldom functions and is therefore a sibling to this class:
http://sourceforge.net/projects/phpxpath/.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml
%patch0 -p0

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-5mdv2011.0
+ Revision: 679616
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.4-4mdv2011.0
+ Revision: 613801
- the mass rebuild of 2010.1 packages

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.4-3mdv2010.1
+ Revision: 466308
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.4-2mdv2010.0
+ Revision: 441770
- rebuild

* Sun Mar 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.4-1mdv2009.1
+ Revision: 355266
- new version
- don't recompress tarball
- don't duplicate spec-helper job
- spec cleanup

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-3mdv2009.1
+ Revision: 323000
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-2mdv2009.0
+ Revision: 237174
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1mdv2007.0
+ Revision: 82964
- Import php-pear-XML_XPath

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.3-1mdk
- 1.2.3
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-6mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-5mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-4mdk
- fix deps

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.1-1mdk
- initial Mandriva package (PLD import)

