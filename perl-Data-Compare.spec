#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Data-Compare
Version  : 1.25
Release  : 3
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Data-Compare-1.25.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Data-Compare-1.25.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Data-Compare-license = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(File::Find::Rule)
BuildRequires : perl(Number::Compare)
BuildRequires : perl(Text::Glob)

%description
This module compares arbitrary data structures to see if they are copies
of each other.

%package dev
Summary: dev components for the perl-Data-Compare package.
Group: Development
Provides: perl-Data-Compare-devel = %{version}-%{release}

%description dev
dev components for the perl-Data-Compare package.


%package license
Summary: license components for the perl-Data-Compare package.
Group: Default

%description license
license components for the perl-Data-Compare package.


%prep
%setup -q -n Data-Compare-1.25

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Compare
cp ARTISTIC.txt %{buildroot}/usr/share/package-licenses/perl-Data-Compare/ARTISTIC.txt
cp GPL2.txt %{buildroot}/usr/share/package-licenses/perl-Data-Compare/GPL2.txt
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.0/Data/Compare.pm
/usr/lib/perl5/vendor_perl/5.28.0/Data/Compare/Plugins.pod
/usr/lib/perl5/vendor_perl/5.28.0/Data/Compare/Plugins/Scalar/Properties.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Compare.3
/usr/share/man/man3/Data::Compare::Plugins.3
/usr/share/man/man3/Data::Compare::Plugins::Scalar::Properties.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Compare/ARTISTIC.txt
/usr/share/package-licenses/perl-Data-Compare/GPL2.txt
