#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-svm
Version  : 0.2.3
Release  : 5
URL      : https://pecl.php.net//get/svm-0.2.3.tgz
Source0  : https://pecl.php.net//get/svm-0.2.3.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: php-svm-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
[![Build Status](https://travis-ci.com/ianbarber/php-svm.svg?branch=master)](https://travis-ci.com/ianbarber/php-svm) (Travis)

%package lib
Summary: lib components for the php-svm package.
Group: Libraries

%description lib
lib components for the php-svm package.


%prep
%setup -q -n svm-0.2.3
cd %{_builddir}/svm-0.2.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20190902/svm.so