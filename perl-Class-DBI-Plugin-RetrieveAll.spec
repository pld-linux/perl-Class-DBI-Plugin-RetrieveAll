#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Class
%define		pnam	DBI-Plugin-RetrieveAll
%include	/usr/lib/rpm/macros.perl
Summary:	Determine type information for columns
Summary(pl.UTF-8):	Określanie informacji o typie dla kolumn
Name:		perl-Class-DBI-Plugin-RetrieveAll
Version:	1.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	859fe774e6d74636b6406b821d4d66d1
URL:		http://search.cpan.org/dist/Class-DBI-Plugin-RetrieveAll/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-DBI
BuildRequires:	perl-DBD-SQLite
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module allows Class::DBI-based classes to query their columns for
data type information in a database-independent manner.

%description -l pl.UTF-8
Ten moduł pozwala klasom opartym na Class::DBI na odpytywanie kolumn o
informacje o typie w sposób niezależny od bazy danych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make}
%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Class/DBI/Plugin/*
%{_mandir}/man3/*
