%define	upstream_name	 Digest-SHA1
%define upstream_version 2.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	20

Summary:	Perl interface to the SHA1 Algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Digest/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel

%description
Digest-SHA1 module for perl.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags} -fPIC"

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto

