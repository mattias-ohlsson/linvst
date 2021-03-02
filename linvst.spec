Name:           linvst
Version:        3.2.1
Release:        1%{?dist}
Summary:        Windows VST wrapper for Linux

License:        GPLv3+
URL:            https://github.com/osxmidi/LinVst
Source0:        https://github.com/osxmidi/LinVst/archive/%{version}.tar.gz

BuildRequires:  wine-devel libX11-devel
Requires:       wine

%description
LinVst adds support for Windows VST to be used in Linux VST capable DAW.

%package testvst
Summary:        Test utility for LinVst

%description testvst
TestVst can roughly test how a VST plugin might run under Wine.

%prep
%autosetup -n LinVst-%{version}

%build
%make_build CXX_FLAGS=-g WINECXX_FLAGS=-g

cd TestVst
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

install -D -p vst/linvst.so %{buildroot}%{_datadir}/%{name}/linvst.so

install -d -m 755 %{buildroot}%{_datadir}/%{name}/testvst
install -m 755 TestVst/{*.exe,*.so} %{buildroot}%{_datadir}/%{name}/testvst/

%files
%license COPYING
%doc README.md
%{_bindir}/lin-vst-servertrack.exe
%{_bindir}/lin-vst-servertrack.exe.so
%{_datadir}/%{name}/linvst.so

%files testvst
%license COPYING
%doc TestVst/README.md
%{_datadir}/%{name}/testvst/testvst.exe
%{_datadir}/%{name}/testvst/testvst.exe.so

%changelog
* Tue Mar 02 2021 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.2.1-1
- Update to 3.2.1

* Thu Oct 29 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 3.15-1
- Update to 3.15

* Wed Mar  4 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.8-1
- Initial build
