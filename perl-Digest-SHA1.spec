%define	upstream_name	 Digest-SHA1
%define upstream_version 2.13

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	14

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
%make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc README Changes
%{_mandir}/*/*
%{perl_vendorarch}/Digest
%{perl_vendorarch}/auto


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 2.130.0-7mdv2012.0
+ Revision: 765190
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 2.130.0-6
+ Revision: 763706
- rebuilt for perl-5.14.x
- cleanup temporary deps, this was added in perl-devel instead

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 2.130.0-5
+ Revision: 763242
- force it
- rebuild

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 2.130.0-4
+ Revision: 667123
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 2.130.0-3mdv2011.0
+ Revision: 564431
- rebuild for perl 5.12.1

* Tue Jul 20 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.130.0-2mdv2011.0
+ Revision: 555247
- rebuild

* Wed Jul 14 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.130.0-1mdv2011.0
+ Revision: 553126
- update to 2.13

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 2.120.0-1mdv2010.1
+ Revision: 406347
- rebuild using %%perl_convert_version

* Sun May 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.12-1mdv2010.0
+ Revision: 379207
- update to new version 2.12

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 2.11-6mdv2009.1
+ Revision: 351717
- rebuild

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 2.11-5mdv2009.0
+ Revision: 223660
- rebuild

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 2.11-4mdv2008.1
+ Revision: 151159
- rebuild for perl 5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 2.11-3mdv2008.0
+ Revision: 23413
- rebuild


* Fri May 19 2006 Scott Karns <scottk@mandriva.org> 2.11-2mdk
- Updated spec to use mkrel macro
- Updated source URL to comply with Mandriva perl packaging policy

* Wed Jan 25 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 2.11-1mdk
- 2.11
- spec cleanup

* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 2.10-3mdk
- Rebuild

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.10-2mdk
- rebuild for new perl; clean up spec

* Tue Apr 13 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 2.10-1mdk
- 2.10.

* Thu Aug 21 2003 François Pons <fpons@mandrakesoft.com> 2.04-1mdk
- 2.04.

* Wed Aug 13 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 2.02-3mdk
- rebuild for new perl
- drop Prefix tag
- don't use PREFIX
- use %%makeinstall_std macro
- use %%make macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 2.02-2mdk
- rebuild for new auto{prov,req}

