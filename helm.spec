%global with_unit_test 0
%if 0%{?fedora}
%global with_devel   1
%global with_bundled 0
%global with_debug   1
%else
%global with_devel   0
%global with_bundled 1
%global with_debug   0
%endif

%if 0%{?with_debug}
%global _dwz_low_mem_die_limit 0
%else
%global debug_package   %{nil}
%endif


%global provider        github
%global provider_tld    com
%global project         helm
%global repo            helm
# https://github.com/helm/helm
%global provider_prefix %{provider}.%{provider_tld}/%{project}/%{repo}
%global import_path     k8s.io/helm
%global commit          2e55dbe1fdb5fdb96b75ff144a339489417b146b
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

%global helm_version            2.11.0
%global helm_git_version        v%{helm_version}
# Needed otherwise "version_ldflags=$(kube::version_ldflags)" doesn't work
%global _buildshell  /bin/bash
%global _checkshell  /bin/bash
##############################################

Name:           helm
Version:        %{helm_version}
Release:        1%{?dist}
Summary:        The Kubernetes Package Manager
License:        ASL 2.0
URL:            https://%{import_path}
Source0:        https://%{provider_prefix}/archive/%{commit}/%{repo}-%{shortcommit}.tar.gz

%description
%{summary}

%if 0%{?with_devel}
%package devel
Summary:       %{summary}
BuildArch:     noarch


%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{import_path} prefix.
%endif

%prep
%setup
# Move all the code under src/k8s.io/kubernetes directory
mkdir -p src/k8s.io/helm
mv $(ls | grep -v "^src$") src/k8s.io/helm/.
###############

%build
%gobuildroot
export GOPATH=$(pwd)
export PATH=$GOPATH/bin:$PATH
pushd src/k8s.io/helm/
#go build ./cmd/helm
make bootstrap
#%gobuild -o bin/helm %{import_path}/cmd/helm
popd

#%install
## source codes for building projects
#%if 0%{?with_devel}
#install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
#echo "%%dir %%{gopath}/src/%%{import_path}/." >> devel.file-list
## find all *.go but no *_test.go files and generate devel.file-list
#for file in $(find . \( -iname "*.go" -or -iname "*.s" \) \! -iname "*_test.go") ; do
#    dirprefix=$(dirname $file)
#    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
#    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
#    echo "%%{gopath}/src/%%{import_path}/$file" >> devel.file-list
#
#    while [ "$dirprefix" != "." ]; do
#        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
#        dirprefix=$(dirname $dirprefix)
#    done
#done
#%endif
#
## testing files for this project
#%if 0%{?with_unit_test} && 0%{?with_devel}
#install -d -p %{buildroot}/%{gopath}/src/%{import_path}/
## find all *_test.go files and generate unit-test-devel.file-list
#for file in $(find . -iname "*_test.go") ; do
#    dirprefix=$(dirname $file)
#    install -d -p %{buildroot}/%{gopath}/src/%{import_path}/$dirprefix
#    cp -pav $file %{buildroot}/%{gopath}/src/%{import_path}/$file
#    echo "%%{gopath}/src/%%{import_path}/$file" >> unit-test-devel.file-list
#
#    while [ "$dirprefix" != "." ]; do
#        echo "%%dir %%{gopath}/src/%%{import_path}/$dirprefix" >> devel.file-list
#        dirprefix=$(dirname $dirprefix)
#    done
#done
#%endif
#
#%if 0%{?with_devel}
#sort -u -o devel.file-list devel.file-list
#%endif
#
#%check
#%if 0%{?with_check} && 0%{?with_unit_test} && 0%{?with_devel}
#%if ! 0%{?with_bundled}
#export GOPATH=%{buildroot}/%{gopath}:%{gopath}
#%else
## No dependency directories so far
#
#export GOPATH=%{buildroot}/%{gopath}:%{gopath}
#%endif

%changelog
* Mon Sep 17 2018 Spyros Trigazis <strigazi@gmail.com>
- Initial package
