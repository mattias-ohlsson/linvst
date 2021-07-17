Name:           linvst
Version:        4.5
Release:        1%{?dist}
Summary:        Windows VST wrapper for Linux

License:        GPLv3+
URL:            https://github.com/osxmidi/LinVst
Source0:        https://github.com/osxmidi/LinVst/archive/%{version}.tar.gz

Patch0:         linvst-4.5-add-winecxx-flags.patch

BuildRequires:  gcc-c++ glibc-devel glibc-devel(x86-32)
BuildRequires:  wine-devel libX11-devel libX11-devel(x86-32)
BuildRequires:  libstdc++(x86-32) libX11(x86-32)

Requires:       wine

%description
LinVst adds support for Windows VST to be used in Linux VST capable DAW.

%package testvst
Summary:        Test utility for LinVst

%description testvst
TestVst can roughly test how a VST plugin might run under Wine.

%prep
%autosetup -p1 -n LinVst-%{version}

%build
%make_build CXX_FLAGS=-g WINECXX_FLAGS=-g

cd TestVst
%make_build

%install
%make_install

install -D -p vst/linvst.so %{buildroot}%{_datadir}/%{name}/linvst.so

install -d -m 755 %{buildroot}%{_datadir}/%{name}/testvst
install -m 755 TestVst/{*.exe,*.so} %{buildroot}%{_datadir}/%{name}/testvst/

%files
%license COPYING
%doc README.md
%{_bindir}/lin-vst-servertrack.exe
%{_bindir}/lin-vst-servertrack.exe.so
%{_bindir}/lin-vst-servertrack32.exe
%{_bindir}/lin-vst-servertrack32.exe.so
%{_datadir}/%{name}/linvst.so

%files testvst
%license COPYING
%doc TestVst/README.md
%{_datadir}/%{name}/testvst/testvst.exe
%{_datadir}/%{name}/testvst/testvst.exe.so

%changelog
* Sat Jul 17 2021 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 4.5-1
- Update to 4.5

* Tue Mar 02 2021 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.2.1-1
- Update to 3.2.1

* Thu Oct 29 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.15-1
- Update to 3.15

* Wed Mar  4 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.8-1
- Initial build
