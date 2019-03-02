#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mkl-dnn
Version  : 0.18
Release  : 13
URL      : https://github.com/intel/mkl-dnn/archive/v0.18.tar.gz
Source0  : https://github.com/intel/mkl-dnn/archive/v0.18.tar.gz
Summary  : Intel® Math Kernel Library for Deep Neural Networks
Group    : Development/Tools
License  : BSD-3-Clause
Requires: mkl-dnn-lib = %{version}-%{release}
Requires: mkl-dnn-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : git
BuildRequires : glibc-dev
Patch1: no-native.patch

%description
# benchdnn
**benchdnn** is a standalone correctness and performance benchmark for
[Intel(R) Math Kernel Library for Deep Neural Networks (Intel(R) MKL-DNN)](/intel/mkl-dnn).
The purpose of the benchmark is extended and robust correctness verification of
the primitives provided by Intel MKL-DNN. Currently, **benchdnn** supports convolutions
, inner products, reorder, batch normalization, deconvolution, recurrent neural network, and shuffle of different data types.

%package dev
Summary: dev components for the mkl-dnn package.
Group: Development
Requires: mkl-dnn-lib = %{version}-%{release}
Provides: mkl-dnn-devel = %{version}-%{release}
Requires: mkl-dnn = %{version}-%{release}

%description dev
dev components for the mkl-dnn package.


%package doc
Summary: doc components for the mkl-dnn package.
Group: Documentation

%description doc
doc components for the mkl-dnn package.


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
%setup -q -n mkl-dnn-0.18
%patch1 -p1
pushd ..
cp -a mkl-dnn-0.18 buildavx2
popd
pushd ..
cp -a mkl-dnn-0.18 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551538363
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
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1551538363
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mkl-dnn
cp src/cpu/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/mkl-dnn/src_cpu_xbyak_COPYRIGHT
cp tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/mkl-dnn/tests_gtests_gtest_LICENSE
pushd clr-build-avx512
%make_install_avx512  || :
popd
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
/usr/lib64/cmake/mkldnn/mkldnn-config-version.cmake
/usr/lib64/cmake/mkldnn/mkldnn-config.cmake
/usr/lib64/cmake/mkldnn/mkldnn-targets-relwithdebinfo.cmake
/usr/lib64/cmake/mkldnn/mkldnn-targets.cmake
/usr/lib64/haswell/avx512_1/libmkldnn.so
/usr/lib64/haswell/libmkldnn.so
/usr/lib64/libmkldnn.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/mkldnn/LICENSE

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libmkldnn.so.0
/usr/lib64/haswell/avx512_1/libmkldnn.so.0.18.0.0
/usr/lib64/haswell/libmkldnn.so.0
/usr/lib64/haswell/libmkldnn.so.0.18.0.0
/usr/lib64/libmkldnn.so.0
/usr/lib64/libmkldnn.so.0.18.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mkl-dnn/src_cpu_xbyak_COPYRIGHT
/usr/share/package-licenses/mkl-dnn/tests_gtests_gtest_LICENSE
