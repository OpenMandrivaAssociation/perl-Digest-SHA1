%define	upstream_name	 Digest-SHA1

%ifarch %{x86_64}
# Workaround for debuginfo bug
%global _debugsource_template %{nil}
%endif

Name:		perl-%{upstream_name}
Version:	2.13
Release:	1

Summary:	Perl interface to the SHA1 Algorithm
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://metacpan.org/release/Digest-SHA1
Source0:	https://cpan.metacpan.org/authors/id/G/GA/GAAS/Digest-SHA1-%{version}.tar.gz

BuildRequires:	perl(Test)
BuildRequires:	perl-devel

%description
Digest-SHA1 module for perl.

%prep
%autosetup -p1 -n %{upstream_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags} -fPIC"

%check
make test

%install
%make_install

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto

