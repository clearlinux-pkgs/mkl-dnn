#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mkl-dnn
Version  : 0.16
Release  : 4
URL      : https://github.com/intel/mkl-dnn/archive/v0.16.tar.gz
Source0  : https://github.com/intel/mkl-dnn/archive/v0.16.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: mkl-dnn-lib
Requires: mkl-dnn-license
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : glibc-dev
Patch1: no-native.patch

%description
> Intel MKL-DNN repository migrated to [https://github.com/intel/mkl-dnn](https://github.com/intel/mkl-dnn).
> The old address will continue to be available and will redirect to the new repo.
> Please update your links.

%package dev
Summary: dev components for the mkl-dnn package.
Group: Development
Requires: mkl-dnn-lib = %{version}-%{release}
Provides: mkl-dnn-devel = %{version}-%{release}

%description dev
dev components for the mkl-dnn package.


%package lib
Summary: lib components for the mkl-dnn package.
Group: Libraries
Requires: mkl-dnn-license = %{version}-%{release}

%description lib
lib components for the mkl-dnn package.


%package license
Summary: license components for the mkl-dnn package.
Group: Default

%description license
license components for the mkl-dnn package.


%prep
%setup -q -n mkl-dnn-0.16
%patch1 -p1
pushd ..
cp -a mkl-dnn-0.16 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538156718
mkdir -p clr-build
pushd clr-build
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
%cmake ..
make VERBOSE=1  %{?_smp_mflags}  || :
popd

%install
export SOURCE_DATE_EPOCH=1538156718
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/mkl-dnn
cp LICENSE %{buildroot}/usr/share/doc/mkl-dnn/LICENSE
cp tests/gtests/gtest/LICENSE %{buildroot}/usr/share/doc/mkl-dnn/tests_gtests_gtest_LICENSE
pushd clr-build-avx2
%make_install_avx2  || :
popd
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/*.hpp
/usr/lib64/haswell/libmkldnn.so
/usr/lib64/libmkldnn.so

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libmkldnn.so.0
/usr/lib64/haswell/libmkldnn.so.0.16.0
/usr/lib64/libmkldnn.so.0
/usr/lib64/libmkldnn.so.0.16.0

%files license
%defattr(0644,root,root,0755)
/usr/share/doc/mkl-dnn/LICENSE
/usr/share/doc/mkl-dnn/tests_gtests_gtest_LICENSE
/usr/share/doc/mkldnn/LICENSE
