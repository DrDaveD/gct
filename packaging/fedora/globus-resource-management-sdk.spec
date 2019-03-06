Name:		globus-resource-management-sdk
%global _name %(echo %{name} | tr - _)
Version:	6.0
Release:	3%{?dist}
Summary:	Grid Community Toolkit - Resource Management SDK

Group:		System Environment/Libraries
License:	%{?suse_version:Apache-2.0}%{!?suse_version:ASL 2.0}
URL:		https://github.com/gridcf/gct/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	globus-common
Requires:	globus-common-devel
Requires:	globus-common-doc
Requires:	globus-callout
Requires:	globus-callout-devel
Requires:	globus-callout-doc
Requires:	globus-gass-cache
Requires:	globus-gass-cache-devel
Requires:	globus-gsi-openssl-error
Requires:	globus-gsi-openssl-error-devel
Requires:	globus-gsi-openssl-error-doc
Requires:	globus-gsi-proxy-ssl
Requires:	globus-gsi-proxy-ssl-devel
Requires:	globus-gsi-proxy-ssl-doc
Requires:	globus-rsl
Requires:	globus-rsl-devel
Requires:	globus-rsl-doc
Requires:	globus-openssl-module
Requires:	globus-openssl-module-devel
Requires:	globus-openssl-module-doc
Requires:	globus-gsi-cert-utils
Requires:	globus-gsi-cert-utils-devel
Requires:	globus-gsi-cert-utils-doc
Requires:	globus-simple-ca
Requires:	globus-gsi-sysconfig
Requires:	globus-gsi-sysconfig-devel
Requires:	globus-gsi-sysconfig-doc
Requires:	globus-gsi-callback
Requires:	globus-gsi-callback-devel
Requires:	globus-gsi-callback-doc
Requires:	globus-gsi-credential
Requires:	globus-gsi-credential-devel
Requires:	globus-gsi-credential-doc
Requires:	globus-gsi-proxy-core
Requires:	globus-gsi-proxy-core-devel
Requires:	globus-gsi-proxy-core-doc
Requires:	globus-gssapi-gsi
Requires:	globus-gssapi-gsi-devel
Requires:	globus-gssapi-gsi-doc
Requires:	globus-gss-assist
Requires:	globus-gss-assist-devel
Requires:	globus-gss-assist-doc
Requires:	globus-xio
Requires:	globus-xio-devel
Requires:	globus-xio-doc
Requires:	globus-xio-gsi-driver
Requires:	globus-xio-gsi-driver-devel
Requires:	globus-xio-gsi-driver-doc
Requires:	globus-io
Requires:	globus-io-devel
Requires:	globus-gssapi-error
Requires:	globus-gssapi-error-devel
Requires:	globus-gssapi-error-doc
Requires:	globus-ftp-control
Requires:	globus-ftp-control-devel
Requires:	globus-ftp-control-doc
Requires:	globus-gass-transfer
Requires:	globus-gass-transfer-devel
Requires:	globus-gass-transfer-doc
Requires:	globus-gram-protocol
Requires:	globus-gram-protocol-devel
Requires:	globus-gram-protocol-doc
Requires:	globus-xio-popen-driver
Requires:	globus-xio-popen-driver-devel
Requires:	globus-ftp-client
Requires:	globus-ftp-client-devel
Requires:	globus-ftp-client-doc
Requires:	globus-gass-server-ez
Requires:	globus-gass-server-ez-devel
Requires:	globus-gram-client
Requires:	globus-gram-client-devel
Requires:	globus-gram-client-doc

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
Resource Management SDK
%prep

%build

%install

%files

%post

%postun

%changelog
* Mon Apr 02 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 6.0-3
- First Grid Community Toolkit release

* Wed Aug 26 2015 Joseph Bester <bester@mcs.anl.gov> - 6.0-2
- Remove obsolete globus-core dependency

* Tue Jul 17 2012 Joseph Bester <bester@mcs.anl.gov> - 6.0-1
- GT 5.2.2 New Metapackage
