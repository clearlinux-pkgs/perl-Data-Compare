#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Data-Compare
Version  : 1.29
Release  : 37
URL      : https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Data-Compare-1.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DC/DCANTRELL/Data-Compare-1.29.tar.gz
Summary  : unknown
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Data-Compare-license = %{version}-%{release}
Requires: perl-Data-Compare-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Clone)
BuildRequires : perl(File::Find::Rule)
BuildRequires : perl(Number::Compare)
BuildRequires : perl(Text::Glob)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
This module compares arbitrary data structures to see if they are copies
of each other.

%package dev
Summary: dev components for the perl-Data-Compare package.
Group: Development
Provides: perl-Data-Compare-devel = %{version}-%{release}
Requires: perl-Data-Compare = %{version}-%{release}

%description dev
dev components for the perl-Data-Compare package.


%package license
Summary: license components for the perl-Data-Compare package.
Group: Default

%description license
license components for the perl-Data-Compare package.


%package perl
Summary: perl components for the perl-Data-Compare package.
Group: Default
Requires: perl-Data-Compare = %{version}-%{release}

%description perl
perl components for the perl-Data-Compare package.


%prep
%setup -q -n Data-Compare-1.29
cd %{_builddir}/Data-Compare-1.29

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Data-Compare
cp %{_builddir}/Data-Compare-%{version}/ARTISTIC.txt %{buildroot}/usr/share/package-licenses/perl-Data-Compare/be0627fff2e8aef3d2a14d5d7486babc8a4873ba || :
cp %{_builddir}/Data-Compare-%{version}/GPL2.txt %{buildroot}/usr/share/package-licenses/perl-Data-Compare/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Data::Compare.3
/usr/share/man/man3/Data::Compare::Plugins.3
/usr/share/man/man3/Data::Compare::Plugins::Scalar::Properties.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Data-Compare/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/perl-Data-Compare/be0627fff2e8aef3d2a14d5d7486babc8a4873ba

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
