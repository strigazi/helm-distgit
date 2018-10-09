# http://github.com/helm/helm
%global goipath         github.com/helm/helm
Version:                v2.11.0
%gometa
#%global man_version     v2.11.0

Name:           helm
Release:	1%{?dist}
Summary:	The Kubernetes Package Manager
License:	ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildArch:      noarch

BuildRequires: golang(github.com/BurntSushi/toml)
BuildRequires: golang(github.com/Masterminds/semver)
BuildRequires: golang(github.com/Masterminds/sprig)
BuildRequires: golang(github.com/Masterminds/vcs)
BuildRequires: golang(github.com/asaskevich/govalidator)
BuildRequires: golang(github.com/cyphar/filepath-securejoin)
BuildRequires: golang(github.com/evanphx/json-patch)
BuildRequires: golang(github.com/ghodss/yaml)
BuildRequires: golang(github.com/gobwas/glob)
BuildRequires: golang(github.com/golang/protobuf/proto)
BuildRequires: golang(github.com/golang/protobuf/ptypes/any)
BuildRequires: golang(github.com/golang/protobuf/ptypes/timestamp)
BuildRequires: golang(github.com/grpc-ecosystem/go-grpc-prometheus)
BuildRequires: golang(github.com/spf13/pflag)
BuildRequires: golang(github.com/technosophos/moniker)
BuildRequires: golang(golang.org/x/crypto/openpgp)
BuildRequires: golang(golang.org/x/crypto/openpgp/clearsign)
BuildRequires: golang(golang.org/x/crypto/openpgp/packet)
BuildRequires: golang(golang.org/x/net/context)
BuildRequires: golang(google.golang.org/grpc)
BuildRequires: golang(google.golang.org/grpc/credentials)
BuildRequires: golang(google.golang.org/grpc/health/grpc_health_v1)
BuildRequires: golang(google.golang.org/grpc/keepalive)
BuildRequires: golang(google.golang.org/grpc/metadata)
BuildRequires: golang(gopkg.in/yaml.v2)
BuildRequires: golang(k8s.io/api/apps/v1)
BuildRequires: golang(k8s.io/api/apps/v1beta1)
BuildRequires: golang(k8s.io/api/apps/v1beta2)
BuildRequires: golang(k8s.io/api/batch/v1)
BuildRequires: golang(k8s.io/api/core/v1)
BuildRequires: golang(k8s.io/api/extensions/v1beta1)
BuildRequires: golang(k8s.io/apimachinery/pkg/api/equality)
BuildRequires: golang(k8s.io/apimachinery/pkg/api/errors)
BuildRequires: golang(k8s.io/apimachinery/pkg/apis/meta/v1)
BuildRequires: golang(k8s.io/apimachinery/pkg/fields)
BuildRequires: golang(k8s.io/apimachinery/pkg/labels)
BuildRequires: golang(k8s.io/apimachinery/pkg/runtime)
BuildRequires: golang(k8s.io/apimachinery/pkg/types)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/intstr)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/strategicpatch)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/validation)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/wait)
BuildRequires: golang(k8s.io/apimachinery/pkg/version)
BuildRequires: golang(k8s.io/apimachinery/pkg/watch)
BuildRequires: golang(k8s.io/client-go/discovery)
BuildRequires: golang(k8s.io/client-go/kubernetes)
BuildRequires: golang(k8s.io/client-go/kubernetes/typed/core/v1)
BuildRequires: golang(k8s.io/client-go/kubernetes/typed/extensions/v1beta1)
BuildRequires: golang(k8s.io/client-go/rest)
BuildRequires: golang(k8s.io/client-go/tools/clientcmd)
BuildRequires: golang(k8s.io/client-go/tools/portforward)
BuildRequires: golang(k8s.io/client-go/transport/spdy)
BuildRequires: golang(k8s.io/client-go/util/homedir)
BuildRequires: golang(k8s.io/helm/pkg/chartutil)
BuildRequires: golang(k8s.io/helm/pkg/engine)
BuildRequires: golang(k8s.io/helm/pkg/getter)
BuildRequires: golang(k8s.io/helm/pkg/helm/environment)
BuildRequires: golang(k8s.io/helm/pkg/helm/helmpath)
BuildRequires: golang(k8s.io/helm/pkg/hooks)
BuildRequires: golang(k8s.io/helm/pkg/ignore)
BuildRequires: golang(k8s.io/helm/pkg/kube)
BuildRequires: golang(k8s.io/helm/pkg/lint/rules)
BuildRequires: golang(k8s.io/helm/pkg/lint/support)
BuildRequires: golang(k8s.io/helm/pkg/manifest)
BuildRequires: golang(k8s.io/helm/pkg/plugin)
BuildRequires: golang(k8s.io/helm/pkg/plugin/cache)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/chart)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/release)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/rudder)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/services)
BuildRequires: golang(k8s.io/helm/pkg/proto/hapi/version)
BuildRequires: golang(k8s.io/helm/pkg/provenance)
BuildRequires: golang(k8s.io/helm/pkg/releasetesting)
BuildRequires: golang(k8s.io/helm/pkg/releaseutil)
BuildRequires: golang(k8s.io/helm/pkg/renderutil)
BuildRequires: golang(k8s.io/helm/pkg/repo)
BuildRequires: golang(k8s.io/helm/pkg/resolver)
BuildRequires: golang(k8s.io/helm/pkg/rudder)
BuildRequires: golang(k8s.io/helm/pkg/storage)
BuildRequires: golang(k8s.io/helm/pkg/storage/driver)
BuildRequires: golang(k8s.io/helm/pkg/storage/errors)
BuildRequires: golang(k8s.io/helm/pkg/strvals)
BuildRequires: golang(k8s.io/helm/pkg/sympath)
BuildRequires: golang(k8s.io/helm/pkg/tiller/environment)
BuildRequires: golang(k8s.io/helm/pkg/timeconv)
BuildRequires: golang(k8s.io/helm/pkg/tlsutil)
BuildRequires: golang(k8s.io/helm/pkg/urlutil)
BuildRequires: golang(k8s.io/helm/pkg/version)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/legacyscheme)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/v1/pod)
BuildRequires: golang(k8s.io/kubernetes/pkg/apis/batch)
BuildRequires: golang(k8s.io/kubernetes/pkg/apis/core)
BuildRequires: golang(k8s.io/kubernetes/pkg/apis/core/v1/helper)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset/typed/core/internalversion)
BuildRequires: golang(k8s.io/kubernetes/pkg/controller/deployment/util)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/cmd/get)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/cmd/util)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/genericclioptions)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/genericclioptions/resource)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/validation)
BuildRequires: golang(github.com/gogo/protobuf/proto)
BuildRequires: golang(github.com/spf13/cobra)
BuildRequires: golang(github.com/stretchr/testify/assert)
BuildRequires: golang(github.com/stretchr/testify/require)
BuildRequires: golang(golang.org/x/crypto/openpgp/errors)
BuildRequires: golang(k8s.io/apimachinery/pkg/api/meta)
BuildRequires: golang(k8s.io/apimachinery/pkg/runtime/schema)
BuildRequires: golang(k8s.io/apimachinery/pkg/util/yaml)
BuildRequires: golang(k8s.io/client-go/kubernetes/fake)
BuildRequires: golang(k8s.io/client-go/rest/fake)
BuildRequires: golang(k8s.io/client-go/testing)
BuildRequires: golang(k8s.io/helm/cmd/helm/installer)
BuildRequires: golang(k8s.io/helm/pkg/helm)
BuildRequires: golang(k8s.io/helm/pkg/repo/repotest)
BuildRequires: golang(k8s.io/kubernetes/pkg/api/testapi)
BuildRequires: golang(k8s.io/kubernetes/pkg/client/clientset_generated/internalclientset/fake)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/cmd/testing)
BuildRequires: golang(k8s.io/kubernetes/pkg/kubectl/scheme)

%description
The Kubernetes Package Manager

%prep
%gosetup -q

%build
%gobuildroot
%gobuild -o _bin/helm    %{goipath}/cmd/helm

%install
install -D -p -m 0755 _bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%doc *.md
%{_bindir}/%{name}

%changelog
* Mon Sep 17 2018 root - 0-0.1.git71ba25a
- First package for Fedora
