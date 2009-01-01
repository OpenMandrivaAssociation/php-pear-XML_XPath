%define		_class		XML
%define		_subclass	XPath
%define		_status		devel
%define		_pearname	%{_class}_%{_subclass}

%define		_requires_exceptions pear(../XPath.php)

Summary:	%{_pearname} - XPath/DOM XML manipulation, maneuvering and query interface
Name:		php-pear-%{_pearname}
Version:	1.2.3
Release:	%mkrel 3
License:	PHP License
Group:		Development/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tar.bz2
Patch0:		%{name}-path_fix.patch
URL:		http://pear.php.net/package/XML_XPath/
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	dos2unix
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

In PEAR status of this package is: %{_status}.

%prep

%setup -q -c

find . -type d -perm 0700 -exec chmod 755 {} \;
find . -type f -perm 0555 -exec chmod 755 {} \;
find . -type f -perm 0444 -exec chmod 644 {} \;

for i in `find . -type d -name CVS` `find . -type f -name .cvs\*` `find . -type f -name .#\*`; do
    if [ -e "$i" ]; then rm -rf $i; fi >&/dev/null
done

# strip away annoying ^M
find -type f | grep -v ".gif" | grep -v ".png" | grep -v ".jpg" | xargs dos2unix -U
%patch0 -p1

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_datadir}/pear/%{_class}/{,%{_subclass}}

install %{_pearname}-%{version}/*.php %{buildroot}%{_datadir}/pear/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php %{buildroot}%{_datadir}/pear/%{_class}/%{_subclass}

install -d %{buildroot}%{_datadir}/pear/packages
install -m0644 package.xml %{buildroot}%{_datadir}/pear/packages/%{_pearname}.xml

%post
if [ "$1" = "1" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear install --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi
if [ "$1" = "2" ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear upgrade -f --nodeps -r %{_datadir}/pear/packages/%{_pearname}.xml
	fi
fi

%preun
if [ "$1" = 0 ]; then
	if [ -x %{_bindir}/pear -a -f %{_datadir}/pear/packages/%{_pearname}.xml ]; then
		%{_bindir}/pear uninstall --nodeps -r %{_pearname}
	fi
fi

%clean
rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs/*
%dir %{_datadir}/pear/%{_class}/%{_subclass}
%{_datadir}/pear/%{_class}/*.php
%{_datadir}/pear/%{_class}/%{_subclass}/*.php
%{_datadir}/pear/packages/%{_pearname}.xml


