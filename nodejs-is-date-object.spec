%{?nodejs_find_provides_and_requires}
Name:                nodejs-is-date-object
Version:             1.0.1
Release:             1
Summary:             Is this value a JS Date object?
License:             MIT
URL:                 https://github.com/ljharb/is-date-object
Source0:             https://registry.npmjs.org/is-date-object/-/is-date-object-%{version}.tgz
BuildArch:           noarch
ExclusiveArch:       %{nodejs_arches} noarch
BuildRequires:       nodejs-packaging npm(tape)
%description
Is this value a JS Date object? This module works cross-realm/iframe, and
despite ES6 @@toStringTag.

%prep
%setup -q -n package
rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/is-date-object
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/is-date-object
%nodejs_symlink_deps

%check
%nodejs_symlink_deps --check
%{__nodejs} --harmony --es-staging test.js

%files
%{!?_licensedir:%global license %doc}
%doc README.md CHANGELOG.md
%license LICENSE
%{nodejs_sitelib}/is-date-object

%changelog
* Thu Aug 20 2020 wangxiao <wangxiao65@huawei.com> - 1.0.1-1
- Package init
