%global debug_package %{nil}

Name:           linvst
Version:        2.8
Release:        1%{?dist}
Summary:        Windows VST wrapper for Linux

License:        GPLv3+
URL:            https://github.com/osxmidi/LinVst
Source0:        https://github.com/osxmidi/LinVst/archive/%{version}.tar.gz

BuildRequires:  wine-devel libX11-devel
Requires:       wine

%description
LinVst adds support for Windows VST to be used in Linux VST capable DAW.

%prep
%autosetup -n LinVst-%{version}

%build
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

install -D -p vst/linvst.so %{buildroot}%{_datadir}/%{name}/linvst.so

%files
%license COPYING
%doc README.md
%{_bindir}/lin-vst-servertrack.exe
%{_bindir}/lin-vst-servertrack.exe.so
%{_datadir}/%{name}/linvst.so

%changelog
* Wed Mar  4 2020 Mattias Ohlsson <mattias.ohlsson@inprose.com> - 2.8-1
- Initial build
