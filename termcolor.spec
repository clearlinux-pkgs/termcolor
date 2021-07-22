#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : termcolor
Version  : 1.1.0
Release  : 45
URL      : http://pypi.debian.net/termcolor/termcolor-1.1.0.tar.gz
Source0  : http://pypi.debian.net/termcolor/termcolor-1.1.0.tar.gz
Summary  : ANSII Color formatting for output in terminal.
Group    : Development/Tools
License  : MIT
Requires: termcolor-license = %{version}-%{release}
Requires: termcolor-python = %{version}-%{release}
Requires: termcolor-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3

%description
=======

%package license
Summary: license components for the termcolor package.
Group: Default

%description license
license components for the termcolor package.


%package python
Summary: python components for the termcolor package.
Group: Default
Requires: termcolor-python3 = %{version}-%{release}

%description python
python components for the termcolor package.


%package python3
Summary: python3 components for the termcolor package.
Group: Default
Requires: python3-core
Provides: pypi(termcolor)

%description python3
python3 components for the termcolor package.


%prep
%setup -q -n termcolor-1.1.0
cd %{_builddir}/termcolor-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1603405608
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/termcolor
cp %{_builddir}/termcolor-1.1.0/COPYING.txt %{buildroot}/usr/share/package-licenses/termcolor/d13c76eb20f5b9385b648bdfad643c238797118d
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/termcolor/d13c76eb20f5b9385b648bdfad643c238797118d

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
