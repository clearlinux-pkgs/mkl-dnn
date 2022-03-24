#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mkl-dnn
Version  : 2.5.4
Release  : 59
URL      : https://github.com/intel/mkl-dnn/archive/v2.5.4/mkl-dnn-2.5.4.tar.gz
Source0  : https://github.com/intel/mkl-dnn/archive/v2.5.4/mkl-dnn-2.5.4.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: mkl-dnn-filemap = %{version}-%{release}
Requires: mkl-dnn-lib = %{version}-%{release}
Requires: mkl-dnn-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : eigen-data
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : graphviz
BuildRequires : openblas
BuildRequires : openblas-dev
BuildRequires : pkg-config
BuildRequires : pypi-sphinx
BuildRequires : python3
BuildRequires : tbb-dev

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


%package filemap
Summary: filemap components for the mkl-dnn package.
Group: Default

%description filemap
filemap components for the mkl-dnn package.


%package lib
Summary: lib components for the mkl-dnn package.
Group: Libraries
Requires: mkl-dnn-license = %{version}-%{release}
Requires: mkl-dnn-filemap = %{version}-%{release}

%description lib
lib components for the mkl-dnn package.


%package license
Summary: license components for the mkl-dnn package.
Group: Default

%description license
license components for the mkl-dnn package.


%prep
%setup -q -n oneDNN-2.5.4
cd %{_builddir}/oneDNN-2.5.4

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1648147245
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -Ofast -falign-functions=32 -fno-lto -fno-semantic-interposition -mno-vzeroupper -mprefer-vector-width=256 "
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fno-lto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fno-lto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fno-lto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v3 -falign-functions=32 -fno-lto -fno-semantic-interposition -march=x86-64-v3 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -march=x86-64-v3 -m64 -Wl,-z,x86-64-v3"
%cmake ..
make  %{?_smp_mflags}
popd
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -fno-lto -fno-semantic-interposition -march=x86_64-v4 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FCFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -fno-lto -fno-semantic-interposition -march=x86_64-v4 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export FFLAGS="$FFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -fno-lto -fno-semantic-interposition -march=x86_64-v4 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -Wl,-z,x86-64-v4 -falign-functions=32 -fno-lto -fno-semantic-interposition -march=x86_64-v4 -mno-vzeroupper -mprefer-vector-width=256 -mtune=skylake "
export CFLAGS="$CFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -march=x86-64-v4 -m64 -Wl,-z,x86-64-v4 "
export FCFLAGS="$FCFLAGS -march=x86-64-v4 -m64 "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1648147245
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mkl-dnn
cp %{_builddir}/oneDNN-2.5.4/LICENSE %{buildroot}/usr/share/package-licenses/mkl-dnn/57997263de7280824c54d5aa8ac45fdb9d74e897
cp %{_builddir}/oneDNN-2.5.4/src/common/ittnotify/LICENSE.BSD %{buildroot}/usr/share/package-licenses/mkl-dnn/be8f76850d5fd6458ff339a1a7df86bbec3e5366
cp %{_builddir}/oneDNN-2.5.4/src/cpu/x64/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/mkl-dnn/59ecdb87df571ebd03bc505a75344cc6f49626e8
cp %{_builddir}/oneDNN-2.5.4/src/gpu/jit/ngen/COPYRIGHT %{buildroot}/usr/share/package-licenses/mkl-dnn/f9e3463caf9d198d7748315d5fcada9e89d43585
cp %{_builddir}/oneDNN-2.5.4/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/mkl-dnn/5a2314153eadadc69258a9429104cd11804ea304
pushd clr-build-avx2
%make_install_v3  || :
popd
pushd clr-build-avx512
%make_install_v4  || :
popd
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/dnnl.h
/usr/include/dnnl.hpp
/usr/include/dnnl_config.h
/usr/include/dnnl_debug.h
/usr/include/dnnl_ocl.h
/usr/include/dnnl_ocl.hpp
/usr/include/dnnl_sycl.h
/usr/include/dnnl_sycl.hpp
/usr/include/dnnl_sycl_types.h
/usr/include/dnnl_threadpool.h
/usr/include/dnnl_threadpool.hpp
/usr/include/dnnl_threadpool_iface.hpp
/usr/include/dnnl_types.h
/usr/include/dnnl_version.h
/usr/include/oneapi/dnnl/dnnl.h
/usr/include/oneapi/dnnl/dnnl.hpp
/usr/include/oneapi/dnnl/dnnl_config.h
/usr/include/oneapi/dnnl/dnnl_debug.h
/usr/include/oneapi/dnnl/dnnl_ocl.h
/usr/include/oneapi/dnnl/dnnl_ocl.hpp
/usr/include/oneapi/dnnl/dnnl_ocl_types.h
/usr/include/oneapi/dnnl/dnnl_sycl.h
/usr/include/oneapi/dnnl/dnnl_sycl.hpp
/usr/include/oneapi/dnnl/dnnl_sycl_types.h
/usr/include/oneapi/dnnl/dnnl_threadpool.h
/usr/include/oneapi/dnnl/dnnl_threadpool.hpp
/usr/include/oneapi/dnnl/dnnl_threadpool_iface.hpp
/usr/include/oneapi/dnnl/dnnl_types.h
/usr/include/oneapi/dnnl/dnnl_version.h
/usr/lib64/cmake/dnnl/dnnl-config-version.cmake
/usr/lib64/cmake/dnnl/dnnl-config.cmake
/usr/lib64/cmake/dnnl/dnnl-targets-relwithdebinfo.cmake
/usr/lib64/cmake/dnnl/dnnl-targets.cmake
/usr/lib64/libdnnl.so

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/dnnl/LICENSE
/usr/share/doc/dnnl/README
/usr/share/doc/dnnl/THIRD-PARTY-PROGRAMS
/usr/share/doc/dnnl/reference/rst/conf.py
/usr/share/doc/dnnl/reference/rst/img_bf16_diagram.png
/usr/share/doc/dnnl/reference/rst/img_depthwise_fusion.jpg
/usr/share/doc/dnnl/reference/rst/img_diagram.png
/usr/share/doc/dnnl/reference/rst/img_dnnl_object_snapshot.jpg
/usr/share/doc/dnnl/reference/rst/img_dnnl_programming_flow.jpg
/usr/share/doc/dnnl/reference/rst/img_inference_scope.jpg
/usr/share/doc/dnnl/reference/rst/img_multiscalar.png
/usr/share/doc/dnnl/reference/rst/img_overview_flow.jpg
/usr/share/doc/dnnl/reference/rst/img_programming_model.png
/usr/share/doc/dnnl/reference/rst/img_singlescalar.png
/usr/share/doc/dnnl/reference/rst/img_training_inference_scope.jpg
/usr/share/doc/dnnl/reference/rst/mem_fmt_blk.png
/usr/share/doc/dnnl/reference/rst/mem_fmt_img1.png
/usr/share/doc/dnnl/reference/rst/mem_fmt_img2.png
/usr/share/doc/dnnl/reference/rst/mem_fmt_padded_blk.png
/usr/share/doc/dnnl/reference/rst/strides.png
/usr/share/doc/dnnl/reference/rst/unrolled_stack_rnn.jpg

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-mkl-dnn

%files lib
%defattr(-,root,root,-)
/usr/lib64/libdnnl.so.2
/usr/lib64/libdnnl.so.2.5
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mkl-dnn/57997263de7280824c54d5aa8ac45fdb9d74e897
/usr/share/package-licenses/mkl-dnn/59ecdb87df571ebd03bc505a75344cc6f49626e8
/usr/share/package-licenses/mkl-dnn/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/mkl-dnn/be8f76850d5fd6458ff339a1a7df86bbec3e5366
/usr/share/package-licenses/mkl-dnn/f9e3463caf9d198d7748315d5fcada9e89d43585
