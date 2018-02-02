#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : termcolor
Version  : 1.1.0
Release  : 19
URL      : http://pypi.debian.net/termcolor/termcolor-1.1.0.tar.gz
Source0  : http://pypi.debian.net/termcolor/termcolor-1.1.0.tar.gz
Summary  : ANSII Color formatting for output in terminal.
Group    : Development/Tools
License  : MIT
Requires: termcolor-legacypython
Requires: termcolor-python3
Requires: termcolor-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======

%package legacypython
Summary: legacypython components for the termcolor package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the termcolor package.


%package python
Summary: python components for the termcolor package.
Group: Default
Requires: termcolor-legacypython
Requires: termcolor-python3

%description python
python components for the termcolor package.


%package python3
Summary: python3 components for the termcolor package.
Group: Default
Requires: python3-core

%description python3
python3 components for the termcolor package.


%prep
%setup -q -n termcolor-1.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507179743
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
export SOURCE_DATE_EPOCH=1507179743
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
