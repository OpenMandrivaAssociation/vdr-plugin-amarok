
%define plugin	amarok
%define name	vdr-plugin-%plugin
%define version	0.0.2
%define rel	10

Summary:	VDR plugin: A frontend for KDE's amarok
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://irimi.ir.ohost.de/
Source:		http://irimi.ir.ohost.de/vdr-%plugin-%version.tar.bz2
Patch0:		amarok-0.0.2-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
A frontend vdr plugin for KDE's amaroK.

You also need vdramgw running on the same host as amaroK. It is
packaged in a separate package

%package -n vdramgw
Summary:	VDR amaroK gateway
Group:		Video
%description -n vdramgw
Gateway for the VDR amarok plugin.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep
chmod 0644 README HISTORY vdramgw/README vdramgw/HISTORY
chmod 0644 vdramgw/vdramgw.conf contrib/jpeg2vdrmpg.sh

%build
%vdr_plugin_build

cd vdramgw
%make CFLAGS="%optflags" CXXFLAGS="%optflags"

%install
rm -rf %{buildroot}
%vdr_plugin_install

install -d -m755 %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}
install -m644 contrib/*.mpg %{buildroot}%{_vdr_plugin_cfgdir}/%{plugin}

install -d -m755 %{buildroot}%{_bindir}
install -m755 vdramgw/vdramgw %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY contrib/jpeg2vdrmpg.sh
%dir %{_vdr_plugin_cfgdir}/%{plugin}
%config(noreplace) %{_vdr_plugin_cfgdir}/%{plugin}/amarokmain.mpg

%files -n vdramgw
%defattr(-,root,root)
%doc vdramgw/README vdramgw/HISTORY vdramgw/vdramgw.conf
%{_bindir}/vdramgw


