#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mkl-dnn
Version  : 1.6.2
Release  : 29
URL      : https://github.com/intel/mkl-dnn/archive/v1.6.2/mkl-dnn-1.6.2.tar.gz
Source0  : https://github.com/intel/mkl-dnn/archive/v1.6.2/mkl-dnn-1.6.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause
Requires: mkl-dnn-lib = %{version}-%{release}
Requires: mkl-dnn-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : eigen-data
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : graphviz
BuildRequires : intel-compute-runtime
BuildRequires : intel-graphics-compiler-dev
BuildRequires : ocl-icd
BuildRequires : openblas
BuildRequires : opencl-clang-dev
BuildRequires : opencl-headers-dev
BuildRequires : pkg-config
BuildRequires : tbb-dev
Patch1: gnu.patch

%description
oneAPI Deep Neural Network Library (oneDNN)
===========================================

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
%setup -q -n oneDNN-1.6.2
cd %{_builddir}/oneDNN-1.6.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1599602125
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=haswell "
export CFLAGS="$CFLAGS -march=haswell -m64"
export CXXFLAGS="$CXXFLAGS -march=haswell -m64"
export FFLAGS="$FFLAGS -march=haswell -m64"
export FCFLAGS="$FCFLAGS -march=haswell -m64"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-lto -fno-math-errno -fno-semantic-interposition -fno-trapping-math -march=skylake-avx512 "
export CFLAGS="$CFLAGS -march=skylake-avx512 -m64 "
export CXXFLAGS="$CXXFLAGS -march=skylake-avx512 -m64 "
export FFLAGS="$FFLAGS -march=skylake-avx512 -m64 "
export FCFLAGS="$FCFLAGS -march=skylake-avx512 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1599602125
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mkl-dnn
cp %{_builddir}/oneDNN-1.6.2/LICENSE %{buildroot}/usr/share/package-licenses/mkl-dnn/aba6ee9c5143e77e6555d96c43e8a204319b10bc
cp %{_builddir}/oneDNN-1.6.2/src/cpu/x64/jit_utils/jitprofiling/LICENSE.BSD %{buildroot}/usr/share/package-licenses/mkl-dnn/be8f76850d5fd6458ff339a1a7df86bbec3e5366
cp %{_builddir}/oneDNN-1.6.2/src/cpu/x64/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/mkl-dnn/59ecdb87df571ebd03bc505a75344cc6f49626e8
cp %{_builddir}/oneDNN-1.6.2/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/mkl-dnn/5a2314153eadadc69258a9429104cd11804ea304
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
/usr/usr/lib64/libmkldnn.so
/usr/usr/lib64/libmkldnn.so.1
/usr/usr/lib64/libmkldnn.so.1.6

%files dev
%defattr(-,root,root,-)
/usr/include/dnnl.h
/usr/include/dnnl.hpp
/usr/include/dnnl_config.h
/usr/include/dnnl_debug.h
/usr/include/dnnl_threadpool_iface.hpp
/usr/include/dnnl_types.h
/usr/include/dnnl_version.h
/usr/include/mkldnn.h
/usr/include/mkldnn.hpp
/usr/include/mkldnn_config.h
/usr/include/mkldnn_debug.h
/usr/include/mkldnn_dnnl_mangling.h
/usr/include/mkldnn_types.h
/usr/include/mkldnn_version.h
/usr/lib64/cmake/dnnl/dnnl-config-version.cmake
/usr/lib64/cmake/dnnl/dnnl-config.cmake
/usr/lib64/cmake/dnnl/dnnl-targets-relwithdebinfo.cmake
/usr/lib64/cmake/dnnl/dnnl-targets.cmake
/usr/lib64/haswell/avx512_1/libdnnl.so
/usr/lib64/haswell/libdnnl.so
/usr/lib64/libdnnl.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/dnnl/LICENSE
/usr/share/doc/dnnl/README
/usr/share/doc/dnnl/THIRD-PARTY-PROGRAMS
/usr/share/doc/dnnl/reference/html/assets/mathjax/config/dnnl.js

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/avx512_1/libdnnl.so.1
/usr/lib64/haswell/avx512_1/libdnnl.so.1.6
/usr/lib64/haswell/libdnnl.so.1
/usr/lib64/haswell/libdnnl.so.1.6
/usr/lib64/libdnnl.so.1
/usr/lib64/libdnnl.so.1.6

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mkl-dnn/59ecdb87df571ebd03bc505a75344cc6f49626e8
/usr/share/package-licenses/mkl-dnn/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/mkl-dnn/aba6ee9c5143e77e6555d96c43e8a204319b10bc
/usr/share/package-licenses/mkl-dnn/be8f76850d5fd6458ff339a1a7df86bbec3e5366
