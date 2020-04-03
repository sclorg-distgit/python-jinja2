%{?scl:%scl_package python-jinja2}
%{!?scl:%global pkg_name %{name}}

%global python3_pkgversion %{nil}
%global srcname Jinja2

Name:           %{?scl_prefix}python-jinja2
Version:        2.10.3
Release:        5%{?dist}
Summary:        General purpose template engine
License:        BSD
URL:            http://jinja.pocoo.org/
Source0:        %{pypi_source}

# Enable building without docs to avoid a circular dependency between this
# and python-sphinx:
%bcond_with docs

BuildArch:      noarch

%{?scl:Requires: %{scl}-runtime}
%{?scl:BuildRequires: %{scl}-runtime}
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-devel
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-setuptools
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-babel >= 0.8
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-markupsafe >= 0.23
# Tests disabled due to missing dependencies
# BuildRequires:  %%{?scl_prefix}python%%{python3_pkgversion}-pytest
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-rpm-macros
%if %{with docs}
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-sphinx
BuildRequires:  make
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-Pallets-Sphinx-Themes
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-sphinxcontrib-log-cabinet
BuildRequires:  %{?scl_prefix}python%{python3_pkgversion}-sphinx-issues
%endif
Requires:       %{?scl_prefix}python%{python3_pkgversion}-babel >= 0.8
Requires:       %{?scl_prefix}python%{python3_pkgversion}-markupsafe >= 0.23
Requires:       %{?scl_prefix}python%{python3_pkgversion}-setuptools

%description
Jinja2 is a template engine written in pure Python.  It provides a
Django inspired non-XML syntax but supports inline expressions and an
optional sandboxed environment.

If you have any exposure to other text-based template languages, such
as Smarty or Django, you should feel right at home with Jinja2. It's
both designer and developer friendly by sticking to Python's
principles and adding functionality useful for templating
environments.

%prep
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%autosetup -n %{srcname}-%{version}

# cleanup
find . -name '*.pyo' -o -name '*.pyc' -delete
%{?scl:EOF}


%build
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_build
%if %{with docs}
make -C docs html PYTHONPATH=$(pwd) SPHINXBUILD=sphinx-build-3
# remove hidden file
rm -rf docs/_build/html/.buildinfo
%endif # with docs

%{?scl:EOF}


%install
%{?scl:scl enable %{scl} - << \EOF}
set -ex
%py3_install
%{?scl:EOF}


%check
%{?scl:scl enable %{scl} - << \EOF}
set -ex
# %%{__python3} -m pytest tests

%{?scl:EOF}


%files
%doc CHANGES.rst
%doc ext
%doc examples
%license LICENSE.rst
%if %{with docs}
%doc docs/_build/html
%endif
%{python3_sitelib}/jinja2
%{python3_sitelib}/Jinja2-%{version}-py?.?.egg-info


%changelog
* Thu Feb 06 2020 Lumír Balhar <lbalhar@redhat.com> - 2.10.3-5
- Import from the python38 module and modified for rh-python38 RHSCL
Resolves: rhbz#1671025

* Fri Dec 13 2019 Tomas Orsava <torsava@redhat.com> - 2.10.3-4
- Exclude unsupported i686 arch

* Wed Nov 20 2019 Lumír Balhar <lbalhar@redhat.com> - 2.10.3-3
- Adjusted for Python 3.8 module in RHEL 8

* Wed Nov 20 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2.10.3-2
- Add missing BR on make.

* Mon Nov 11 2019 Lumír Balhar <lbalhar@redhat.com> - 2.10.3-1
- New upstream version (2.10.3)

* Thu Oct 03 2019 Miro Hrončok <mhroncok@redhat.com> - 2.10.1-5
- Rebuilt for Python 3.8.0rc1 (#1748018)

* Sat Aug 17 2019 Miro Hrončok <mhroncok@redhat.com> - 2.10.1-4
- Rebuilt for Python 3.8

* Thu Aug 15 2019 Miro Hrončok <mhroncok@redhat.com> - 2.10.1-3
- Bootstrap for Python 3.8

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Wed Apr 10 2019 Thomas Moschny <thomas.moschny@gmx.de> - 2.10.1-1
- Update to 2.10.1.
- Update specfile.

* Wed Feb 27 2019 Phil Wyett <philwyett@kathenas.org> - 2.10-8
- Fix FTBS due to bad conditional
- Add version requirement for markupsafe

* Sat Feb 02 2019 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sat Jul 14 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Miro Hrončok <mhroncok@redhat.com> - 2.10-5
- Rebuilt for Python 3.7

* Thu Jun 14 2018 Miro Hrončok <mhroncok@redhat.com> - 2.10-4
- Bootstrap for Python 3.7

* Mon Apr 16 2018 Charalampos Stratakis <cstratak@redhat.com> - 2.10-3
- Don't build the Python 2 subpackage on EL > 7

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 16 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.10-1
- Update to 2.10.
- Use %%bcond.
- Move BRs to their respective subpackages.

* Fri Oct 20 2017 Troy Dawson <tdawson@redhat.com> - 2.9.6-4
- Really cleanup spec file conditionals

* Fri Sep 29 2017 Troy Dawson <tdawson@redhat.com> - 2.9.6-3
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr  5 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.9.6-1
- Update to 2.9.6.

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.9.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sun Jan 29 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.9.5-1
- Update to 2.9.5.

* Fri Jan 13 2017 Thomas Moschny <thomas.moschny@gmx.de> - 2.9.4-1
- Update to 2.9.4.

* Sat Dec 31 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.8.1-1
- Update to 2.8.1.

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.8-8
- Rebuild for Python 3.6

* Thu Sep 22 2016 Orion Poplawski <orion@cora.nwra.com> - 2.8-7
- Ship python2-jinja2 (bug #1378519)
- Modernize spec

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.8-6
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri Feb  5 2016 Thomas Moschny <thomas.moschny@gmx.de> - 2.8-5
- Do not call py.test, there are currently no tests in the tarball.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.8-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Mon Oct 12 2015 Robert Kuska <rkuska@redhat.com> - 2.8-3
- Rebuilt for Python3.5 rebuild

* Mon Jul 27 2015 Thomas Moschny <thomas.moschny@gmx.de> - 2.8-2
- Apply updates Python packaging guidelines.
- Mark LICENSE with %%license.

* Sun Jul 26 2015 Haïkel Guémar <hguemar@fedoraproject.org> - 2.8-1
- Upstream 2.8

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.7.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec 2 2014 Orion Poplawski <orion@cora.nwra.com> - 2.7.3-2
- Add Requires python(3)-setuptools (bug #1168774)

* Sat Jun  7 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.7.3-1
- Update to 2.7.3.
- Reenable docs.

* Sat May 10 2014 Orion Poplawski <orion@cora.nwra.com> - 2.7.2-2
- Bootstrap (without docs) build for Python 3.4

* Fri Jan 10 2014 Thomas Moschny <thomas.moschny@gmx.de> - 2.7.2-1
- Update to 2.7.2.
- Update python3 conditional.

* Fri Aug 16 2013 Thomas Moschny <thomas.moschny@gmx.de> - 2.7.1-1
- Update to 2.7.1.

* Thu Jul 25 2013 Orion Poplawski <orion@cora.nwra.com> - 2.7-1
- Update to 2.7
- spec cleanup

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 2.6-5
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Fri Aug  3 2012 David Malcolm <dmalcolm@redhat.com> - 2.6-4
- remove rhel logic from with_python3 conditional

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jul 25 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.6-1
- Update to 2.6.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Jan 18 2011 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.5-3
- Re-enable html doc generation.
- Remove conditional for F-12 and below.
- Do not silently fail the testsuite for with py3k.

* Mon Nov  1 2010 Michel Salim <salimma@fedoraproject.org> - 2.5.5-2
- Move python3 runtime requirements to python3 subpackage

* Wed Oct 27 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.5-1
- Update to 2.5.5.

* Wed Aug 25 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.2-4
- Revert to previous behavior: fail the build on failed test.
- Rebuild for Python 3.2.

* Wed Aug 25 2010 Dan Horák <dan[at]danny.cz> - 2.5.2-3
- %%ifnarch doesn't work on noarch package so don't fail the build on failed tests

* Wed Aug 25 2010 Dan Horák <dan[at]danny.cz> - 2.5.2-2
- disable the testsuite on s390(x)

* Thu Aug 19 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.5.2-1
- Update to upstream version 2.5.2.
- Package depends on python-markupsafe and is noarch now.

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.5-4
- add explicit build-requirement on python-setuptools
- fix doc disablement for python3 subpackage

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.5-3
- support disabling documentation in the build to break a circular build-time
dependency with python-sphinx; disable docs for now

* Thu Jul 22 2010 David Malcolm <dmalcolm@redhat.com> - 2.5-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Tue Jul 13 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.5-1
- Update to upstream version 2.5.
- Create python3 subpackage.
- Minor specfile fixes.
- Add examples directory.
- Thanks to Gareth Armstrong for additional hints.

* Wed Apr 21 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.4.1-1
- Update to 2.4.1.

* Tue Apr 13 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.4-1
- Update to 2.4.

* Tue Feb 23 2010 Thomas Moschny <thomas.moschny@gmx.de> - 2.3.1-1
- Update to 2.3.1.
- Docs are built using Sphinx now.
- Run the testsuite.

* Sat Sep 19 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.2.1-1
- Update to 2.2.1, mainly a bugfix release.
- Remove patch no longer needed.
- Remove conditional for FC-8.
- Compilation of speedup module has to be explicitly requested now.

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sat Jan 10 2009 Thomas Moschny <thomas.moschny@gmx.de> - 2.1.1-1
- Update to 2.1.1 (bugfix release).

* Thu Dec 18 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.1-1
- Update to 2.1, which fixes a number of bugs.
  See http://jinja.pocoo.org/2/documentation/changelog#version-2-1.

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 2.0-3
- Rebuild for Python 2.6

* Tue Jul 22 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-2
- Use rpm buildroot macro instead of RPM_BUILD_ROOT.

* Sun Jul 20 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-1
- Upstream released 2.0.

* Sun Jun 29 2008 Thomas Moschny <thomas.moschny@gmx.de> - 2.0-0.1.rc1
- Modified specfile from the existing python-jinja package.

