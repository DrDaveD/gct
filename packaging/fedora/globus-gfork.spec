%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		globus-gfork
%global soname 0
%global _name %(echo %{name} | tr - _)
Version:	5.0
Release:	1%{?dist}
Summary:	Grid Community Toolkit - GFork

Group:		System Environment/Libraries
License:	%{?suse_version:Apache-2.0}%{!?suse_version:ASL 2.0}
URL:		https://github.com/gridcf/gct/
Source:		%{_name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:	gcc
BuildRequires:	globus-common-devel >= 14
BuildRequires:	globus-xio-devel >= 3

%if %{?suse_version}%{!?suse_version:0}
%global mainpkg lib%{_name}%{soname}
%global nmainpkg -n %{mainpkg}
%else
%global mainpkg %{name}
%endif

%if %{?nmainpkg:1}%{!?nmainpkg:0}
%package %{?nmainpkg}
Summary:	Grid Community Toolkit - GFork
Group:		System Environment/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{name} < %{version}-%{release}
%endif

%package progs
Summary:	Grid Community Toolkit - GFork Programs
Group:		Applications/Internet
Requires:	%{mainpkg}%{?_isa} = %{version}-%{release}

%package devel
Summary:	Grid Community Toolkit - GFork Development Files
Group:		Development/Libraries
Requires:	%{mainpkg}%{?_isa} = %{version}-%{release}

%if %{?nmainpkg:1}%{!?nmainpkg:0}
%description %{?nmainpkg}
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{mainpkg} package contains:
GFork Library
%endif

%description
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name} package contains:
GFork Library

%description progs
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-progs package contains:
GFork Programs - GFork is user configurable super-server daemon very similar
to xinetd. It listens on a TCP port. When clients connect to a port it runs an
administrator defined program which services that client connection, just as
x/inetd do.

%description devel
The Grid Community Toolkit (GCT) is an open source software toolkit used for
building grid systems and applications. It is a fork of the Globus Toolkit
originally created by the Globus Alliance. It is supported by the Grid
Community Forum (GridCF) that provides community-based support for core
software packages in grid computing.

The %{name}-devel package contains:
GFork Development Files

%prep
%setup -q -n %{_name}-%{version}

%build
%configure --disable-static \
	   --includedir=%{_includedir}/globus \
	   --libexecdir=%{_datadir}/share/globus \
	   --docdir=%{_pkgdocdir}

make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

# Remove libtool archives (.la files)
rm $RPM_BUILD_ROOT%{_libdir}/*.la

# Add empty default configuration file
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}
echo "# This is the default gfork configuration file" > \
  $RPM_BUILD_ROOT%{_sysconfdir}/gfork.conf

%post %{?nmainpkg} -p /sbin/ldconfig

%postun %{?nmainpkg} -p /sbin/ldconfig

%files %{?nmainpkg}
%defattr(-,root,root,-)
%{_libdir}/libglobus_gfork.so.*
%dir %{_pkgdocdir}
%doc %{_pkgdocdir}/GLOBUS_LICENSE

%files progs
%defattr(-,root,root,-)
%{_sbindir}/gfork
%config(noreplace) %{_sysconfdir}/gfork.conf
%doc %{_pkgdocdir}/README.txt

%files devel
%defattr(-,root,root,-)
%{_includedir}/globus/*
%{_libdir}/libglobus_gfork.so
%{_libdir}/pkgconfig/%{name}.pc

%changelog
* Sat Mar 31 2018 Mattias Ellert <mattias.ellert@physics.uu.se> - 5.0-1
- First Grid Community Toolkit release

* Thu Sep 08 2016 Globus Toolkit <support@globus.org> - 4.9-4
- Rebuild after changes for el.5 with openssl101e

* Thu Aug 25 2016 Globus Toolkit <support@globus.org> - 4.9-3
- SLES 12 packaging conditionals

* Sat Aug 20 2016 Globus Toolkit <support@globus.org> - 4.9-1
- Update bug report URL

* Thu Aug 06 2015 Globus Toolkit <support@globus.org> - 4.8-2
- Add vendor

* Wed Jul 01 2015 Globus Toolkit <support@globus.org> - 4.8-1
- remove dead code

* Thu Sep 25 2014 Globus Toolkit <support@globus.org> - 4.7-1
- Fix typo in help message
- Quiet some autoconf/automake warnings

* Fri Aug 22 2014 Globus Toolkit <support@globus.org> - 4.6-1
- Merge fixes from ellert-globus_6_branch

* Wed Aug 20 2014 Globus Toolkit <support@globus.org> - 4.5-2
- Fix Source path

* Mon Jun 09 2014 Globus Toolkit <support@globus.org> - 4.5-1
- Merge changes from Mattias Ellert

* Fri Apr 18 2014 Globus Toolkit <support@globus.org> - 4.4-1
- Version bump for consistency

* Thu Feb 27 2014 Globus Toolkit <support@globus.org> - 4.3-1
- Packaging fixes, Warning Cleanup

* Tue Feb 25 2014 Globus Toolkit <support@globus.org> - 4.2-1
- Packaging fixes

* Mon Feb 10 2014 Globus Toolkit <support@globus.org> - 4.1-1
- Put automake version requirement first

* Tue Jan 21 2014 Globus Toolkit <support@globus.org> - 4.0-1
- Repackage for GT6 without GPT

* Wed Jun 26 2013 Globus Toolkit <support@globus.org> - 3.2-7
- GT-424: New Fedora Packaging Guideline - no %%_isa in BuildRequires

* Tue Mar 05 2013 Globus Toolkit <support@globus.org> - 3.2-6
- Add missing build dependency

* Mon Nov 26 2012 Globus Toolkit <support@globus.org> - 3.2-5
- 5.2.3

* Mon Jul 16 2012 Joseph Bester <bester@mcs.anl.gov> - 3.2-4
- GT 5.2.2 final

* Fri Jun 29 2012 Joseph Bester <bester@mcs.anl.gov> - 3.2-3
- GT 5.2.2 Release

* Wed May 09 2012 Joseph Bester <bester@mcs.anl.gov> - 3.2-2
- RHEL 4 patches

* Tue Feb 14 2012 Joseph Bester <bester@mcs.anl.gov> - 3.2-1
- RIC-229: Clean up GPT metadata

* Mon Dec 05 2011 Joseph Bester <bester@mcs.anl.gov> - 3.1-4
- Update for 5.2.0 release

* Mon Dec 05 2011 Joseph Bester <bester@mcs.anl.gov> - 3.1-3
- Last sync prior to 5.2.0

* Tue Oct 11 2011 Joseph Bester <bester@mcs.anl.gov> - 3.1-2
- Add explicit dependencies on >= 5.2 libraries

* Thu Oct 06 2011 Joseph Bester <bester@mcs.anl.gov> - 3.1-1
- Add backward-compatibility aging

* Thu Sep 01 2011 Joseph Bester <bester@mcs.anl.gov> - 3.0-2
- Update for 5.1.2 release

* Sat Jan 23 2010 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2-4
- Update to Globus Toolkit 5.0.0

* Fri Oct 16 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2-3
- Fix location of default config file
- Add empty default config file

* Wed Oct 07 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2-2
- Include additional documentation

* Tue Jul 28 2009 Mattias Ellert <mattias.ellert@fysast.uu.se> - 0.2-1
- Autogenerated
