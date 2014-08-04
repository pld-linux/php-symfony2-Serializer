%define		pearname	Serializer
%define		php_min_version 5.3.3
%include	/usr/lib/rpm/macros.php
Summary:	Symfony2 Serializer Component
Name:		php-symfony2-Serializer
Version:	2.4.8
Release:	1
License:	MIT
Group:		Development/Languages/PHP
Source0:	https://github.com/symfony/%{pearname}/archive/v%{version}/%{pearname}-%{version}.tar.gz
# Source0-md5:	b8290f40acc011d3de2e34f9c82d2319
URL:		http://symfony.com/doc/2.4/components/serializer.html
BuildRequires:	phpab
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.610
Requires:	php(core) >= %{php_min_version}
Requires:	php(ctype)
Requires:	php(dom)
Requires:	php(json)
Requires:	php(pcre)
Requires:	php(simplexml)
Requires:	php(spl)
Requires:	php(xml)
Requires:	php-pear >= 4:1.3.10
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Serializer Component is meant to be used to turn objects into a
specific format (XML, JSON, Yaml, ...) and the other way around.

%prep
%setup -q -n %{pearname}-%{version}

%build
phpab -n -e '*/Tests/*' -o autoload.php .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
cp -a *.php */ $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}
rm -r $RPM_BUILD_ROOT%{php_pear_dir}/Symfony/Component/%{pearname}/Tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md LICENSE README.md
%dir %{php_pear_dir}/Symfony/Component/Serializer
%{php_pear_dir}/Symfony/Component/Serializer/*.php
%{php_pear_dir}/Symfony/Component/Serializer/Encoder
%{php_pear_dir}/Symfony/Component/Serializer/Exception
%{php_pear_dir}/Symfony/Component/Serializer/Normalizer
