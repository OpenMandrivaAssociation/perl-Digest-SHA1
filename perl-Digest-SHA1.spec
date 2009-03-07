%define	real_name	Digest-SHA1
%define	name		perl-%real_name
%define	version	2.11
%define	release	%mkrel 6

Summary:	Perl interface to the SHA1 Algorithm
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Digest/%{real_name}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{real_name}/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot

%description
Digest-SHA1 module for perl.

%prep
%setup -q -n %{real_name}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto

