#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v21
# autospec commit: e36a856
#
Name     : mkl-dnn
Version  : 3.7
Release  : 103
URL      : https://github.com/oneapi-src/oneDNN/archive/v3.7/oneDNN-3.7.tar.gz
Source0  : https://github.com/oneapi-src/oneDNN/archive/v3.7/oneDNN-3.7.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: mkl-dnn-lib = %{version}-%{release}
Requires: mkl-dnn-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : cmake
BuildRequires : doxygen
BuildRequires : eigen-data
BuildRequires : git
BuildRequires : glibc-dev
BuildRequires : graphviz
BuildRequires : llvm-dev
BuildRequires : openblas
BuildRequires : openblas-dev
BuildRequires : pkg-config
BuildRequires : pypi-sphinx
BuildRequires : python3
BuildRequires : tbb-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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
%setup -q -n oneDNN-3.7
cd %{_builddir}/oneDNN-3.7
pushd ..
cp -a oneDNN-3.7 buildavx2
popd
pushd ..
cp -a oneDNN-3.7 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739983910
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
pushd ../buildavx2/
mkdir -p clr-build-avx2
pushd clr-build-avx2
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd
pushd ../buildavx512/
mkdir -p clr-build-avx512
pushd clr-build-avx512
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
GOAMD64=v4
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v4 -mprefer-vector-width=512 "
%cmake ..   -G 'Unix Makefiles'
make  %{?_smp_mflags}
popd
popd

%install
export GCC_IGNORE_WERROR=1
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1739983910
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mkl-dnn
cp %{_builddir}/oneDNN-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/mkl-dnn/9380b922e0913dbe94d8be4c34154d91734304dc || :
cp %{_builddir}/oneDNN-%{version}/src/common/ittnotify/LICENSE.BSD %{buildroot}/usr/share/package-licenses/mkl-dnn/be8f76850d5fd6458ff339a1a7df86bbec3e5366 || :
cp %{_builddir}/oneDNN-%{version}/src/cpu/x64/xbyak/COPYRIGHT %{buildroot}/usr/share/package-licenses/mkl-dnn/59ecdb87df571ebd03bc505a75344cc6f49626e8 || :
cp %{_builddir}/oneDNN-%{version}/src/gpu/intel/jit/ngen/COPYRIGHT %{buildroot}/usr/share/package-licenses/mkl-dnn/f9e3463caf9d198d7748315d5fcada9e89d43585 || :
cp %{_builddir}/oneDNN-%{version}/tests/gtests/gtest/LICENSE %{buildroot}/usr/share/package-licenses/mkl-dnn/5a2314153eadadc69258a9429104cd11804ea304 || :
export GOAMD64=v2
pushd ../buildavx2/
GOAMD64=v3
pushd clr-build-avx2
%make_install_v3  || :
popd
popd
pushd ../buildavx512/
GOAMD64=v4
pushd clr-build-avx512
%make_install_v4  || :
popd
popd
GOAMD64=v2
pushd clr-build
%make_install
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/include/oneapi/dnnl/dnnl_common.h
/usr/include/oneapi/dnnl/dnnl_common.hpp
/usr/include/oneapi/dnnl/dnnl_common_types.h
/usr/include/oneapi/dnnl/dnnl_config.h
/usr/include/oneapi/dnnl/dnnl_debug.h
/usr/include/oneapi/dnnl/dnnl_graph.h
/usr/include/oneapi/dnnl/dnnl_graph.hpp
/usr/include/oneapi/dnnl/dnnl_graph_ocl.h
/usr/include/oneapi/dnnl/dnnl_graph_ocl.hpp
/usr/include/oneapi/dnnl/dnnl_graph_sycl.h
/usr/include/oneapi/dnnl/dnnl_graph_sycl.hpp
/usr/include/oneapi/dnnl/dnnl_graph_types.h
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
/usr/include/oneapi/dnnl/dnnl_ukernel.h
/usr/include/oneapi/dnnl/dnnl_ukernel.hpp
/usr/include/oneapi/dnnl/dnnl_ukernel_types.h
/usr/include/oneapi/dnnl/dnnl_version.h
/usr/include/oneapi/dnnl/dnnl_version_hash.h
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
/usr/share/doc/dnnl/reference/rst/bf16_programming.jpg
/usr/share/doc/dnnl/reference/rst/compressed_sdpa_pattern.png
/usr/share/doc/dnnl/reference/rst/conf.py
/usr/share/doc/dnnl/reference/rst/fp-gated-mlp.png
/usr/share/doc/dnnl/reference/rst/gated-mlp-swish.png
/usr/share/doc/dnnl/reference/rst/gqa.png
/usr/share/doc/dnnl/reference/rst/img_bf16_diagram.png
/usr/share/doc/dnnl/reference/rst/img_depthwise_fusion.jpg
/usr/share/doc/dnnl/reference/rst/img_diagram.png
/usr/share/doc/dnnl/reference/rst/img_dnnl_object_snapshot.jpg
/usr/share/doc/dnnl/reference/rst/img_dnnl_programming_flow.jpg
/usr/share/doc/dnnl/reference/rst/img_graph_programming_model.png
/usr/share/doc/dnnl/reference/rst/img_inference_scope.jpg
/usr/share/doc/dnnl/reference/rst/img_multiscalar.png
/usr/share/doc/dnnl/reference/rst/img_overview_flow.jpg
/usr/share/doc/dnnl/reference/rst/img_programming_model.png
/usr/share/doc/dnnl/reference/rst/img_singlescalar.png
/usr/share/doc/dnnl/reference/rst/img_training_inference_scope.jpg
/usr/share/doc/dnnl/reference/rst/int8_programming.jpg
/usr/share/doc/dnnl/reference/rst/mem_fmt_blk.png
/usr/share/doc/dnnl/reference/rst/mem_fmt_img1.png
/usr/share/doc/dnnl/reference/rst/mem_fmt_img2.png
/usr/share/doc/dnnl/reference/rst/mem_fmt_padded_blk.png
/usr/share/doc/dnnl/reference/rst/sdpa-mask-1.png
/usr/share/doc/dnnl/reference/rst/sdpa-mask-2.png
/usr/share/doc/dnnl/reference/rst/sdpa-mask-3.png
/usr/share/doc/dnnl/reference/rst/sdpa-reorder.png
/usr/share/doc/dnnl/reference/rst/sdpa.png
/usr/share/doc/dnnl/reference/rst/strides.png
/usr/share/doc/dnnl/reference/rst/unrolled_stack_rnn.jpg

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libdnnl.so.3.7
/V4/usr/lib64/libdnnl.so.3.7
/usr/lib64/libdnnl.so.3
/usr/lib64/libdnnl.so.3.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mkl-dnn/59ecdb87df571ebd03bc505a75344cc6f49626e8
/usr/share/package-licenses/mkl-dnn/5a2314153eadadc69258a9429104cd11804ea304
/usr/share/package-licenses/mkl-dnn/9380b922e0913dbe94d8be4c34154d91734304dc
/usr/share/package-licenses/mkl-dnn/be8f76850d5fd6458ff339a1a7df86bbec3e5366
/usr/share/package-licenses/mkl-dnn/f9e3463caf9d198d7748315d5fcada9e89d43585
