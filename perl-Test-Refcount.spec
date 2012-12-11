%define upstream_name    Test-Refcount
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Assert reference counts on objects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Devel::FindRef)
BuildRequires: perl(Devel::Refcount)
BuildRequires: perl(Test::Builder)
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(Test::More)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
The Perl garbage collector uses simple reference counting during the normal
execution of a program. This means that cycles or unweakened references in
other parts of code can keep an object around for longer than intended. To
help avoid this problem, the reference count of a new object from its class
constructor ought to be 1. This way, the caller can know the object will be
properly DESTROYed when it drops all of its references to it.

This module provides two test functions to help ensure this property holds
for an object class, so as to be polite to its callers.

If the assertion fails; that is, if the actual reference count is different
to what was expected, a trace of references to the object is printed, using
Marc Lehmann's the Devel::FindRef manpage module. See the examples below
for more information.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)

%{_mandir}/man3/*
%perl_vendorlib/*




%changelog
* Sun Apr 22 2012 Götz Waschk <waschk@mandriva.org> 0.70.0-2mdv2012.0
+ Revision: 792690
- update build deps
- yearly rebuild

* Wed Apr 20 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.70.0-1
+ Revision: 656227
- update to 0.07

* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2
+ Revision: 654317
- rebuild for updated spec-helper

* Fri Nov 27 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 470460
- update to 0.06

* Fri Nov 27 2009 Götz Waschk <waschk@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 470452
- update to new version 0.06

* Fri Jul 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 394270
- update to 0.05

* Mon Jun 29 2009 Götz Waschk <waschk@mandriva.org> 0.40.0-1mdv2010.0
+ Revision: 390501
- import perl-Test-Refcount


* Mon Jun 29 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist

