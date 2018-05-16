#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : termcolor
Version  : 1.1.0
Release  : 22
URL      : http://pypi.debian.net/termcolor/termcolor-1.1.0.tar.gz
Source0  : http://pypi.debian.net/termcolor/termcolor-1.1.0.tar.gz
Summary  : ANSII Color formatting for output in terminal.
Group    : Development/Tools
License  : MIT
Requires: termcolor-python3
Requires: termcolor-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
=======

%package python
Summary: python components for the termcolor package.
Group: Default
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
export SOURCE_DATE_EPOCH=1523308568
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
