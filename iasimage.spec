#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xC9D50845DE5519CB (arzhan@kinzhalin.com)
#
Name     : iasimage
Version  : v0.0.2
Release  : 3
URL      : https://github.com/intel/iasimage/releases/download/v0.0.2/iasimage-v0.0.2.tar.gz
Source0  : https://github.com/intel/iasimage/releases/download/v0.0.2/iasimage-v0.0.2.tar.gz
Source99 : https://github.com/intel/iasimage/releases/download/v0.0.2/iasimage-v0.0.2.tar.gz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause
Requires: iasimage-bin
Requires: cryptography

%description
iasimage
-----------
iasimage is a utility program for creating Intel Automotive Service (IAS) images, a binary file format understood by IntelÂ© Slim Bootloader to load and initialize Operating Systems or Hypervisor.

%package bin
Summary: bin components for the iasimage package.
Group: Binaries

%description bin
bin components for the iasimage package.


%prep
%setup -q -n iasimage-0.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527862878
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1527862878
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/iasimage
